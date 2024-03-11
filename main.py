import os
import json
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from llama_index.core import (
    VectorStoreIndex,
)
from llama_index.readers.google.docs.base import GoogleDocsReader
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# If you get SSL certificate error run this </Applications/Python\ 3.6/Install\ Certificates.command>

OPENAI_API_KEY = "PUT YOUR OPEN API KEY HERE"
#ideally have google drive api give you all google docs IDs to train on
GOOGLE_DOCS_IDS = [
    "DOC ID 1", "DOC ID 2"
]
SLACK_BOT_TOKEN = "PUT YOUR SLACK BOT TOKEN HERE"
SLACK_APP_TOKEN = "PUT YOUR SLACK APP TOKEN HERE"


os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
app = App(token=SLACK_BOT_TOKEN)


def authorize_gdocs():
    google_oauth2_scopes = ["https://www.googleapis.com/auth/documents.readonly"]
    creds = None
    if os.path.exists("token_copy.json"):
        creds = Credentials.from_authorized_user_file(
            "token_copy.json", google_oauth2_scopes
        )
    if not creds or not creds.valid:
        # Check if credentials are not present or invalid
        if not creds or not creds.valid:
            # If credentials are expired and refresh token is available, refresh the credentials
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                # If credentials are not available, initiate the OAuth2 flow
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials_copy.json", google_oauth2_scopes
                )
                # Run the local server to get the credentials
                creds = flow.run_local_server(port=8080)
            # Save the credentials to a file for future use
            with open("token_copy.json", "w") as token:
                token.write(creds.to_json())
    return creds

@app.event("app_mention")
def handle_mention(event, say):
    print("received")
    # Access message details from the event object
    message = event["text"]
    channel = event["channel"]
    # Execute the query and get the response
    message = message.replace("<@U06MLP9DL8N>", "")
    print(message)
    response = query_engine.query(message)
    say({"channel": channel, "text": str(response)})

# If the script is run directly (not imported as a module), execute the following code
if __name__ == "__main__":
    # Authorize Google Docs
    authorize_gdocs()
    # Load data from Google Docs
    documents = GoogleDocsReader().load_data(document_ids=GOOGLE_DOCS_IDS)
    # print(documents)
    # Create an index from the documents
    index = VectorStoreIndex.from_documents(documents)
    # Create a query engine from the index
    query_engine = index.as_query_engine()

    SocketModeHandler(app, SLACK_APP_TOKEN).start()
    # app.start(port=3000)
