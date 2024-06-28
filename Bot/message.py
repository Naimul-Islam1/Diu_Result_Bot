class Messages:
  

  def get_startmessage():
      return """
  <b> <i>
  Welcome to the Result Bot! Use /cmd: /help to see available commands.
  </i></b>
  """
  
  def get_helpmessage():
      return """
Available commands:\n/start - Welcome message\n/help - List of commands\n/result - Get semester results
"""


  def get_resultmessage():
        return """
  Please provide the <b> <i>semesterID </i> and <i>studentID</i></b> in the format: <b> <i> semesterId studentId </i> </b>
  
  """
  
  


messagex=Messages()

  