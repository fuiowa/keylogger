import subprocess
import os.path


prompt = "config/promptWindow.txt"
warning = "config/warningWindow.txt"

def getStr(p):
	input = str(p.communicate()[0]).strip()
	return input[2:len(input)-3]

def verify(pw):
	s = subprocess.Popen("echo "+pw+" | sudo -S echo success",shell=True,stdout=subprocess.PIPE)
	if "success" not in getStr(s):
		return False
	return True

def getPassword():
	pw = "password"
	first_time = True
	while(not verify(pw)):
		if not first_time:
			choice = "something"
			while("Continue" not in choice):
				w = subprocess.Popen("osascript "+warning,shell=True,stdout=subprocess.PIPE)
				choice = getStr(w)
		p = subprocess.Popen("osascript "+prompt,shell=True,stdout=subprocess.PIPE)
		pw = getStr(p)
		first_time = False

	f = open("config/password.txt","w")
	f.write(pw)
	f.close()


