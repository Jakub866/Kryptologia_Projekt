
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



