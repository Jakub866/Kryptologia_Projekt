def enc_ceasar(n, plaintext: str):
    key = ''.join(chr(i) for i in range(128))
    result =''
    for l in plaintext:
        i =(key.index(l) + n)  % 128
        result += key[i]
    return result

def dec_ceasar(n: int,cyphertext: str):
    key = ''.join(chr(i) for i in range(128))
    result =''
    for l in cyphertext:
            i = (key.index(l) - n) % 128
            result += key[i]
    return result