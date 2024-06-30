from logging import DEBUG, getLogger, StreamHandler, Formatter, FileHandler,WARNING,ERROR,CRITICAL,INFO,basicConfig
from colorama import Fore, Back, Style
from Bot.resultBot import Bot

basicConfig(format=Fore.GREEN+'%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
              
              level=INFO)
  
  

logger = getLogger(__name__)



app=Bot.app


if __name__=="__main__":
  print(Fore.GREEN+"DiU Result Bot Developed by Swadhin & Naimul")
  logger.info("Bot is running")
  app.run()
  
