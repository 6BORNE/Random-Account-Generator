import os
import random
import string
import json
from time import sleep

chars = string.ascii_letters + string.digits + "!@#$%^&*"
random.seed = (os.urandom(1024))
email = ["@gmail.com", "@hotmail.com", "@outlook.com", "@live.com", "@yahoo.com"]
names = json.loads(open('E:/random_account_gen/names.json').read())
words = json.loads(open('E:/random_account_gen/words.json').read())
print("< By Victor Krenzel 24/12/2020 >")
sleep(2)
input("[+] Press any key to generate random accounts . . . ")
sleep(1)
print("< By Victor Krenzel 24/12/2020 >")

for name in names:
    name_extra = ''.join(random.choice(string.digits) for i in range(random.randint(1, 4)))
    first_name = ''.join(random.choice(names)) 
    
    username = first_name.lower() + "." + name_extra + ''.join(random.choice(email))
    password = random.choice(words) + ''.join(random.choice(chars) for i in range(random.randint(1, 5)))
    print(username, ":", password)
input("Enter any key to exit . . . ")