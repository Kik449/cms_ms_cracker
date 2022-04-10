# Script for cracking CMS SIMPLE Passwords
# by s0ck37 [https://github.com/Kik449]

# Import hashlib for hashing, sys for arguments and pwn for logging
import hashlib,sys
from pwn import *

# Credits
log.info("CMS SIMPLE Password Cracker")

# Passing arguments
try:
    to_crack = sys.argv[1]
    wordlist = sys.argv[2]
    sitemask = sys.argv[3]
except:
    log.info(f"Usage: python3 {sys.argv[0]} <hash> <wordlist> <sitemask>")
    exit(0)

# Load wordlist
content = open(wordlist,"rb",).read().decode('utf-8','ignore').split("\n")
total = len(content)

# Initializate variable count, progress and print_prog(only for the logger)
count = 0
print_prog = int(total/159)
progress = log.progress("Cracking")

# Try to crack the password
for i in content:
    if count%print_prog == 0:
        progress.status(f"{count}/{total}")
    if hashlib.md5((sitemask+i.strip()).encode()).hexdigest() == to_crack:
        log.info(f"Cracked: {i}")
        progress.success("Done")
        exit(0)
    count += 1
log.failure("No password matched")
exit(1)
