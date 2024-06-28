import requests
import json
from pyrogram import Client, filters
from Bot.settings import setting
from Bot.message import messagex
from Bot.result import get_result



class Bot:
      app = Client("result_bot",
                 api_id=setting.APPID,
                 api_hash=setting.APIKEY, 
                 bot_token=setting.BOT_TOKEN)

    @app.on_message(filters.command("start"))
    async def start(client, message):
        message.reply_text(messagex.get_startmessage())

    @app.on_message(filters.command("help"))
    async def help(client, message):
        message.reply_text(messagex.get_helpmessage())

    @app.on_message(filters.command("result"))
    async def result(client, message):
        message.reply_text("")

    @app.on_message(filters.text & ~filters.command(["start", "help", "result"]))
    async def fetch_result(client, message):
        try:
            semester_id, student_id = message.text.split()
            result = get_result(semester_id, student_id)
            if result:
                cgpa = result.get('cgpa', 'N/A')
                courses = result.get('courses', [])

                table = "Course ID | Course Title | Credits | Grade | Point\n"
                table += "---------------------------------------------------\n"
                for course in courses:
                    table += f"{course['courseId']} | {course['courseTitle']} | {course['totalCredit']} | {course['gradeLetter']} | {course['pointEquivalent']}\n"

                message.reply_text(f"CGPA: {cgpa}\n\n{table}")
            else:
                message.reply_text("Could not fetch results. Please check the semester ID and student ID.")
        except ValueError:
            message.reply_text("Invalid format. Please provide the semester ID and student ID in the format: semesterId studentId")

