from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

from kivy.lang import Builder
import os
from kivy.uix.button import Button
from plyer import filechooser
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
import cezar

# #005776 hex of color blue


class FileChoose(Button):
    selection = ListProperty([])

    def __init__(self, **kwargs):
        super(FileChoose,self).__init__(**kwargs)

    def choose(self,*args):
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        return filechooser.open_file()


    def on_selection(self, *a, **k):
        global path
        path = str(self.selection).strip().strip("[").strip("]").strip("'")


    #
    #     # OriginalFile = open(path, "rb")
    #     # while (byte := OriginalFile.read(1)):
    #     #     print(byte)


class WindowManager(ScreenManager):
    pass


class Main_page(Screen):
    Window.size = (800, 900)
    Window.clearcolor = (1, 1, 1, 1)


class Caesar_Page(Screen):
    plaintext = ObjectProperty(None)
    keyphrase = ObjectProperty(None)


    def set(self, *args):
        data = str(FileChoose.choose(FileChoose)).strip().strip("[").strip("]").strip("'")
        self.ids.directory.text = data

    def encrypt(self,keyphrase,plaintext):


        print(f"{keyphrase.text} klucz")
        print(f"{plaintext.text} tekst jawny")
        ciphertext = cezar.enc_ceasar(int(keyphrase.text),plaintext.text)
        self.ids.output.text = ciphertext


class Atbash_Page(Screen):
    pass


class Veginere_Page(Screen):
    pass


class Substitution_Page(Screen):
    pass


class Vernam_Page(Screen):
    pass


kv = Builder.load_file('page.kv')
sm = ScreenManager()
sm.add_widget(Main_page(name='MainPage'))
sm.add_widget(Caesar_Page(name ='cezar'))

class PageApp(App):

    def build(self):
        return sm


if __name__ == "__main__":
    PageApp().run()
