#!/usr/bin/python3

for let in range(ord('z'), ord('a') - 1, -1):

        print("{:s}".format((chr(let - 32) if let % 2 != 0 else chr(let))), end="")
