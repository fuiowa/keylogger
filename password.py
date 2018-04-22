import subprocess
import os.path
import sys

prompt = "config/promptWindow.txt"

def getStr(p):
	input = str(p.communicate()[0]).strip()
	if sys.version_info[0] == "2":
		return input
	return input[2:len(input)-3]

def verify(pw):
	s = subprocess.Popen("echo "+pw+" | sudo -S echo success",shell=True,stdout=subprocess.PIPE)
	if "success" not in getStr(s):
		return False
	return True

def getPassword():
	pw = "password"
	while(not verify(pw)):
		p = subprocess.Popen("osascript "+prompt,shell=True,stdout=subprocess.PIPE)
		pw = getStr(p)
		print(pw)

	f = open("config/password.txt","w")
	f.write(pw)
	f.close()