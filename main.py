import hashlib
import itertools

def bruteforce(passwordHash, hashtype):

    wordlist = "abcdefghijklmnopqrstuvwxyz"
    y=''
    length=7
    wordlistHash=''
    passwordHash=passwordHash

    while wordlistHash != passwordHash:
        for c in itertools.product(wordlist, repeat=length):
            word = y.join(c)+'908042a6ecd0'
            if hashtype == 'sha256':
                wordlistHash = hashlib.sha256(word.encode("utf-8")).hexdigest()
                print(f"Trying password: {word}:{wordlistHash}")
                if wordlistHash == passwordHash:
                    print(f"Found password: {word}")
                    break
            elif hashtype == 'md5':
                wordlistHash = hashlib.md5(word.encode("utf-8")).hexdigest()
                print(f"Trying password: {word}:{wordlistHash}")
                if wordlistHash == passwordHash:
                    print(f"Found password: {word}")
                    break
            elif hashtype == 'sha1':
                wordlistHash = hashlib.sha1(word.encode("utf-8")).hexdigest()
                print(f"Trying password: {word}:{wordlistHash}")
                if wordlistHash == passwordHash:
                    print(f"Found password: {word}")
                    break
            else:
                print("Please either enter a sha256, md5 or sha1 hash and restart the script")
                exit()
        break

bruteforce('1a75a3c4ba3d20ae21d703dd6484642f', 'md5')

