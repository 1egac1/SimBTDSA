import shutil
import os
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

#print(os.listdir())

def connecting(chdevice):
    src = "keys/public_key.pem"
    dst = chdevice+"/public_key.pem"
    shutil.copyfile(src, dst)

    data = b"its me"
    hash_obj = SHA256.new(data)
    f = open("keys/privat_key.pem", "rb")
    key = DSA.import_key(f.read())
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    f.close()

    file = open(chdevice+"/data.txt", "wb")
    file.write(data)
    file.close()

    file = open(chdevice+"/signature", "wb")
    file.write(signature)
    file.close()
    
    return 0


def dsa_keys_creation():
    key = DSA.generate(1024)
    f = open("keys/public_key.pem", "wb")
    f.write(key.publickey().export_key())
    f = open("keys/privat_key.pem", "wb")
    f.write(key.export_key())
    f.close()
    return

def assimilation():
    files = os.listdir()
    bool_check = False

    for i in files:
        if i == "keys/privat_key.pem":
            bool_check = True

    if bool_check:  
        return
    else:
        dsa_keys_creation()
        return


def main():
    assimilation()
    
    device2connect = input()
    
    connecting(device2connect)
    
    dsa_certificate()



main()
