import screen
import tkinter as tk
import inventory

class Inv_Mgmt_Screen(screen.Screen):
    
    def __init__(self,root,screen_changer):
        super().__init__(root,screen_changer)

        self._inv_entry = tk.Entry(self._screen,width=60)
        self._inv_results_listbox = tk.Listbox(self._screen,width=45,height=20,font=screen.Screen._fixed_font)
        tk.Label(self._screen, text="Inventory Management").pack(pady=10)
        self._inv_entry.pack()
        self._inv_results_listbox.pack()
        button_row = tk.Frame(self._screen)
        button_row.pack(pady=5)

        # Two buttons packed side-by-side within the row
        tk.Button(button_row, text="Add Item",command=self.add_item_button,width=15).pack(side=tk.LEFT, padx=10)
        tk.Button(button_row, text="Modify Item", width=15,command=self.modify_item_button).pack(side=tk.LEFT, padx=10)
        
        # Delete Item button
        tk.Button(button_row, text="Delete Item", command=self.delete_item_button,width=15).pack(side=tk.LEFT, padx=10)
        
        # Return to main menu
        tk.Button(self._screen, text="Back", command=self.back_button).pack()

    @property
    def results(self):
        results = []
        results.append(self._inv_results_listbox)
        return results
    
    @property
    def entries(self):
        results = []
        results.append([self._inv_entry,self.enter_input,"<Return>"])
        return results
    
    def add_item_button(self):
        pass

    def modify_item_button(self):
        pass

    def delete_item_button(self):
        pass

    def enter_input(self,event):
        entry = self._inv_entry.get() # string to return
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
            self._inv_entry.delete(0,tk.END)  
        else:
            listbox_widget.insert(index,f"")
            listbox_widget.insert(index + 1,f"               No Results Found")

    def add_item(self):
        self.add_item_popup()
    
    def add_item_popup(self,item_dict=None):
        pass

        
    

    def back_button(self):
        self._screen_changer("main_menu")

    def focus(self):
        self._inv_entry.focus_set()

    def clear(self):
        self._inv_results_listbox.delete(0,tk.END)
