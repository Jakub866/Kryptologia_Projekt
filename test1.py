import numpy as np
import binascii
import collections
counter = 0
import matplotlib.pyplot as plt

class Histogram():
    def __init__(self,plain,cipher):
        self.plain = plain
        self.cipher = cipher
        self.cipherArray = self.load_text(cipher)
        self.plainArray = self.load_binary(plain)



    def load_binary(self,file):
        arrayFile = np.fromfile(file, dtype="uint8")
        arrayFile =np.array([hex(x) for x in arrayFile])

        print(arrayFile)
        return arrayFile

    def load_text(self,file):
        arrayFile = np.genfromtxt(file,dtype='uint8')
        test = np.genfromtxt(file,dtype="str")

        print(arrayFile)
        print(test)

        return arrayFile

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

        print(self.plainArray)
        print(len(self.cipherArray))

        print(counter_one)
        print(counter_second)

        """dane wymagane"""
        x_bar = [x for x in range(128)]
        first_data = [counter_one[_] for _ in range(len(counter_one))]
        second_data = [counter_second[_] for _ in range(len(counter_second))]

        print(first_data)
        print(second_data)

        # f = plt.figure(figsize=(20,8))
        #
        #
        # f.add_subplot(211)
        # plt.title("Encrypted data")
        # plt.bar(x_bar,first_data,width=0.7)
        # plt.xticks(x_bar)
        # plt.xticks(rotation=90)
        # plt.tight_layout()
        # plt.margins(x=0)
        #
        # f.add_subplot(212)
        # plt.title("Plain data")
        # plt.bar(x_bar,second_data,width=0.7)
        # plt.xticks(x_bar)
        # plt.xticks(rotation=90)
        # plt.tight_layout()
        # plt.margins(x=0)
        #
        #
        # return plt.gcf()

index_key = "".join((chr(i) for i in range(128)))
print(index_key[105])




