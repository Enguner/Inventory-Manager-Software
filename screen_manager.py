import tkinter as tk
import main_menu_screen as mu_s
import transaction_screen as t_s



class Screen_Manager():

    def __init__(self):
        self._last = None
        self._root = tk.Tk()
        self._root.title("Inventory System")
        self._root.geometry("800x600")
        self._screens = {}
        self._screens["transaction"] = t_s.Transaction_Screen(self._root,self.change_screen)
        self._screens["main_menu"] = mu_s.Main_Menu_Screen(self._root,self.change_screen)


        self.change_screen("main_menu")
        

    def change_screen(self,new_screen,bindings=None,fields=None):
        if self._last is not None:
            self._last.screen.pack_forget()

        if new_screen in self._screens:
            self._screens[new_screen].screen.pack(fill="both", expand=True)
        self._last = self._screens[new_screen]

        if bindings is not None:
            for bind in bindings:
                pass # add binding logic

        if fields is not None:
            for field in fields:
                pass # add field logic

    
    def run(self):
        self._root.mainloop()

menu = Screen_Manager()
menu.run()