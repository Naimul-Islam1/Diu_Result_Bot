from dotenv import load_dotenv
import os

load_dotenv()
class Settings:
  APIKEY=os.getenv("APIKEY")
  APPID=os.getenv("APPID")
  BOT_TOKEN=os.getenv("BOT_TOKEN")
  
  

setting=Settings()


