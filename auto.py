#!python3

from pynput.keyboard import Controller, Key
from github import Github
import os
import sys
import _thread
import time


keyboard = Controller()
project_name = sys.argv[1]

def press_keys():
    time.sleep(20)
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.release(Key.enter)
    time.sleep(5)
    for char in project_name:
        time.sleep(0.5)
        keyboard.press(char)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    keyboard.press("Y")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    

def start_project():
    print("[+] starting project")
    os.system("create-react-native-app " + project_name )
    print("[+] Project Created")
    os.system("cd " + project_name)
    link_to_github()

def link_to_github():
    username = "louiskop"
    password = "cellc022"
    user = Github(username, password).get_user()
    repo = user.create_repo(project_name)
    print("[+] repo created")
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "Initial-commit" ')
    os.system("git remote add origin https://github.com/louiskop/" + project_name + ".git")
    os.system("git remote set-url origin https://github.com/louiskop/" + project_name + ".git")
    os.system("git push -u origin master")
    print("[+] Project created and linked to Github!")
    print("happy coding!")


try:
    _thread.start_new_thread( start_project, () )
    _thread.start_new_thread( press_keys, () )
   
except:
    print("Error: unable to start thread")

while 1:
    pass
