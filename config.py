from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "fe2dec8e960bf8dcb4e4820d81fe7d46")
      API_ID = int(getenv("API_ID", "17718356"))
      AS_COPY = True if getenv("AS_COPY", "True") == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "5989527178:AAGE13kpv859YYecSJr_wSL3oARV0I9DFUM")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001759084765; -1001739641240").replace("\n", " ").split(' '))
