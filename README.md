# Question 2 Solution: Qualifying Offer Display

Jayanth Gunda's solution to Question 2 of the Phillies Baseball R&amp;D Questionnaire.

Steps to run my solution to Question 2:

1. Install any version of Python 3 that corresponds to your Operating System (instructions available at https://www.python.org/downloads/).

2. Confirm that pip is installed on your Operating System (it should be if you have installed Python 3 from python.org) by running one 
   of the following commands in the Command Line (based on the Operating System being used, will display the version of pip currently installed):
   
        On Linux/Unix or macOS: python3 -m pip --version
        On Windows: py -m pip --version
   
3. Install the Python package virtualenv by running one of the following commands in the Command Line (based on the Operating System being used):
   
        On Linux/Unix or MacOS: python3 -m pip install --user virtualenv
        On Windows: py -m pip install --user virtualenv

4. Download this GitHub repository as a ZIP file by clicking on the Code -> "Download ZIP" button at the top right of this page.

5. Extract the downloaded ZIP file into a folder on your Local Machine. Change directory into the extracted folder by running
   the following command in the Command Line:
      
         cd /path/to/extractedFolder

6. Create a Python Virtual Environment called 'env' inside the extracted folder by running one of the following commands in the Command Line
   (based on the Operating System being used):
   
        On Linux/Unix or MacOS: python3 -m venv env
        On Windows: py -m venv env
  
7. Activate the created 'env' virtual environment by running one of the following commands in the Command Line (based on the Operating System 
   shell being used):
   
        On Linux/Unix or MacOS, using the bash shell: source env/bin/activate
        On Linux/Unix or MacOS, using the csh shell: source env/bin/activate.csh
        On Linux/Unix or MacOS, using the fish shell: source env/bin/activate.fish
        On Windows, using the Command Prompt: env\Scripts\activate.bat
        On Windows, using PowerShell: env\Scripts\Activate.ps1
   
8. Install all the Python packages needed to run qualifyingOffer.py within the activated 'env' virtual environment by running the following command
   in the Command Line:

        pip install -r requirements.txt
   
9. Execute the Python program that produces the generated output for Question 2 by running the following command in the Command Line:
   
        python qualifyingOffer.py
