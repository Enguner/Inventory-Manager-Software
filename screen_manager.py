import tkinter as tk
import main_menu_screen
import transaction_screen
import search_items_screen



class Screen_Manager():

    def __init__(self):
        self._last = None
        self._bound = []
        self._root = tk.Tk()
        self._root.title("Inventory System")
        self._root.geometry("800x600")
        self._screens = {}
        self._screens["transaction"] = transaction_screen.Transaction_Screen(self._root,self.change_screen)
        self._screens["main_menu"] = main_menu_screen.Main_Menu_Screen(self._root,self.change_screen)
        self._screens["search"] = search_items_screen.Search_Items_Screen(self._root,self.change_screen)
        self.change_screen("main_menu")
        
    def change_screen(self,new_screen):
        if self._last is not None: # Remove old screen if there is one 
            self._last.screen.pack_forget()

        if len(self._bound)>0: # Remove all old bindings
            for entry in self._bound:
                entry[0].unbind(entry[1])

        if new_screen in self._screens: # New screen logic
            self._screens[new_screen].screen.pack(fill="both", expand=True)
        self._last = self._screens[new_screen]

        if new_screen == "search": 
            entries = self._screens["search"].entries
            for entry in entries: #entry is list item
                widget = entry[0] #entry[0] entry widget
                method = entry[1] #entry[1] method to bind
                binding = entry[2] #entry[2] binding
                widget.bind(binding,method)
                self._bound.append([widget,binding])
            self._screens["search"].clear()
            self._screens["search"].focus()
 
    def run(self):
        self._root.mainloop()
