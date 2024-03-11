# ema

Project: A slack-bot that is able to do contexual conversations based on google documents.

![image](https://github.com/Ashish1013/e_project/assets/25063446/65dee6c0-48ee-4806-b791-16e64bee7882)


Limitations: There are many as of now. Refer the image below to know more.

![image](https://github.com/Ashish1013/e_project/assets/25063446/944bbe7f-2381-48c4-94a0-6cd8c474ac18)

_________________________________________________________________________________________________________
This project uses a Python virtual environment to manage dependencies.

## Setting up the Virtual Environment

Every time you start a new terminal session, you need to activate the virtual environment. You can do this by navigating to the project's root directory and running the following command:

```bash
source venv/bin/activate
```

## Manage Dependencies

Dependencies for this project are listed in the requirements.txt file. If you add new dependencies to this file, you need to install them. Ensure that your virtual environment is activated, then run the following command:

```bash
pip install -r requirements.txt
```

## Slack App Setup (slack bot)

Create a slack app preferably with your personal email and personal workspace. (https://api.slack.com/apps)

**Follow the following steps to set up for slack app**

This includes steps to get your SLACK_BOT_TOKEN and SLACK_APP_TOKEN tokens.

https://slack.dev/bolt-python/tutorial/getting-started
https://api.slack.com/tutorials/tracks/responding-to-app-mentions
https://api.slack.com/messaging/retrieving

## OpenAI API Key
Create an OpenAI account and get the API key using the following link. https://platform.openai.com/api-keys
Put this link at an appropriate place in the main.py

## Google authentication setup

When run, the script will automatically ask for google authentication. 
Please select the google account for which you have provided the document IDs in main.py.
Currently the script manually takes in the document_ids to train the model.

To find the id of a google document navigate to the Google Drive web. Right click on the file and select 'get sharable link'. The File ID is the last part of that link, after id= ''

**Getting google OAUTH 2.0 credentials (back up)**
Create OAuth 2.0 Client ID in google console and save the credential json as "credentials_copy.json"
Follow these steps to get credentials: https://medium.com/@tony.infisical/guide-to-using-oauth-2-0-to-access-google-apis-dead94d6866d

## Final step
After the environment is set and you have edited the main.py to include your tokens/ auth keys run the main.py file.
