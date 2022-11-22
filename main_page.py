from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from plyer import filechooser
from kivy.properties import ListProperty

import algorithms.ciphers.cezar as cezar
import algorithms.ciphers.atbash as atbash
import algorithms.ciphers.vigenere as vigenere
import algorithms.ciphers.substitution as substitution

# #005776 hex of color blue


class FileChoose(Button):
    selection = ListProperty([])

    def __init__(self, **kwargs):
        super(FileChoose,self).__init__(**kwargs)

    def choose(self,*args):
        return filechooser.open_file()


    def on_selection(self, *a, **k):
        global path
        path = str(self.selection).strip().strip("[").strip("]").strip("'")


class WindowManager(ScreenManager):
    pass


class Main_page(Screen):
    Window.size = (800, 900)
    Window.clearcolor = (1, 1, 1, 1)


class Caesar_Page(Screen):
    def refresh(self):
        self.ids.directory.text = ""
        self.ids.keyphrase.text = "Place for a key"
        self.ids.output.text = "Encrypted/Decrypted file"
        self.ids.plaintext.text = "Place holder for file"
        self.ids.status.text = ""


    def set(self, *args):
        data = str(FileChoose.choose(FileChoose)).strip().strip("[").strip("]").strip("'")
        self.ids.directory.text = data

    def encrypt(self,keyphrase,plaintext):
        try:
            ciphertext = cezar.enc_ceasar(int(keyphrase.text),plaintext.text)
            self.ids.output.text = ciphertext
            Caesar_Page.status(self, "Encryption done.")
        except:
            Caesar_Page.status(self, "Key must be a number between 1-26!")
            return None

    def decrypt(self, keyphrase, plaintext):

        try:
            deciphertext = cezar.dec_ceasar(int(keyphrase.text),plaintext.text)
            self.ids.output.text = deciphertext
            Caesar_Page.status(self, "Decryption done.")
        except:
            Caesar_Page.status(self, "Key must be a number between 1-26!")
            return None

    def status(self,status):
        self.ids.status.text = status

class Atbash_Page(Screen):

    def refresh(self):
        self.ids.directory.text = ""
        self.ids.output.text = "Encrypted/Decrypted file"
        self.ids.plaintext.text = "Place holder for file"
        self.ids.status.text = ""

    def set(self, *args):
        data = str(FileChoose.choose(FileChoose)).strip().strip("[").strip("]").strip("'")
        self.ids.directory.text = data

    def encrypt(self,plaintext):
        try:
            ciphertext = atbash.toAtBash(plaintext.text)
            self.ids.output.text = ciphertext
            Atbash_Page.status(self, "Algorithm done.")
        except:
            Atbash_Page.status(self, "Something gone wrong")
            return None

    def status(self,status):
        self.ids.status.text = status



class Vigenere_Page(Screen):
    def refresh(self):
        self.ids.directory.text = ""
        self.ids.keyphrase.text = "Place for a key"
        self.ids.output.text = "Encrypted/Decrypted file"
        self.ids.plaintext.text = "Place holder for file"
        self.ids.status.text = ""

    def set(self, *args):
        data = str(FileChoose.choose(FileChoose)).strip().strip("[").strip("]").strip("'")
        self.ids.directory.text = data

    def encrypt(self, keyphrase, plaintext):
        try:
            ciphertext = vigenere.encryption(keyphrase.text, plaintext.text)
            self.ids.output.text = ciphertext
            Vigenere_Page.status(self, "Encryption done.")
        except:
            Vigenere_Page.status(self, "Something gone wrong.")


    def decrypt(self, keyphrase, plaintext):
        try:
            deciphertext = vigenere.decryption(keyphrase.text, plaintext.text)
            self.ids.output.text = deciphertext
            Vigenere_Page.status(self, "Decryption done.")
        except:
            Vigenere_Page.status(self, "Something gone wrong.")

    def status(self,status):
        self.ids.status.text = status

class Substitution_Page(Screen):
    def refresh(self):
        self.ids.directory.text = ""
        self.ids.keyphrase.text = "Place for a key"
        self.ids.output.text = "Encrypted/Decrypted file"
        self.ids.plaintext.text = "Place holder for file"
        self.ids.status.text = ""

    def set(self, *args):
        data = str(FileChoose.choose(FileChoose)).strip().strip("[").strip("]").strip("'")
        self.ids.directory.text = data

    def encrypt(self, keyphrase, plaintext):
        try:
            ciphertext = substitution.enc_substit(keyphrase.text, plaintext.text)
            self.ids.output.text = ciphertext
            Substitution_Page.status(self, "Encryption done.")
        except:
            Substitution_Page.status(self, "Something gone wrong.")

    def decrypt(self, keyphrase, plaintext):
        try:
            deciphertext = substitution.dec_substit(keyphrase.text, plaintext.text)
            self.ids.output.text = deciphertext
            Substitution_Page.status(self, "Decryption done.")
        except:
            Substitution_Page.status(self, "Something gone wrong.")


    def status(self,status):
        self.ids.status.text = status
class Vernam_Page(Screen):
    pass


kv = Builder.load_file('kivy_files\\page.kv')
sm = ScreenManager()
sm.add_widget(Main_page(name='main'))
sm.add_widget(Caesar_Page(name ='cezar'))
sm.add_widget(Atbash_Page(name ='atbash'))
sm.add_widget(Vigenere_Page(name ='vigenere'))
sm.add_widget(Substitution_Page(name ="substit"))
class PageApp(App):

    def build(self):
        return sm


if __name__ == "__main__":
    PageApp().run()
