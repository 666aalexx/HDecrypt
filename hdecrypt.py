#!/usr/bin/python3

#Created by 666aalexx

import hashlib; import sys; import argparse; import os;

#Colours
redColour = "\033[31m"
greenColour = "\033[32m"
yellowColour = "\033[33m"
blueColour = "\033[34m"
resetColour = "\033[0m"

parser = argparse.ArgumentParser()
parser.add_argument("-H", "--hash", required=True)
parser.add_argument("-a", "--algorithm", required=True)
parser.add_argument("-w", "--wordlist", required=True)
args = parser.parse_args()

hash_file = args.hash
algorithm = args.algorithm
wordlist = args.wordlist

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
                        os.system("clear")
                        print(f"{greenColour}[+]{resetColour} {word}")
                        sys.exit(0)
                    else:
                        os.system("clear")
                        print(f"{redColour}[X] {resetColour}{word}")
                        pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
