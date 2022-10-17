import binascii
import atbasz
import cezar as cz


def saving_encrypting(choose_encryption_method: int, src_f: str):
    index_key = "".join((chr(i) for i in range(128)))
    ces_shift = "t"
    OriginalFile = open(src_f, "rb")
    EncryptedFile = open("Encrypted_" + src_f, "w")
    while (byte := OriginalFile.read(1)):
        non_crypted_double_bytes = bytes.hex(byte)
        for non_crypted_single_bytes in non_crypted_double_bytes:
            match choose_encryption_method:
                case 1:
                    if ces_shift == "t":
                        print("Przesunięcie: ", end='')
                        ces_shift = int(input())
                    EncryptedFile.write(str(index_key.index(cz.enc_ceasar(ces_shift,non_crypted_single_bytes))))
                case 2:                            
                    EncryptedFile.write(str(index_key.index(atbasz.toAtBash(non_crypted_single_bytes))))
                case default:
                    print("Encryption method not found")
                    quit()
            #print(index_key.index(enc_ceasar(32,z)))
            
            #writer.write(str(index_key.index(atbasz.toAtBash(z))))
            EncryptedFile.write("\n")
    OriginalFile.close()
    EncryptedFile.close()

saving_encrypting(2, "Source.jpg")
sending_bytes =[]
with open("Encrypred_" + "Source.jpg", "r") as reader:
    while (byte := reader.readline()):
        byte = byte.strip()
        #print(byte)
        # print(f"{byte} ||")
        sending_bytes.append(byte)
    with open("Rsoult.jpg", "wb") as writer:
        wynik = ''
        moze = True
        for x in sending_bytes:
            #print(x, "->", index_key[int(x)], "<-", dec_ceasar(32, index_key[int(x)]))
            x =  index_key[int(x)]
            #x = cz.dec_ceasar(32, x)
            x = atbasz.toAtBash(x)
            #print(x)
            if moze:
                wynik = wynik + x
                if len(wynik) == 2:
                    writer.write(binascii.unhexlify(wynik))
                    wynik = ''

            #x = dec_ceasar(32, index_key[int(x)])
            #print(x)
            #x = index_key[int(dec_ceasar(32,x))]
            
            



reader.close()
writer.close()