from dotenv import load_dotenv

load_dotenv("config.env")

HEROKU = True  # NOTE Make it false if you're not deploying on heroku or docker.

if HEROKU:
    from os import environ

    BOT_TOKEN = "2026504958:AAFgjj1Cp7qv27ibKuXOGkss165EaSPjSds"
    API_ID = 7307631
    API_HASH = "0fe96911f6b94a6f6bbec202adbfaaf2"
    )
    SESSION_STRING = environ.get("SESSION_STRING", None)
    USERBOT_PREFIX = environ.get("USERBOT_PREFIX", ".")
    SUDO_USERS_ID = [
        int(x) for x in environ.get("SUDO_USERS_ID", "").split()
    ]
    LOG_GROUP_ID = -1001563789052
    GBAN_LOG_GROUP_ID = -1001563789052
    MESSAGE_DUMP_CHAT = -1001563789052
    WELCOME_DELAY_KICK_SEC = int(
        environ.get("WELCOME_DELAY_KICK_SEC", None)
    )
    MONGO_URL = "mongodb+srv://suryaakumar:suryaa737@cluster0.ltkky.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    ARQ_API_URL = "https://thearq.tech"
    ARQ_API_KEY = environ.get("ARQ_API_KEY", None)
    LOG_MENTIONS = bool(int(environ.get("LOG_MENTIONS", None)))
    RSS_DELAY = int(environ.get("RSS_DELAY", None))
    PM_PERMIT = bool(int(environ.get("PM_PERMIT", None)))
else:
    BOT_TOKEN = "2026504958:AAFgjj1Cp7qv27ibKuXOGkss165EaSPjSds"
    API_ID = 7307631
    API_HASH = "0fe96911f6b94a6f6bbec202adbfaaf2"
    USERBOT_PREFIX = "."
    PHONE_NUMBER = "+919994417013"  
    SUDO_USERS_ID = 1909663268
    ]  # Sudo users have full access to everything, don't trust anyone
    LOG_GROUP_ID = -1001563789052
    GBAN_LOG_GROUP_ID = -1001563789052
    MESSAGE_DUMP_CHAT = -1001563789052
    WELCOME_DELAY_KICK_SEC = 300
    MONGO_URL = "mongodb+srv://suryaakumar:suryaa737@cluster0.ltkky.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    ARQ_API_KEY = "Get this from @ARQRobot"
    ARQ_API_URL = "https://thearq.tech"
    LOG_MENTIONS = True
    RSS_DELAY = 300  # In seconds
    PM_PERMIT = True
