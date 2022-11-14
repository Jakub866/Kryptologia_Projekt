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
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.lang import Builder



from kivy.properties import StringProperty

# #005776 hex of color blue

class Main_page(Screen):
    Builder.load_file('page.kv')
    Window.size = (800, 900)
    Window.clearcolor = (1,1,1,1)



class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)



class Caesar_Page(Screen):

    Builder.load_file("ceasar.kv")
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



class Atbash_Page(Screen):
    Builder.load_file("atbash.kv")
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


class Veginere_Page(Screen):
    Builder.load_file("veginere.kv")
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

class Substitution_Page(Screen):
    Builder.load_file("substitution.kv")
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

class Vernam_Page(Screen):
    Builder.load_file("vernam.kv")
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
        screenmanager.add_widget(Caesar_Page(name="CaesarPage"))
        screenmanager.add_widget(Atbash_Page(name="AtbashPage"))

        screenmanager.add_widget(Veginere_Page(name="VeginerePage"))
        screenmanager.add_widget(Substitution_Page(name="SubstitutionPage"))
        screenmanager.add_widget(Vernam_Page(name="VernamPage"))
        return screenmanager


if __name__ == "__main__":
    PageApp().run()