import binascii
import algorithms.ciphers.cezar as cz
import algorithms.ciphers.atbash as atbasz
import algorithms.ciphers.vigenere as vig
import algorithms.ciphers.substitution as sub
import time


index_key = "".join((chr(i) for i in range(128)))

def saving_encrypting(choose_encryption_method: int, src_f: str, src_s:str, key):
    OriginalFile = open(src_f, "rb")
    EncryptedFile = open(src_s, "w")
    while (byte := OriginalFile.read(1)):
        non_crypted_double_bytes = bytes.hex(byte)
        for non_crypted_single_bytes in non_crypted_double_bytes:
            match choose_encryption_method:
                case 1:
                    EncryptedFile.write(str(index_key.index(cz.enc_ceasar(int(key),non_crypted_single_bytes))))
                case 2:
                    EncryptedFile.write(str(index_key.index(atbasz.toAtBash(non_crypted_single_bytes))))
                case 3:
                    EncryptedFile.write((str(index_key.index(vig.encryption(key,non_crypted_single_bytes)))))
                case 4:
                    EncryptedFile.write(str(index_key.index(sub.enc_substit(key,non_crypted_single_bytes))))
                case default:
                    pass
            EncryptedFile.write("\n")
    OriginalFile.close()
    EncryptedFile.close()



def reading_decrypting(choose_encryption_method: int, src_s: str, src_f:str, key: int):
    time.sleep(3)
    EncrypredFile = open(src_s, "r")
    DecryptedFile = open(src_f, "wb")
    wynik = ""
    while (byte := EncrypredFile.readline()):
        byte = byte.strip()
        byte =  index_key[int(byte)]
        match choose_encryption_method:
            case 1:
                byte = cz.dec_ceasar(int(key), byte)
            case 2:
                byte = atbasz.toAtBash(byte)
            case 3:
                byte = vig.decryption(key,byte)
            case 4:
                byte = sub.dec_substit(key,byte)
            case default:
                pass
        wynik = wynik + byte
        if len(wynik) == 2:
            DecryptedFile.write(binascii.unhexlify(wynik))
            wynik = ''
    DecryptedFile.close()
    EncrypredFile.close()

def handle_input_enc(choose_encryption_method: int, inp, key):
    match choose_encryption_method:
        case 1:
            return cz.enc_ceasar(int(key),inp)
        case 2:
            return atbasz.toAtBash(inp)
        case 3:
            return vig.encryption(key,inp)
        case 4:
            return sub.enc_substit(key,inp)
        case default:
            pass

def handle_input_dec(choose_encryption_method: int, inp, key):
    match choose_encryption_method:
        case 1:
            return cz.dec_ceasar(int(key),inp)
        case 2:
            return atbasz.toAtBash(inp)
        case 3:
            return vig.decryption(key,inp)
        case 4:
            return sub.dec_substit(key,inp)
        case default:
            pass
