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


def encryption(key, plaintext):
    key = key_vigenere(key)
    ciphertext = enc_vigenere(plaintext, key)
    return ciphertext

def decryption(key,ciphertext):
    key = key_vigenere(key)
    plaintext = dec_vigenere(ciphertext,key)
    return plaintext



