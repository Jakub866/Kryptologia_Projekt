from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty


class Main_page(Screen, ScrollView):
    Window.size = (800, 900)
    plaintext =ObjectProperty(None)
    keyphrase = ObjectProperty(None)
    algorithm = ObjectProperty(None)

    # Pod koncowy produkt
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)




class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)



class Second_page(Screen):
    plaintext = ObjectProperty(None)
    keyphrase = ObjectProperty(None)
    algorithm = ObjectProperty(None)

    # Pod koncowy produkt
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def press(self):
        plaintext = self.plaintext.text
        keyphrase = self.keyphrase.text
        algorithm = self.algorithm.text

        print(f" tekst jawny {plaintext} haslo {keyphrase} algorytm {algorithm}")

        self.plaintext.text = ""
        self.keyphrase.text = ""
        self.algorithm.text = ""

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    # ---==== Wyswietlenie lokalizacji pliku === -----
    def load(self, path, filename):
        self.text_input.text = str(filename).strip("[]").strip("'")

        self.dismiss_popup()








class PageApp(App):
    def build(self):
        screenmanager =ScreenManager()
        screenmanager.add_widget(Main_page(name ="MainPage"))
        screenmanager.add_widget(Second_page(name="SecondPage"))
        return screenmanager


if __name__ == "__main__":
    PageApp().run()