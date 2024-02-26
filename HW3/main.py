
# Homework 3: Encryption and Decryption of a file with openSSL

# Privacy and Censorship.
# Noah Holt

'''
Why developed and security principles used?

This program is for encrypting data to keep it safe. AES-256 is the new and improved standard over the old
DES and time-consuming 3DES. This helps to ensure confidentiality and limits accessibility to those who know the
password (or in this case access to this file).
'''

import subprocess
from random import randbytes


def GetInitVect(size):
    dyslexicRugby = randbytes(size)
    return dyslexicRugby.hex()


def DentalExtraction(file):
    with open(file, "rb+") as f:
        f.seek(16, 2)

        bytes = f.read()

        f.seek(16, 2)
        f.truncate()
        return bytes.hex()


notEncryptedFile = "ThisIsNotATest.txt"
encryptedFile = "ThisIsNotEncrypted"
reversEncryption = "CapturedData.txt"
superSecretPassword = "FartsAreIndeedFunny"

# Initialization Vector Stuff
# Mine is 16 to work, but I think its supposed to be 32 so try both maybe.
number256 = 16 # 256 / 8 = number of bytes per encryption
IVleagueCollege = GetInitVect(number256)

# Please ignore WARNINGS, they are natural
subprocess.run(f"openssl aes-256-cbc -a -in {notEncryptedFile} -out {encryptedFile} -k {superSecretPassword} -iv {IVleagueCollege}", shell=True)
with open(encryptedFile, "ab") as f:
    f.write(bytearray.fromhex(IVleagueCollege))

print("File Is NOW Top Secret")
print("Nobody will every crack this Muahaha")

superObviousIV = DentalExtraction(encryptedFile)
subprocess.run(f"openssl aes-256-cbc -d -a -out {reversEncryption} -in {encryptedFile} -k {superSecretPassword} -iv {superObviousIV}", shell=True)
print("Oh No, someone cracked the Code!")
