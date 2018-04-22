import subprocess
import password

f = open("config/password.txt","r")
pw = "password"
while not password.verify(pw):
	password.getPassword()
	pw = f.readline()
	password.verify(pw)

subprocess.Popen("echo "+pw+" | sudo -S pip3 install pynput",shell=True)
subprocess.Popen("python main.py",shell=True)