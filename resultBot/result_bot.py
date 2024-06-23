import requests
from pyrogram import Client, filters

# Provided API credentials
api_id = 28793443
api_hash = 'f296fa5e298b76a436d8309dc3480bb9'
bot_token = '7471349714:AAE6_VVTOUhYM5-pLP38eGmuutt84b09PeU'

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
    message.reply_text("Please provide the semester ID and student ID in the format: semesterId studentId. Example:222 222-15-0000")

@app.on_message(filters.text & ~filters.command(["start", "help", "result"]))
def fetch_result(client, message):
    try:
        semester_id, student_id = message.text.split()
        results = get_result(semester_id, student_id)
        
        if results and isinstance(results, list) and len(results) > 0:
            # Assuming the semester information is the same across all courses in the response
            semester_name = results[0].get('semesterName', 'N/A')
            semester_year = results[0].get('semesterYear', 'N/A')
            sgpa = results[0].get('cgpa', 'N/A')
            total_credits = sum(course.get('totalCredit', 0) for course in results)
            
            response_text = f"Semester: {semester_name} {semester_year}\n"
            response_text += f"SGPA: {sgpa}\n"
            response_text += f"Total Credits: {total_credits}\n\n"
            
            #table header
            response_text += "Course ID | Course Title | Credits | Grade | Point\n"
            response_text += "--------------------------------------------------\n"
            
            # course details
            for course in results:
                course_id = course.get('customCourseId', course.get('courseId', 'N/A'))
                course_title = course.get('courseTitle', 'N/A')
                total_credit = course.get('totalCredit', 'N/A')
                grade_letter = course.get('gradeLetter', 'N/A')
                point_equivalent = course.get('pointEquivalent', 'N/A')
                response_text += f"{course_id} | {course_title} | {total_credit} | {grade_letter} | {point_equivalent}\n"

            message.reply_text(response_text)
        else:
            message.reply_text("Invalid Input. Please check the semester ID and student ID.")
    except ValueError:
        message.reply_text("Invalid format. Please provide the semester ID and student ID in the format: semesterId studentId")

app.run()
