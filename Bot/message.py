class Messages:
    
    def __init__(self):
        pass
      

    def get_startmessage(self):
        return """
        **Welcome to the Result Bot!** 📚

        Use cmd:/help to see available commands.

        **Semester ID** and **Student ID** are required to get the result.

        You have to provide the **Semester ID** and **Student ID** to get the result.
        EXAMPLE: `241 191-15-2639`

        If you don't know what these are, please contact your department.

        **Semester ID Examples:**
        * Spring 2024 = `241`
        * Summer 2024 = `242`
        * Fall 2024 = `243`
        * Spring 2025 = `251`
        * Summer 2025 = `252`
        * -----------------
        * Fall 2027 = `273`
        """

    def get_helpmessage(self):
        return """
        **Available commands:**
        - cmd :/start - Welcome message
        - cmd :/help - List of commands
        - cmd :/result- Get semester results
        - cmd :/about - About the bot and developers
        
        """

    def get_resultmessage(self):
        return """
        Please provide the **Semester ID** and **Student ID** in the format:
        ```
        semesterId studentId
        ```
        """

    def about(self):
        return """
        **DiU Result Bot** 🤖 developed by Swadhin & Naimul

        This bot provides semester results for Daffodil International University students.

        To get your result, simply provide your ** Semester ID** and **Student ID **.
        """
messagex=Messages()