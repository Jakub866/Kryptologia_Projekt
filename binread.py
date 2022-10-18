import binascii
import atbasz
import cezar as cz


index_key = "".join((chr(i) for i in range(128)))

def saving_encrypting(choose_encryption_method: int, src_f: str):
    ces_shift = ""
    OriginalFile = open(src_f, "rb")
    EncryptedFile = open("Encrypted_" + src_f, "w")
    while (byte := OriginalFile.read(1)):
        non_crypted_double_bytes = bytes.hex(byte)
        for non_crypted_single_bytes in non_crypted_double_bytes:
            match choose_encryption_method:
                case 1:
                    if ces_shift == "":
                        print("Przesunięcie: ", end='')
                        ces_shift = int(input())
                    EncryptedFile.write(str(index_key.index(cz.enc_ceasar(ces_shift,non_crypted_single_bytes))))
                case 2:         
                    EncryptedFile.write(str(index_key.index(atbasz.toAtBash(non_crypted_single_bytes))))                
                case default:
                    print("Encryption method not found")
                    quit()
            EncryptedFile.write("\n")
    OriginalFile.close()
    EncryptedFile.close()

def reading_decrypting(choose_encryption_method: int, src_f: str):
    EncrypredFile = open("Encrypted_" + src_f, "r")
    DecryptedFile = open("Decrypted_" + src_f, "wb")
    ces_shift = ""
    wynik = ''
    while (byte := EncrypredFile.readline()):
        byte = byte.strip()
        byte =  index_key[int(byte)]
        match choose_encryption_method:
                case 1:
                    if ces_shift == "":
                        print("Przesunięcie: ", end='')
                        ces_shift = int(input())
                    byte = cz.dec_ceasar(32, byte)
                case 2:         
                    byte = atbasz.toAtBash(byte)                
                case default:
                    print("Encryption method not found")
                    quit()
        wynik = wynik + byte
        if len(wynik) == 2:
            DecryptedFile.write(binascii.unhexlify(wynik))
            wynik = ''
    DecryptedFile.close()
    EncrypredFile.close()

saving_encrypting(1, "Source.jpg")
reading_decrypting(1, "Source.jpg")