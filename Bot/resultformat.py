def get_formatted_result(data):
  
    totalcredit = 0
    for course in data:
        totalcredit += course['totalCredit']
  
    message = f"""
**Result for {data[0]['semesterName']} {data[0]['semesterYear']} (Semester ID: {data[0]['semesterId']})**\n
**Student ID:** {data[0]['studentId']}


`| Course Code | Course Title                      | Credit | Grade | Point |
|-------------|-----------------------------------|--------|-------|-------|`
"""
    for course in data:
        
        message += f"| `{course['customCourseId']}` | {course['courseTitle']} | {course['totalCredit']} | {course['gradeLetter']} | {course['pointEquivalent']} |\n"

    message += f"""
**CGPA:** `{data[0]['cgpa']}`
** Total Credit:{totalcredit}`** 

** _Note: `I` indicates Incomplete grade._ **
"""
    return message



