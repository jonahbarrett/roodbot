class DiscordApiCredentials(object):
    def __init__(self, token: str):
        self.token = token


# --- "User" Stuff Section ---
# ----------------------------

DISCORD_CLIENT_ID = 69696969696969696969
DISCORD_TOKEN = 'REPLACEME'

DISCORD_CREDENTIALS = DiscordApiCredentials(token=DISCORD_TOKEN)

DISCORD_USERNAME = 'SomeBot#1234'

# Talk normally to the bot like you're conversing, without any prefix or ping
# This requires a channel name, you can add multiple auto talk channels with a comma.
DISCORD_AUTO_TALK = []

# Learn from all servers and channels
# If you have a large server, it will learn from bot channels too, if you enable this be sure to disable the bot from reading the channel.
DISCORD_LEARN_FROM_ALL = False

# Don't learn from any of these channels
DISCORD_LEARN_CHANNEL_EXCEPTIONS = []

# Learn from any of these channels
# If this channel is set, it will ignore DISCORD_LEARN_FROM_ALL setting and will explicitly learn in the channel.
DISCORD_LEARN_CHANNEL = []

# If you want learned messages to be printed in the console
RECEIPT_LOGS = False

# Learn from direct messages
DISCORD_LEARN_FROM_DIRECT_MESSAGE = False

# Always learn from a specific user no matter what other flags are set
# This should be set to a string containing a username like "SomeGuy#1234"
DISCORD_LEARN_FROM_USER = None

# --- Technical Stuff Section ---
# -------------------------------

DISCORD_REMOVE_URL = True
EMOTES_SKIP = True

# Store training data here
DISCORD_TRAINING_DB_PATH = 'db/discord.db'
