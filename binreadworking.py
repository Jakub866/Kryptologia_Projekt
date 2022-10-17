import base64
import binascii
import string


def enc_ceasar(n, plaintext):
    key = "".join((chr(i) for i in range(128)))
    result =''
    for l in plaintext:
        i =(key.index(l) + n) % 128
        result += key[i]
    return result

def dec_ceasar(n,cyphertext):
    key = "".join((chr(i) for i in range(128)))
    #print(key)
    result =''
    for l in cyphertext:
            i = (key.index(l) - n) % 128
            result += key[i]
    return result
index_key = "".join((chr(i) for i in range(128)))

with open("Source.jpg", "rb") as reader:
    crypted_bytes =[]
    non_crypted_bytes =[]

    while (byte := reader.read(1)):
        non_crypted_bytes.append(bytes.hex(byte))

    with open("Encrypred.jpg", "w") as writer:
        for x in non_crypted_bytes:
            for z in x:
                #print(index_key.index(enc_ceasar(32,z)))
                writer.write(str(index_key.index(enc_ceasar(32,z))))
                writer.write("\n")


reader.close()
writer.close()


sending_bytes =[]
with open("Encrypred.jpg", "r") as reader:
    while (byte := reader.readline()):
        byte = byte.strip()
        #print(byte)
        # print(f"{byte} ||")
        sending_bytes.append(byte)
    with open("Rsoult.jpg", "wb") as writer:
        wynik = ''
        moze = True
        for x in sending_bytes:
           # print(x, "->", index_key[int(x)], "<-", dec_ceasar(32, index_key[int(x)]))
            x =  index_key[int(x)]
            x = dec_ceasar(32, x)
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
