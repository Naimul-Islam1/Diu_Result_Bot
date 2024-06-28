from dotenv import load_env,getenv
import os

load_env()
class Settings:
  APIKEY=os.getenv("APIKEY")
  APPID=os.getenv("APPID")
  BOT_TOKEN=os.getenv("BOT_TOKEN")
  
  

setting=Settings()

