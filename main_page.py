import threading

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import mainthread
from kivy.animation import Animation
from kivy.uix.image import Image


from plyer import filechooser
from binread import *

global workThread
global Previous



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
    # remember last opened Page
    def on_enter(self):
        global Previous
        Previous = self.manager.current


    def refresh(self):
        ids_list = [self.ids.loadDirectory,self.ids.saveDirectory,
                    self.ids.keyphrase, self.ids.input, self.ids.output, self.ids.status]
        for i in ids_list:
            i.text = ""

    def status(self,status):
        self.ids.status.text = status


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


    def enc_dec_algorithm(self, keyphrase, plaintext, algorithm, type):
        input_functions = {1:handle_input_dec, 2: handle_input_enc}
        directory_functions ={1:reading_decrypting, 2: saving_encrypting}
        if plaintext.text:
            try:
                plaintext = input_functions[type](algorithm, plaintext.text, keyphrase.text)
                self.ids.output.text = plaintext
                self.status("Completed")
            except:
                self.status("Wrong keyspace. Check Help")

        if self.ids.loadDirectory.text and self.ids.saveDirectory.text:
            try:
                self.status("")
                self.manager.current = "loading"
                global workThread

                workThread = threading.Thread(
                    target=directory_functions[type],
                    args=(algorithm,self.ids.loadDirectory.text,self.ids.saveDirectory.text,keyphrase.text))

                workThread.start()
                self.status("Algorithm done.")
            except:
                self.status("Wrong keyspace. Check Help")

        if self.ids.loadDirectory.text and not self.ids.saveDirectory.text:
            self.status("There is no save directory")

        if not self.ids.loadDirectory.text and self.ids.saveDirectory.text:
            self.status("There is no load directory")
        if keyphrase and not self.ids.loadDirectory.text and not self.ids.input.text:
            self.status("Wrong input")





class Main_page(Screen):
    Window.size = (800, 950)
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

class Loading_Page(Screen):
    local = ""

    def animationThread(self):
        # Initiate the animation
        anim= Animation(pos_hint = {"center_x":0.1}, duration= 1.5)
        anim+= Animation(pos_hint = {"center_x":0.9}, duration = 1.5)
        anim.repeat = True
        anim.start(self.loading_image)

        # Waiting for the end of the Enc/Dec thread
        while workThread.is_alive():
            time.sleep(3)
            print(workThread.is_alive())
        anim.stop(self.loading_image)
        self.edit()


    def on_enter(self):
        # init loading labels
        self.loading_label = Label(text="Loading...",
                                   size_hint=(1, 0.1),
                                   font_size=50,
                                   pos_hint={"center_x": 0.5},
                                   )
        self.loading_image = Image(source="images//pad.png",
                                   size_hint=(.2, .2),
                                   pos_hint={"center_x": 0.9},
                                   )

        self.ids.loadingLayout.add_widget(self.loading_label)
        self.ids.loadingLayout.add_widget(self.loading_image)

        Loading_Thread = threading.Thread(target=self.animationThread, daemon=True)
        Loading_Thread.start()

    @mainthread
    def get_back(self, *args):
        # delete response label
        self.ids.loadingLayout.remove_widget(self.response_label)
        self.ids.loadingLayout.remove_widget(self.response_button)

        self.manager.current = Previous


    @mainthread
    def edit(self):
        # Deleting old widgets
        self.ids.loadingLayout.remove_widget(self.loading_label)
        self.ids.loadingLayout.remove_widget(self.loading_image)
        # Init of response
        self.response_button = Button(text="Finish",
                                 size_hint=(1,.2),
                                 font_size = 25,
                             )
        self.response_label = Label(text="Algorithm was succesfully completed",
                               font_size = 50,
                               text_size= (self.width,None),
                               halign = 'center',
                               valign = 'center',
                               )
        # Add new response to Loading Page
        self.ids.loadingLayout.add_widget(self.response_label)
        self.ids.loadingLayout.add_widget(self.response_button)
        self.response_button.bind(on_press=self.get_back)



kv = Builder.load_file('kivy_files\\page.kv')
sm = ScreenManager()
sm.add_widget(Main_page(name='main'))
sm.add_widget(Caesar_Page(name ='cezar'))
sm.add_widget(Atbash_Page(name ='atbash'))
sm.add_widget(Vigenere_Page(name ='vigenere'))
sm.add_widget(Substitution_Page(name ="substit"))
sm.add_widget(Loading_Page(name="loading"))

class PageApp(App):

    def build(self):
        return sm


if __name__ == "__main__":
    PageApp().run()

