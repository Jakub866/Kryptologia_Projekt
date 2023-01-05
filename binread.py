import binascii
import algorithms.ciphers.cezar as cz
import algorithms.ciphers.atbash as atbasz
import algorithms.ciphers.vigenere as vig
import algorithms.ciphers.substitution as sub
import algorithms.ciphers.enigma as en
import time

index_key = "".join((chr(i) for i in range(128)))

def enigma_dec_enc(LRotor: int, MRotor: int, RRotor: int, PlugBoard: list, key_set: str,
                   ring_list: tuple, InOtTx: str):
    global CLRotor, CMRotor, CRRotor, CReflector
    match LRotor:
        case 1:
            CLRotor = en.Rotor(en.SRotorA, "Q")
        case 2:
            CLRotor = en.Rotor(en.SRotorB, "E")
        case 3:
            CLRotor = en.Rotor(en.SRotorC, "V")
        case 4:
            CLRotor = en.Rotor(en.SRotorE, "J")
        case 5:
            CLRotor = en.Rotor(en.SRotorF, "Z")

    match MRotor:
        case 1:
            CMRotor = en.Rotor(en.SRotorA, "Q")
        case 2:
            CMRotor = en.Rotor(en.SRotorB, "E")
        case 3:
            CMRotor = en.Rotor(en.SRotorC, "V")
        case 4:
            CMRotor = en.Rotor(en.SRotorE, "J")
        case 5:
            CMRotor = en.Rotor(en.SRotorF, "Z")

    match RRotor:
        case 1:
            CRRotor = en.Rotor(en.SRotorA, "Q")
        case 2:
            CRRotor = en.Rotor(en.SRotorB, "E")
        case 3:
            CRRotor = en.Rotor(en.SRotorC, "V")
        case 4:
            CRRotor = en.Rotor(en.SRotorE, "J")
        case 5:
            CRRotor = en.Rotor(en.SRotorF, "Z")

    CReflector = en.Reflector(en.SReflector)

    PG = en.Plugboard(PlugBoard)

    ENIGMA = en.Enigma(CReflector, CLRotor, CMRotor, CRRotor, PG, en.KB)
    ENIGMA.set_key(key_set)
    ENIGMA.set_rings(ring_list)

    output = ""

    for letter in InOtTx:
        output = output + ENIGMA.encipher(letter)

    return output


def saving_encrypting(choose_encryption_method: int, src_f: str, src_s: str, key):
    OriginalFile = open(src_f, "rb")
    EncryptedFile = open(src_s, "w")
    while (byte := OriginalFile.read(1)):
        non_crypted_double_bytes = bytes.hex(byte)
        for non_crypted_single_bytes in non_crypted_double_bytes:
            match choose_encryption_method:
                case 1:
                    EncryptedFile.write(str(index_key.index(cz.enc_ceasar(int(key), non_crypted_single_bytes))))
                case 2:
                    EncryptedFile.write(str(index_key.index(atbasz.toAtBash(non_crypted_single_bytes))))
                case 3:
                    EncryptedFile.write((str(index_key.index(vig.encryption(key, non_crypted_single_bytes)))))
                case 4:
                    EncryptedFile.write(str(index_key.index(sub.enc_substit(key, non_crypted_single_bytes))))
                case 5:
                    EncryptedFile.write(str(index_key.index(
                        enigma_dec_enc(key[0], key[1], key[2], key[3],
                                      key[4], key[5],
                                       non_crypted_single_bytes))))  # Przykład enigma_key = [1, 5, 4, 3, ["AB", "BC", "CD"], "MUL", (12, 32, 124)]
                case default:
                    pass
            EncryptedFile.write("\n")
    OriginalFile.close()
    EncryptedFile.close()


def reading_decrypting(choose_encryption_method: int, src_s: str, src_f: str, key):
    time.sleep(3)
    EncrypredFile = open(src_s, "r")
    DecryptedFile = open(src_f, "wb")
    wynik = ""
    while (byte := EncrypredFile.readline()):
        byte = byte.strip()
        byte = index_key[int(byte)]
        match choose_encryption_method:
            case 1:
                byte = cz.dec_ceasar(int(key), byte)
            case 2:
                byte = atbasz.toAtBash(byte)
            case 3:
                byte = vig.decryption(key, byte)
            case 4:
                byte = sub.dec_substit(key, byte)
            case 5:

                byte = enigma_dec_enc(key[0], key[1], key[2], key[3],
                                      key[4], key[5],
                                      byte)
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
            return cz.enc_ceasar(int(key), inp)
        case 2:
            return atbasz.toAtBash(inp)
        case 3:
            return vig.encryption(key, inp)
        case 4:
            return sub.enc_substit(key, inp)
        case 5:
            return enigma_dec_enc(key[0], key[1],key[2], key[3],
                                  key[4], key[5],
                                  inp)
        case default:
            pass


def handle_input_dec(choose_encryption_method: int, inp, key):
    match choose_encryption_method:
        case 1:
            return cz.dec_ceasar(int(key), inp)
        case 2:
            return atbasz.toAtBash(inp)
        case 3:
            return vig.decryption(key, inp)
        case 4:
            return sub.dec_substit(key, inp)
        case 5:
            return enigma_dec_enc(key[0], key[1], key[2], key[3],
                                  key[4], key[5],
                                  inp)
        case default:
            pass

# Przykład enigma_key = [5, 4, 3, ["AB", "BC", "CD"], "MUL", (12, 32, 124)]
#saving_encrypting(5, "README.md", "ENREADME.MD", None, [3, 2, 1, ["AR", "XO", "EW"], "123", (2, 4, 59)])
#reading_decrypting(5, "ENREADME.MD", "CHECK.MD", None, [3, 2, 1, ["AR", "XO", "EW"], "123", (2, 4, 59)])

#Pierwsze 3 liczby to wybór rotora od lewej do prawej możliwy wybór: 1-5
#Kolejnym jest lista dwóch znaków oznaczająca pluggboarda, tj jaka z liter zamieniana jest z jaką.
#3 literowy string to wybór od jakich liter/znaków zaczynają się rotory.
#Krotka zawierająca 3 liczby to numer który odpowiada za to w którym momencie rotor zostanie poruszony w kolejną pozycję dodaję dużą ilość złożności.
#UWAGA nie ma możliwości wyboru reflektora. jest tylko jeden.
