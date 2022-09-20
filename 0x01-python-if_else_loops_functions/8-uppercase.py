#!/usr/bin/python3

def uppercase(str):

    for letter in str:

        if ord('a') <= ord(letter) <= ord('z'):

            letter = chr(ord(letter) - (ord('a') - ord('A')))

        print("{:s}".format(letter), end="")
    print("")
