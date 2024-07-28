# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27500622"))
API_HASH = getenv("API_HASH", "d45e39daf0e869ad0807311f14fb83fd")
BOT_TOKEN = getenv("BOT_TOKEN", "6713397211:AAE5o9r-FamtWXTINNcxWWaCGeBuRVaLkrg")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7008835401 6332124181").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://SUSHIL-SINGH:aIKAr5fTy2hH2zU8@sushil-singh.rop0dec.mongodb.net/?retryWrites=true&w=majority&appName=SUSHIL-SINGH")
LOG_GROUP = getenv("LOG_GROUP", "-1002228957170")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002180994841"))
