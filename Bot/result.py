import requests 


def get_result(semester_id, student_id):
    url = f"http://203.190.10.22:8189/result?grecaptcha&semesterId={semester_id}&studentId={student_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

  

