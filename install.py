import subprocess


f = open("config/password.txt","w")
pw = "password"
while not password.verify(pw):
	password.getPassword()
	pw = f.readline()
	password.verify(pw)

subprocess.Popen("echo "+pw+" | sudo -S easy_install pynput",shell=True)
subprocess.Popen("python main.py",shell=True)