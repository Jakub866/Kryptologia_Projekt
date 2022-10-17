

alphabet =''.join(chr(i) for i in range(128))
print(alphabet)


def substit_key(key):
    ending = "".join(x for x in alphabet if x not in key)
    key+=ending
    key = "".join(dict.fromkeys(key))
    return key

def enc_substit(plaintext, key):
    key = substit_key(key)
    permutation = dict(zip(alphabet, key))
    print(permutation)
    result = ""
    for x in plaintext:
        result += permutation[x]
    return result

def dec_substit(cyphertext, key):
    key = substit_key(key)
    permutation_revers = dict(zip(key, alphabet))
    print(permutation_revers)
    result = ""
    for x in cyphertext:
        result += permutation_revers[x]
    return result



key = "juljuszuceazar"

plaintext = "nasz plain text jest przerabiany nacholera wie co"

print(f"{enc_substit(plaintext,key)}  zaszyfrowane")
cyphertext = enc_substit(plaintext,key)

print(dec_substit(cyphertext,key))



