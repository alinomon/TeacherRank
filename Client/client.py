from turtle import goto
import requests, sys

endpointReg = "http://127.0.0.1:8000/api/register/"
endpointLogin = "http://127.0.0.1:8000/api/login/"
endpointList = "http://127.0.0.1:8000/api/list/"
endpointRate = "http://127.0.0.1:8000/api/rate/"
endpointView = "http://127.0.0.1:8000/api/view/"
endpointAverage = "http://127.0.0.1:8000/api/average/"

kill = 0
while kill != -1:
    selection = input("Please type out commands as they appear in the menus\n\nlogin\nregister\n\n> ")

    if(selection == "register"):# Go to Register Function RETURNS: (1, if account created successfully and logged in)(0, if account already exists)
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")
        response = requests.post(endpointReg, params={"username":username, "email": email, "password": password})
    if(selection == "login"):# Go to Log In Function RETURNS: (2, if log in successful)(3, log in unsuccessful)
        username = input("Username: ")
        password = input("Password: ")
        response = requests.post(endpointLogin, params={"username":username, "password": password})

    if(response.text == '1' or response.text == '2'):#User Logged in and/or Account Created, Main Menu with all functions displayed
        if(response.text == '1'):
            killmain = 0
            print("Account Created Successfully! Logging in...")
            #Start of Main Screen Functionality
            while killmain != -1:
                print("Welcome to TeacherRank! Please select a menu option (As listed verbatim):\n")
                selection_main = input("list\nview\naverage \"professor_id\" \"module_code\"\nrate \"professor_id\" \"module_code\" \"year\" \"semester\" \"rating\"\nlogout\n\n> ")
                token_select = selection_main.split()
                #Selection Block
                if(token_select[0] == 'list'):
                    response = requests.get(endpointList)
                    print("\n\n" + response.text)
                elif(token_select[0] == 'view'):
                    response = requests.get(endpointView)
                    print("\n\n" + response.text)
                elif(token_select[0] == 'average'):
                    professor_id = token_select[1]
                    module_code = token_select[2]
                    response = requests.get(endpointAverage, params={"professor_id":professor_id, "module_code": module_code})
                    print("\n\n" + response.text)
                elif(token_select[0] == 'rate'):
                    professor_id = token_select[1]
                    module_code = token_select[2]
                    year = token_select[3]
                    semester = token_select[4]
                    rating = token_select[5]
                    response = requests.post(endpointRate, params={"professor_id":professor_id, "module_code": module_code, "year": year, "semester": semester, "rating": rating})
                    print("\n\n" + response.text)
                elif(token_select[0] == 'logout'):
                    killmain = -1
                    print("\n\nLogging out...")
        if(response.text == '2'):
            print("Log In Successful!")
            killmain = 0
            #Start of Main Screen Functionality
            while killmain != -1:
                print("Welcome to TeacherRank! Please select a menu option (As listed verbatim):\n")
                selection_main = input("list\nview\naverage \"professor_id\" \"module_code\"\nrate \"professor_id\" \"module_code\" \"year\" \"semester\" \"rating\"\nlogout\n\n> ")
                token_select = selection_main.split()
                #Selection Block
                if(token_select[0] == 'list'):
                    response = requests.get(endpointList)
                    print("\n\n" + response.text)
                elif(token_select[0] == 'view'):
                    response = requests.get(endpointView)
                    print("\n\n" + response.text)
                elif(token_select[0] == 'average'):
                    professor_id = token_select[1]
                    module_code = token_select[2]
                    response = requests.get(endpointAverage, params={"professor_id":professor_id, "module_code": module_code})
                    print("\n\n" + response.text)
                elif(token_select[0] == 'rate'):
                    professor_id = token_select[1]
                    module_code = token_select[2]
                    year = token_select[3]
                    semester = token_select[4]
                    rating = token_select[5]
                    response = requests.post(endpointRate, params={"professor_id":professor_id, "module_code": module_code, "year": year, "semester": semester, "rating": rating})
                    print("\n\n" + response.text)
                elif(token_select[0] == 'logout'):
                    killmain = -1
                    print("\n\nLogging out...")
    elif(response.text == '0'):#Account already exists  
        print("Account with that email already exists! Returning to start screen...")
    elif(response.text == '3'):#Log in unsuccessful
        print("Log In Unsuccessful. Returning to start screen...")

"""
if(sys.argv[1] == "register" or sys.argv[1] == "login"):#Register and Log InFunction
    if(sys.argv[1] == "register"):# Go to Register Function RETURNS: (1, if account created successfully and logged in)(0, if account already exists)
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")
        response = requests.post(endpointReg, params={"username":username, "email": email, "password": password})
    if(sys.argv[1] == "login"):# Go to Log In Function RETURNS: (2, if log in successful)(3, log in unsuccessful)
        username = input("Username: ")
        password = input("Password: ")
        response = requests.post(endpointLogin, params={"username":username, "password": password})

    if(response.text == '1' or response.text == '2'):#User Logged in and/or Account Created, Main Menu with all functions displayed
        if(response.text == '1'):
            print("Account Created Successfully! Logging in...")
        if(response.text == '2'):
            print("Log In Successful!")
    elif(response.text == '0'):#Account already exists  
        print("Account with that email already exists! Returning to start screen...")
    elif(response.text == '3'):#Log in unsuccessful
        print("Log In Unsuccessful. Returning to start screen...")

#Start of Main Screen Functionality
print("Welcome to TeacherRank! Please select a menu option (As listed verbatim):\n")
print("list\nview\naverage \"professor_id\" \"module_code\"\nrate \"professor_id\" \"module_code\" \"year\" \"semester\" \"rating\"\nlogout\n")

#Selection Block
if(sys.argv[1] == 'list'):
    response = requests.get(endpointList)
    print(response.text)
elif(sys.argv[1] == 'view'):
    response = requests.get(endpointView)
    print(response.text)
elif(sys.argv[1] == 'average'):
    professor_id = sys.argv[2]
    module_code = sys.argv[3]
    response = requests.get(endpointAverage, params={"professor_id":professor_id, "module_code": module_code})
    print(response.text)
elif(sys.argv[1] == 'rate'):
    professor_id = sys.argv[2]
    module_code = sys.argv[3]
    year = sys.argv[4]
    semester = sys.argv[5]
    rating = sys.argv[6]
    response = requests.post(endpointRate, params={"professor_id":professor_id, "module_code": module_code, "year": year, "semester": semester, "rating": rating})
    print(response.text)
elif(sys.argv[1] == 'logout'):
    print("Log Out Function")
"""