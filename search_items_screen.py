import tkinter as tk
import inventory
import screen

class Search_Items_Screen(screen.Screen):
    def __init__(self,root,screen_changer):
        super().__init__(root,screen_changer)
        tk.Label(self._screen, text="Search Items").pack(pady=10)
        # Create Entry box (no 'text' or 'command' allowed)
        self._search_entry = tk.Entry(self._screen,width=60)
        self._search_entry.pack()
        self._search_results_listbox = tk.Listbox(self._screen,width=45,height=20,font=screen.Screen._fixed_font)
        self._search_results_listbox.pack()
        tk.Button(self._screen, text="Back", command=self.back_button).pack()

    def back_button(self):
        self._screen_changer("main_menu")
 
    def enter_input(self,event):
        entry = self._search_entry.get() # string to return
        inv = inventory.Inventory()
        search_results = inv.search(entry)
        listbox_widget = self.results[0]
        listbox_widget.delete(0,tk.END)
        index = 1 
        listbox_widget.insert(0,f"Item #....Name............Qty.....Slot")
        search_results = screen.Screen.format_results(search_results)
        if len(search_results) != 0:
            for entry in search_results:
                listbox_widget.insert(index,entry)
                index += 1    
            self._search_entry.delete(0,tk.END)  
        else:
            listbox_widget.insert(index,f"")
            listbox_widget.insert(index + 1,f"               No Results Found")

    def clear(self):
        self._search_entry.delete(0,tk.END)
        self._search_results_listbox.delete(0,tk.END)
        
    def focus(self):
        self._search_entry.focus_set()
        
    @property
    def entries(self):
        entries = []
        entries.append([self._search_entry,self.enter_input,"<Return>"])
        return entries

    @property
    def results(self):
        results = []
        results.append(self._search_results_listbox)
        return results