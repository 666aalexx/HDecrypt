#!/usr/bin/python3

#Created by 666aalexx

import hashlib, sys, argparse
from pwn import *

parser = argparse.ArgumentParser()
parser.add_argument("-H", "--hash", required=True)
parser.add_argument("-a", "--algorithm", required=True)
parser.add_argument("-w", "--wordlist", required=True)
args = parser.parse_args()

hash_file = args.hash
algorithm = args.algorithm
wordlist = args.wordlist

p1 = log.progress("Decrypting hash")
p2 = log.progress("Password")

def main():
    with open(wordlist, "r") as wfile:
        for word in wfile:
            word = word.strip()
            hash_func = getattr(hashlib, algorithm.lower())
            hword = hash_func(word.encode()).hexdigest()
            with open(hash_file, "r") as hfile:
                for hashes in hfile:
                    hashes = hashes.strip()
                    if hword == hashes:
                        p1.success("Completed")
                        p2.success(word)
                        sys.exit(0)
                    else:
                        p2.status(word)
                        pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
