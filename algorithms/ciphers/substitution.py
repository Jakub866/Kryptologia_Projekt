
alphabet =''.join(chr(i) for i in range(128))


def substit_key(key):
    ending = "".join(x for x in alphabet if x not in key)
    key+=ending
    key = "".join(dict.fromkeys(key))
    return key

def enc_substit(key,plaintext):
    key = substit_key(key)
    permutation = dict(zip(alphabet, key))
    result = ""
    for x in plaintext:
        result += permutation[x]
    return result

def dec_substit(key,cyphertext):
    key = substit_key(key)
    permutation_revers = dict(zip(key, alphabet))
    result = ""
    for x in cyphertext:
        result += permutation_revers[x]
    return result






