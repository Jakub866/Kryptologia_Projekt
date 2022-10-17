def key_vigenere(key):
    keyArray =[]
    for i in range(0, len(key)):
        keyElement = ord(key[i])
        keyArray.append(keyElement)
    return keyArray

def shiftEnc(plainletter, shift_number):
    return chr(((ord(plainletter) + shift_number) % 128))


def enc_vigenere(plaintext, key):
    secret = "".join(shiftEnc(plaintext[i], key[i % len(key)]) for i in range(len(plaintext)))
    return secret


def shiftDec(plainletter, shift_number):
    return chr(((ord(plainletter) - shift_number) % 128))


def dec_vigenere(cyphertext, key):
    secret = "".join(shiftDec(cyphertext[i], key[i % len(key)]) for i in range(len(cyphertext)))
    return secret

key2generate = "Test"
key = key_vigenere(key2generate)
plaintext = "test"
ciphertext = enc_vigenere(plaintext,key)
print(ciphertext)


decrypt = dec_vigenere(ciphertext,key)

print(decrypt)


