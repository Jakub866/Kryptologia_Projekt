import base64
import binascii
import string

def enc_ceasar(n, plaintext):

    key = ''.join(chr(i) for i in range(128))
    result =''
    for l in plaintext:
        i =(key.index(l) + n) % 128
        result += key[i]
    return result

def dec_ceasar(n,cyphertext):
    key = ''.join(chr(i) for i in range(128))
    result =''
    for l in cyphertext:
            i = (key.index(l) - n) % 128
            result += key[i]
    return result

def change(n):
    key = ''.join(chr(i) for i in range(128))
    key = [i for i in key]
    result = ""
    for l in n:
        for x in range(len(key)):
            if key[x] == l:
                result += str(x) + ","
    return result








# with open("8.jfif", "rb") as reader:
#     crypted_bytes =[]
#     non_crypted_bytes =[]
#     numbers =[]
#
#     while (byte := reader.read(1)):
#         non_crypted_bytes.append(bytes.hex(byte))
#
#     with open("9.jfif", "w") as writer:
#         for x in non_crypted_bytes:
#
#             numbers.append(change(x))
#
#             crypted_bytes.append(enc_ceasar(42,change(x)))
#             # writer.write(enc_ceasar(42,x))
#
# reader.close()
# writer.close()
#
# print(crypted_bytes)

# for x in range(len(crypted_bytes)):
#     print(f"{crypted_bytes[x]} || {non_crypted_bytes[x]}")

# sending_bytes =[]
# with open("9.jfif", "r") as reader:
#     while (byte := reader.read(2)):
#         print(f"{byte} ||")
#         sending_bytes.append(byte)
# #
#     with open("10.jfif", "wb") as writer:
#         for x in sending_bytes:
#             x = dec_ceasar(42,x)
#             writer.write(binascii.unhexlify(x))



# reader.close()
# writer.close()
