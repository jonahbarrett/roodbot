# About
armchair-expert is a chatbot inspired by old Markov chain IRC bots like PyBorg. It regurgitates what it learns from you in unintentionally hilarious ways.

## Features
- Uses NLP to select the most optimal subjects for which to generate a response
- Uses a Recurrent Neural Network (RNN) to structure and capitalize the output, mimicking sentence structure and capitalization of learned text
- Learns new words in real-time with an n-gram markov chain, which is positionally aware of the distances between different words, creating a more coherent sentence

## Requirements
- 3+ GB of RAM
- python 3.6+
- keras (Tensorflow backend)
- spaCy 2.0.0+
- spacymoji
- numpy
- tweepy
- discord.py
- sqlalchemy

## Installation
There is a Requirements.txt file in the root folder, simply run
```
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```
you need to manually run this part
```
'python -m spacy download en'
```
- You might need to install tensorflow manually and 2.0 should work but may have errors, especially an avx2 systems.

## Setup & Training
Navigate to the CONFIG folder:
- Create a copy of armchair_expert.example.py and rename it to armchair_expert.py
- Create a copy of config/ml.example.py and rename it to config/ml.py
- Make sure you have the spacy 'en' dataset downloaded: 'python -m spacy download en'
- It is preferred to import data first for training before starting the bot.
  - You can use the provided script in "\scripts\import_text_file.py"
    - Simply copy the script to the root folder, together with your txt file and run it as:
      ```
      python import_text_file.py "your-data-file-name-here"
      ```
    - It would look like this: *python import_text_file.py "CAN YOU HEAR ME.txt"*
  - Another option is to let the bot run for a while and learn from the user messages being sent in the servers.
- Be sure to check the discord connector as you can set channels for it to ignore, especially bot commands and what not.
- Every time the bot starts it will train on all new data it acquired since it started up last
- The bots sentence structure model is only trained once on initial start-up. To train it with the most recent acquired data, start the bot with the --retrain-structure flag. If you are noticing the bot is not generating sentences which the structure of learned material, this will help.

# Connectors
## Discord
- Navigate to the CONFIG folder:
- Create a copy of discord.example.py and rename it to discord.py
- Open the discord.py file with your text editor and fill the required fields
  - You will need to register a bot with Discord: https://discordapp.com/developers/applications/me#top
  - Click New Application and set a name for it, click the Bot tab and click add bot
  - Now copy the **Client ID**, **Username#xxxx**, and **TOKEN** to the discord.py file.
- Go back to the Root Directory
- python armchair.py
- When the bot starts you should see a message print to the console containing a link which will allow you to join the bot to a server.

## Twitter
- You will need to create an application on the twitter developer site on your bot's twitter account https://apps.twitter.com
- After creating it, assign it permissions to do direct messages (this isn't default)
- Create an access token for your account
- Copy config/twitter.example.py to config/twitter.py
- Fill in the tokens and secrets along with your handle
- Go back to the Root Directory
- python armchair.py
