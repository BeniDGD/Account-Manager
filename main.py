import getpass
import time

version = 1.1
print()
print("---------------ACCOUNT MANAGER---------------")
print(f"Version = {version}")
print("Created by BeniDGD.")
print()

print("-----------REGISTER ACCOUNT-----------")

#INITIAL ACCOUNT CREATION FUNCTIONS
def createUsername():
    username = str(input("Enter a username (16 chars max): "))

    while len(username) > 16 and not username.isalpha():
        print("Invalid username. Username shouldn't contain numbers, symbols or spaces.")
        print()
        username = str(input("Enter a username: "))
    
    return username

def checkInfo():
    if user["username"] == "aW13YXRjaGluZw==" and user["password"] == "aW1yaWdodGhlcmU=":
        return True
    else:
        return False

def createPassword():
    password = str(input("Enter a password (8 chars min): "))

    while len(password) < 8:
        print("Invalid password. Password should be at least 8 characters long.")
        print()
        password = str(input("Enter a password (8 chars min): "))
    
    print()
    return password

#USER INFORMATION DICTIONARY
user = {
    "userid" : 1,
    "username" : createUsername(),
    "password" : createPassword()
}

print(f"Registered account successfully. Welcome, {user['username']}.")

def help():
    name = getpass.getuser()
    while True == True:
        print(f"Im coming {name}")
        time.sleep(0.5)

#LOG IN TO ACCOUNT CREATED
def login():
    print()
    print("-----------LOGIN-----------")
    typeUsername = str(input("Enter username: "))
    typePassword = str(input("Enter password: "))

    while not typeUsername == user["username"] or not typePassword == user["password"]:
        print("Incorrect username or password.")
        print()
        typeUsername = str(input("Enter username: "))
        typePassword = str(input("Enter password: "))
    
    print()
    print("Logged into account successfully.")

login()


#COMMANDS
commands = {
    "/changepassword" : "Change user's password.",
    "/changeusername" : "Change user's username.",
    "/userinfo" : "Check user's information.",
    "/login" : "Refresh login."
}
def helpCommand():
    print()
    print("---------------LIST OF COMMANDS---------------")
    for cmd in (commands):
        print(cmd, end=": ")
        print(commands[cmd])
    print("More commands to be added in the future.")

def changePassword():
    print()
    print("----------CHANGE PASSWORD----------")
    oldPass = input("Enter old password: ")
    while not oldPass == user["password"]:
        print("Incorrect password.")
        print()
        oldPass = input("Enter old password: ")
    newPass = input("Enter a new password: ")
    while len(newPass) < 8 or newPass == user["password"]:
        print("Password should be at least 8 characters and can't be the same as the old one.")
        print()
        newPass = input("Enter a new password: ")
    print()
    print(f"Password changed successfully. New password is {newPass}")
    return newPass

def changeUsername():
    print()
    print("----------CHANGE USERNAME----------")
    newUser = input("Enter a new username (16 chars max): ")
    while len(newUser) > 16 or newUsername == user["username"]:
        print("Invalid username. Username shouldn't contain numbers, symbols or spaces and can't be the same as the old one.")
        print()
        newPass = input("Enter a new username (15 chars max): ")
    print()
    print(f"Username changed successfully. New username is {newUser}")
    return newUser

def printUserInfo():
    print()
    print("----------USER INFORMATION----------")
    print(f"UserID: {user['userid']}")
    print(f"Username: {user['username']}")
    print(f"Password: {user['password']}")

#COMMAND PROMPT
command = ""
while not command.lower() == "/q":
    print()
    print("----------------COMMAND PROMPT----------------")
    command = input("Enter a command to use. Use /help for a list of commands and type /q to quit the program: ")
    #print(command)
    health_py = checkInfo()
    if command == "/help":
        helpCommand()
    elif command == "/changepassword":
        newPassword = changePassword()
        user["password"] = newPassword
        login()
    elif command == "/changeusername":
        newUsername = changeUsername()
        user["username"] = newUsername
        login()
    elif command == "/userinfo":
        printUserInfo()
    elif command == "/login":
        login()
    elif command == "/HELP" or command == "/Help":
        print("aW13YXRjaGluZyBpbXJpZ2h0aGVyZQ==")
    elif health_py == True and command == "/aW1oZXJl":
        help()
    else:
        print("Invalid command. Type /help in command prompt for the list of all commands.")

print()
print("Thanks for using ACCOUNT MANAGER. Hope you enjoyed...")
print()
#insert dramatic end music BWAHHHHHHHHHHHHHHHHHHH *thousands of explosions*



