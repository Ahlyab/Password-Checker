import requests
import hashlib
import sys
import os
from requests.exceptions import ConnectionError
from time import sleep

def system_pause():
    return os.system('pause')


def logo():
    print( " _____                                    _ ")
    print( "|  __ \                                  | |")
    print( "| |__) |_ _ ___ _____      _____  _ __ __| |")
    print( "|  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |")
    print( "| |  | (_| \__ \__ \\\ V  V / (_) | | | (_| |")
    print( "|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|")
    print( "         _               _                  ")
    print( "        | |             | |                 ")
    print( "     ___| |__   ___  ___| | _____ _ __      ")
    print( "    / __| '_ \ / _ \/ __| |/ / _ \ '__|     ")
    print( "   | (__| | | |  __/ (__|   <  __/ |        ")
    print( "    \___|_| |_|\___|\___|_|\_\___|_|        ")
                                                 

def author():
    print("-----------------------------------------------------------")
    print("\t\t Developer : Ahlyab ")
    print("\tThis is developed for testing your password \n\tIf it ever been leaked in data breaches")
    print("\t\t !!! Warning !!!\n\tFor any misuse Developer is not responsible!")
    print("-----------------------------------------------------------\n")


def input_password():
    password = input('>> Enter your password: ')
    return password


def request_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status_code}, check the API and try again!')
    return response


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five_char, tail = sha1password[:5], sha1password[5:]
    response_api = request_api_data(first_five_char)
    return get_password_leaks_count(response_api, tail)


def main(args):
    count = pwned_api_check(args)
    if count:
        print(f'[!] {args} was found {count} time..... \n[!] you should probably change it...')
    else:
        print('[+] your password is NOT FOUND \n[+] your password is good and secure. carry on')
    system_pause()
    return '[+] Exiting! \n>> Done!'


if __name__ == '__main__':
    logo()
    author()
    try:
        sys.exit(main(input_password()))
    except ConnectionError:
        print('[!] Please make sure if your internet connection is working!')
        os.system('pause')
