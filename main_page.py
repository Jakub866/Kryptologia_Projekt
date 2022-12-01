from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from plyer import filechooser
import binread
from kivy.animation import Animation
from kivy.clock import Clock, mainthread
# #005776 hex of color blue


class FileChoose(Button):
    def __init__(self, **kwargs):
        super(FileChoose,self).__init__(**kwargs)

    def choose(self,*args):
        return filechooser.open_file()

    def save(self,*args):
        return filechooser.save_file()



class WindowManager(ScreenManager):
    pass


class Page(Screen):

    def fade(self,dt):
        anim = Animation(opacity=0, duration=2)
        anim.start(self.ids.status)



    def status(self,status):
        self.ids.status.opacity = 1
        self.ids.status.text = status
        Clock.schedule_once(self.fade,10)


    def refresh(self):
        ids_list = [self.ids.loadDirectory,self.ids.saveDirectory,
                    self.ids.keyphrase, self.ids.input, self.ids.output, self.ids.status]
        for i in ids_list:
            i.text = " "

    def set_load(self):
        try:
            path_load = str(FileChoose.choose(FileChoose))
            self.ids.loadDirectory.text = path_load[2:len(path_load)-2]
            self.status("File loaded.")

        except:
            self.status("Wrong directory")

    def set_save(self):
        try:
            path_save = str(FileChoose.save(FileChoose))
            self.ids.saveDirectory.text = path_save[2:len(path_save)-2]

            self.status("Saving directory loaded.")
        except:
            self.status("Error when choosing a path to save")

    def encrypt(self,keyphrase,plaintext,enc):

            if plaintext.text:
                try:
                    ciphertext = binread.handle_input_enc(enc, plaintext.text, keyphrase.text)
                    self.ids.output.text = ciphertext
                except:
                    self.status("Wrong input or keyspace. Check Help")

            if self.ids.loadDirectory.text:
                try:
                    fileEncrypt = binread.saving_encrypting(enc,self.ids.loadDirectory.text, self.ids.saveDirectory.text,
                                                    keyphrase.text)
                    self.status("Encryption done.")
                except:
                    self.status("Wrong input or keyspace. Check Help")



    def decrypt(self, keyphrase, plaintext,enc):

        if plaintext.text:
            try:
                plaintext = binread.handle_input_dec(enc,plaintext.text,keyphrase.text)
                self.ids.output.text = plaintext
            except:
                self.status("Wrong input or keyspace. Check Help")


        if self.ids.loadDirectory.text:
            try:
                fileDecrypt = binread.reading_decrypting(enc,self.ids.loadDirectory.text, self.ids.saveDirectory.text,
                                                    keyphrase.text)
                self.status("Decryption done.")
            except:
                self.status("Wrong input or keyspace. Check Help")


class Main_page(Screen):
    Window.size = (800, 900)
    Window.clearcolor = (1, 1, 1, 1)

class Atbash_Page(Page):
    pass

class Vigenere_Page(Page):
    pass

class Caesar_Page(Page):
    pass

class Substitution_Page(Page):
    pass

class Vernam_Page(Page):
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
