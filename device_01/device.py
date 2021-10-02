from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

def signature_verifaing():
    file = open("public_key.pem", "rb")
    key = DSA.import_key(file.read())
    file.close()

    file = open("signature", "rb")
    signature = file.read()
    file.close()

    file = open("data.txt", "rb")
    data = file.read()
    file.close()

    hash_obj = SHA256.new(data)
    verifier = DSS.new(key, 'fips-186-3')

    try:
        verifier.verify(hash_obj, signature)
        print('Signature verified.')
    except ValueError:
        print("It's error somewhere.")

signature_verifaing()
