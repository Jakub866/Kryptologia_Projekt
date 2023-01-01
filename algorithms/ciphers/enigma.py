"""
Reflector - A
Rotors - I - II -III
Plugboard - A-R G-k O-K
Message - A => X

import string

alphabet = string.ascii_uppercase
print(alphabet)
"""


class Keyboard:

    def Forward(self, letter):
        signal = "".join((chr(i) for i in range(128))).find(letter)
        return signal

    def backward(self, signal):
        letter = "".join((chr(i) for i in range(128)))[signal]
        return letter


class Plugboard:

    def __init__(self, pairs):
        self.left = "".join((chr(i) for i in range(128)))
        self.right = "".join((chr(i) for i in range(128)))

        for pair in pairs:
            A = pair[0]
            B = pair[1]
            pos_A = self.left.find(A)
            pos_B = self.left.find(B)
            self.left = self.left[:pos_A] + B + self.left[pos_A + 1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B + 1:]

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal


class Rotor:

    def __init__(self, wiring, notch):
        self.left = "".join((chr(i) for i in range(128)))
        self.right = wiring
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def show(self):
        print(self.left)
        print(self.right)
        print("")

    def rotate(self, n=1, forward=True):
        for i in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[127] + self.left[:127]
                self.right = self.right[127] + self.right[:127]

    def rotate_to_letter(self, letter):
        n = "".join((chr(i) for i in range(128))).find(letter)
        self.rotate(n)

    def set_ring(self, n):
        self.rotate(n - 1, False)
        n_notch = "".join((chr(i) for i in range(128))).find(self.notch)
        self.notch = "".join((chr(i) for i in range(128)))[(n_notch - n) % 128]


class Reflector:

    def __init__(self, wiring):
        self.left = "".join((chr(i) for i in range(128)))
        self.right = wiring

    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal


class Enigma:

    def __init__(self, re, r1, r2, r3, pb, kb):
        self.re = re
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.pb = pb
        self.kb = kb

    def set_key(self, key):
        self.r1.rotate_to_letter(key[0])
        self.r2.rotate_to_letter(key[1])
        self.r3.rotate_to_letter(key[2])

    def encipher(self, letter):

        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r2.left[0] == self.r2.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r3.left[0] == self.r3.notch:
            self.r2.rotate()
            self.r3.rotate()
        else:
            self.r3.rotate()

        signal = self.kb.Forward(letter)
        signal = self.pb.forward(signal)
        signal = self.r3.forward(signal)
        signal = self.r2.forward(signal)
        signal = self.r1.forward(signal)
        signal = self.re.reflect(signal)
        signal = self.r1.backward(signal)
        signal = self.r2.backward(signal)
        signal = self.r3.backward(signal)
        signal = self.pb.backward(signal)
        letter = self.kb.backward(signal)
        return letter

    def set_rings(self, rings):
        self.r1.set_ring(rings[0])
        self.r2.set_ring(rings[1])
        self.r3.set_ring(rings[2])


index_key = "".join((chr(i) for i in range(65)))
temp = "".join((chr(i) for i in range(91, 128)))

FirstRotor = index_key + "EKMFLGDQVZNTOWYHXUSPAIBRCJ" + temp
SecondRotor = index_key + "EKMFLGDQVZNTOWYHXUSPAIBRCJ" + temp
ThirdRotor = index_key + "EKMFLGDQVZNTOWYHXUSPAIBRCJ" + temp
FourthRotor = index_key + "EKMFLGDQVZNTOWYHXUSPAIBRCJ" + temp
FifthRotor = index_key + "VZBRGITYUPSDNHLXAWMJQOFECK" + temp

ReflectorA = index_key + "EJMZALYXVBWFCRQUONTSPIKHGD" + temp
ReflectorB = index_key + "YRUHQSLDPXNGOKMIEBFZCWVJAT" + temp
ReflectorC = index_key + "FVPJIAOYEDRZXWGCTKUQSBNMHL" + temp

I = Rotor(FirstRotor, "Q")

II = Rotor(SecondRotor, "E")

III = Rotor(ThirdRotor, "V")

IV = Rotor(FourthRotor, "J")

V = Rotor(FifthRotor, "Z")

A = Reflector(ReflectorA)
B = Reflector(ReflectorB)
C = Reflector(ReflectorC)
KB = Keyboard()
PG = Plugboard(["AZ", "BY", "CX"])

"""
ENIGMA = Enigma(A, III, II, I, PG, KB)

ENIGMA.set_key("MUL")

ENIGMA.set_rings((12, 32, 124))

message = "TEST"
message = message.upper()

cipher_text = ""

for letter in message:
    cipher_text = cipher_text + ENIGMA.encipher(letter)

print(cipher_text)
"""