# mrz bot
# ultra forward bot 

from os import environ 

class Config:
    API_ID = environ.get("API_ID", "29478734")
    API_HASH = environ.get("API_HASH", "8bd53e36eceada3329fbe46d9b961d1f")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://UploadLinkToFileBot:UploadLinkToFileBot@cluster0.1gybihh.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = environ.get("BOT_OWNER_ID", "6807518752")
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
