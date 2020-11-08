# About
Armchair-expert is a chatbot inspired by old Markov chain IRC bots like PyBorg. It regurgitates what it learns from you in unintentionally hilarious ways.
## This is a fork of [csvance/armchair-expert](https://github.com/csvance/armchair-expert)
- has been updated to work with discord changes
- added minor changes to the discord interactions
- Filters punctuations away for better or worse, it won't respond to random punctuations
- is a private bot, which you will need to run your own instance
- you will need to add your own data-set
- some specific packages you need to install, for the bot to work properly

## Features
- Uses NLP to select the most optimal subjects for which to generate a response
- Uses a Recurrent Neural Network (RNN) to structure and capitalize the output, mimicking sentence structure and capitalization of learned text
- Learns new words in real-time with an n-gram markov chain, which is positionally aware of the distances between different words, creating a more coherent sentence

## Requirements
- 3+ GB of RAM
- python 3.6+ minimum
- keras (Tensorflow backend)
- spaCy 2.0.0+
- spacymoji
- numpy
- tweepy
- discord.py
- sqlalchemy

## Installation
*I really recommend you install this in a virtual env, as you will install specific versions of some packages which might conflict on what you have. If not, you can just install it normally.*
- This was ran under a **Windows** enviroment, so `python` could be `python3` in linux.
**First:** Run the Requirements.txt file in the root folder:
```
pip install -r requirements.txt
```

**Then:** Run the command in the same root folder:
```
python -m spacy download en
```
- You can skip this

**Tensorflow version:**
- For my case I ran **1.14** for Python 3.7
```
pip install tensorflow
```
- You can technically run that and just proceed, but I cannot guarantee you won't have any issues when running it. You will get avx2 etc errors.
- However the new versions beyond 1.15 has code breaking errors between keras and tensorflow. Beware of which versions you install.
- You can look through this repo [tensorflow windows](https://github.com/fo40225/tensorflow-windows-wheel). Provided by **fo40225**.
  - then select which tensorflow version you want together with your python version.
  - download and install via pip
- Alternatively, you can also run intel optimised version of tensorflow from [here](https://pypi.org/project/intel-tensorflow/1.14.0/).

### Setup & Training
Navigate to the `\armchairexpert\config` folder:
- Create a copy of armchair_expert.example.py and rename it to armchair_expert.py
- Create a copy of config/ml.example.py and rename it to config/ml.py
- Then go back to the root folder `\armchairexpert\`
- It is preferred to import data first for training before starting the bot.
  - You can use the provided import script in `\scripts\import_text_file.py`
  - Simply copy the script to the root folder, together with your txt file and run it as:
    `python import_txt.py "<your-data-file-name-here>"`
  - It would look like this: `python import_text_file.py "CAN YOU HEAR ME.txt"`
  - Another option is to let the bot run for a while and learn from the user messages being sent in the servers.
- Every time the bot starts it will train on all new data it acquired since it started up last
-The bots sentence structure model is only trained once on initial start-up.
To train it with the most recent acquired data, start the bot with the `--retrain-structure flag`. If you are noticing the bot is not generating sentences which the structure of learned material, this will help.

### Connectors
#### Discord
- Before you can run the bot, you will need to have a [Discord app](https://discord.com/) account and register a [discord bot](https://discord.com/developers/applications/me#top) to interface with.
- You can take a look and see a step by step instructions on how to create and add the bot into your server, [Here](https://discordpy.readthedocs.io/en/latest/discord.html).

##### Filling in the discord bot info and configuration
- Navigate to the `\armchairexpert\config` folder:
- Create a copy of discord.example.py and rename it to discord.py
- Open the discord.py file with your text editor and fill the required fields.
- Now copy the **Client ID**, **Username#xxxx**, and **TOKEN** to the discord.py file.
- Change the configuration as you wish, for instance enabling learn from all, etc.
- Go back to the `\armchairexpert\` Directory
- open console within the directory and run, `python armchair.py`
- When the bot starts you should see a message print to the console containing a link which will allow you to join the bot to a server.

#### Twitter (I've only prioritised discord and is not updated, not sure if twitter changed their api or not. Proceed at your own expense.)
You can just skip this if you want discord.
- You will need to create an application on the twitter developer site on your bot's twitter account https://apps.twitter.com
- After creating it, assign it permissions to do direct messages (this isn't default)
- Create an access token for your account
- Copy config/twitter.example.py to config/twitter.py
- Fill in the tokens and secrets along with your handle
- Go back to the Root Directory
- python armchair.py
