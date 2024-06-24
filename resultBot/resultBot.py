import requests
import json
from pyrogram import Client, filters



app = Client("result_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def get_result(semester_id, student_id):
    url = f"http://203.190.10.22:8189/result?grecaptcha&semesterId={semester_id}&studentId={student_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Welcome to the Result Bot! Use /help to see available commands.")

@app.on_message(filters.command("help"))
def help(client, message):
    message.reply_text("Available commands:\n/start - Welcome message\n/help - List of commands\n/result - Get semester results")

@app.on_message(filters.command("result"))
def result(client, message):
    message.reply_text("Please provide the semester ID and student ID in the format: semesterId studentId")

@app.on_message(filters.text & ~filters.command(["start", "help", "result"]))
def fetch_result(client, message):
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

app.run()
