import numpy as np
import binascii
import collections
counter = 0
import matplotlib.pyplot as plt

class Histogram():
    def __init__(self, load, save, type):
        self.plain = load
        self.cipher = save
        match type:
            case 1:
                self.cipherArray = self.load_text(load)
                self.plainArray = self.load_binary(save)
            case 2:
                self.cipherArray = self.load_text(save)
                self.plainArray = self.load_binary(load)



    def load_binary(self,file):
        arrayFile = np.fromfile(file, dtype="uint8")
        arrayFile =np.array([hex(x) for x in arrayFile])

        arrayFile = []
        OriginalFile = open(file, "rb")
        while (byte := OriginalFile.read(1)):
            non_crypted_double_bytes = bytes.hex(byte)
            # print(non_crypted_double_bytes)
            for non_crypted_single_bytes in non_crypted_double_bytes:
                arrayFile.append(ord(non_crypted_single_bytes))

        return arrayFile

    def load_text(self,file):
        test = np.genfromtxt(file,dtype="int")
        # test = []
        # EncrypredFile = open(file, "r")
        # while (byte := EncrypredFile.readline()):
        #     byte = byte.strip()
        #     test.append((int(byte)))
        return test

    def visualization(self):

        """tworzymy puste zbiory po 128 elementow"""
        index = list(_ for _ in range(128))
        zeroes = list(0 for _ in range(128))
        init_dict = dict(zip(index, zeroes))

        """Tworzymy licznik z 128 elementami"""
        counter_one = collections.Counter(init_dict)
        counter_second = collections.Counter(init_dict)



        """Uzupelniamy licznik naszymi danymi"""
        counter_one.update(self.plainArray)
        counter_second.update(self.cipherArray)

        f = plt.figure(figsize=(20,6))
        first_key = [_ for _ in counter_one.keys()]
        second_key = [_ for _ in counter_second.keys()]
        first_data = [_ for _ in counter_one.values()]
        second_data =[_ for _ in counter_second.values()]
        f.add_subplot(211)
        plt.title("Plain data")
        plt.bar(first_key,first_data,width=0.7)

        plt.xticks(rotation=90)
        # #
        f.add_subplot(212)
        plt.title("Encrypted data")
        plt.bar(second_key,second_data,width=0.7)

        plt.xticks(rotation=90)
        plt.subplots_adjust(hspace=.3)


        return plt.gcf()






