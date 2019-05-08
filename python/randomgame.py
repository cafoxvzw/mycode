#!/usr/bin/python3

import requests

MYAPI = r"https://www.random.org/integers/?num=1&min=0&max=1&col=1&base=10&format=plain&rnd=new"

def main():
    result = requests.get(MYAPI)
    if "1" in result.text: # if the value of 1 is in the result.txt
        print("You won!")
    else:
        print("You lost!")

main()

