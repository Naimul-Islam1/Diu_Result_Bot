import requests
import json
from pyrogram import Client, filters
from Bot.settings import setting
from Bot.message import messagex
from Bot.result import get_result
from Bot.resultformat import get_formatted_result




class Bot:
    app = Client("resultbot",
                 api_id=setting.APPID, 
                 api_hash=setting.APIKEY, 
                 bot_token=setting.BOT_TOKEN)

    @app.on_message(filters.command("start"))
    async def start(client, message):
       await  message.reply_text(messagex.get_startmessage())

    @app.on_message(filters.command("help"))
    async def help(client, message):
      await message.reply_text(messagex.get_helpmessage())

    @app.on_message(filters.command("result"))
    async def result(client, message):
       await message.reply_text(messagex.get_resultmessage())
    
    @app.on_message(filters.command("about"))
    async def about(client, message):
       await message.reply_text(messagex.about())
    
   

    @app.on_message(filters.text & ~filters.command(["start", "help", "result"]))
    async def fetch_result(client, message):
        try:
            semester_id, student_id = message.text.split()
            result = get_result(semester_id, student_id)
            if result:
               
                formatted_result = get_formatted_result(result)
                await message.reply_text(formatted_result)
            else:
                await message.reply_text("Could not fetch results. Please check the semester ID and student ID.")
        except ValueError:
            await message.reply_text("""Invalid format. Please provide the semester ID and student ID in the format: semesterId studentId
                                     \nExample: 241 191-15-2639""" +
                                     messagex.get_resultmessage())

