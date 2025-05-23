import inventory
import tkinter as tk
import tkinter.font as tkFont

class Menu:
    """ Initializing """
    def __init__(self):
        """
        Attributes:
            -self._root
            -self._main_menu_screen
            -self._search_items_screen
            -self._search_entry

        Methods:
            - TBD

        """
        self._inventory = inventory.Inventory()
        self._root = tk.Tk()
        self._root.title("Inventory System")
        self._root.geometry("800x600")
        fixed_font = tkFont.Font(family="Courier New", size=10)

        # Create two screens (frames)
        self._main_menu_screen = tk.Frame(self._root)
        self._search_items_screen = tk.Frame(self._root)
        self._inv_management_screen = tk.Frame(self._root)
        self._transaction = tk.Frame(self._root)

        self._last = self._main_menu_screen 

        
        """Main Menu"""

        # Set up main menu ````````````````````````````````````````````````````

        tk.Label(self._main_menu_screen, text="Inventory System").pack(pady=30)
 
        button = tk.Button(self._main_menu_screen, text="Search Items", command=self.show_search_items_screen,width=20,height=2)
        button.pack(pady=10)

        button = tk.Button(self._main_menu_screen, text="Inv. Management", command=self.show_inv_management_screen,width=20,height=2)
        button.pack(pady=10)

        button = tk.Button(self._main_menu_screen, text="Transaction", command=self.show_search_items_screen,width=20,height=2)
        button.pack(pady=10)

        button = tk.Button(self._main_menu_screen, text="Logs", command=self.show_search_items_screen,width=20,height=2)
        button.pack(pady=10)

        button = tk.Button(self._main_menu_screen, text="User Setup", command=self.show_search_items_screen,width=20,height=2)
        button.pack(pady=10)
        
        # End of main menu Setup ``````````````````````````````````````````````
        

        """Search Screen"""


        # Set up Search Screen ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        tk.Label(self._search_items_screen, text="Search Items").pack(pady=10)
        # Create Entry box (no 'text' or 'command' allowed)
        self._search_entry = tk.Entry(self._search_items_screen,width=60)
        self._search_entry.pack()
        self._results_listbox = tk.Listbox(self._search_items_screen,width=45,height=20,font=fixed_font)
        self._results_listbox.pack()
        tk.Button(self._search_items_screen, text="Back", command=self.show_main_menu_screen).pack()

        # End of Search Screen Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


        """Inv. Management Screen"""

        # Set up Inv. Management Screen ````````````````````````````````````````
        self._search_entry = tk.Entry(self._inv_management_screen,width=60)
        self._results_listbox = tk.Listbox(self._inv_management_screen,width=45,height=20,font=fixed_font)
        tk.Label(self._inv_management_screen, text="Inventory Management").pack(pady=10)
        self._search_entry.pack()
        self._results_listbox.pack()
        button_row = tk.Frame(self._inv_management_screen)
        button_row.pack(pady=5)

        # Two buttons packed side-by-side within the row
        tk.Button(button_row, text="Add Item", width=15).pack(side=tk.LEFT, padx=10)
        tk.Button(button_row, text="Modify Item", width=15).pack(side=tk.LEFT, padx=10)
        tk.Button(button_row, text="Delete Item", width=15).pack(side=tk.LEFT, padx=10)
        tk.Button(self._inv_management_screen, text="Back", command=self.show_main_menu_screen).pack()

        # End of Inv. Management Screen set up ````````````````````````````````````````

        """Transaction Screen"""

        # Set up Transaction Screen ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # End of Transaction Screen set up ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



        
        # Start with main_menu
        self._main_menu_screen.pack(fill="both", expand=True)
    
    """ Screen Switching """

    def show_main_menu_screen(self):
        self._last.pack_forget()
        self._last = self._main_menu_screen
        self._main_menu_screen.pack(fill="both", expand=True)
        self._search_entry.unbind("<Return>")  # removes the event listener
    
    def show_search_items_screen(self):
        self._last.pack_forget()
        self._last = self._search_items_screen
        self._search_items_screen.pack(fill="both", expand=True)
        self._search_entry.bind("<Return>", self.handle_search_input)
        self._search_entry.delete(0, tk.END)
        self._results_listbox.delete(0, tk.END)
        self._search_entry.focus_set()  # optional: auto-focus
        
    def show_inv_management_screen(self):
        self._last.pack_forget()
        self._last = self._inv_management_screen
        self._inv_management_screen.pack(fill="both", expand=True)
        self._search_entry.delete(0, tk.END)
        self._results_listbox.delete(0, tk.END)
        self._search_entry.bind("<Return>", self.handle_search_input)



    """Event Handling"""

    def handle_search_input(self, event):
        self._results_listbox.delete(0, tk.END) # Clears listbox
        self._results_listbox.insert(0,f"Item #....Name............Qty.....Slot")
        query = self._search_entry.get().lower() # results of text box
        results = self._inventory.search(query)
        i = 1 # for inserting purposes
        # Formatting Search Results ````````````````````````````
        for entry in results: 

            # current format is string
            entry = str(entry).split(',') # Now its a list

            """The Item Number """
            # handle item #s being from 1 - 1000
            while len(entry[0])<4: # Possible vals are ... 1,2,3,4 , system only designed for up to 9,999 items
                entry[0] = "0" + entry[0]
            while len(entry[0])<10:
                entry[0] = entry[0] + "."

            """The Item Name """
            # handle names being longer than 16 
            if len(entry[1]) > 15:
                entry[1] = entry[0][:15]
            
            while len(entry[1]) < 16:
                entry[1] = entry[1] + "."

            """Item qty"""

            while len(entry[3])<8:
                entry[3]+= "."

            entry = f"{entry[0]}{entry[1]}{entry[3]}{entry[4]}"
            
        #End of Formatting Search Results ````````````````````````````

            self._results_listbox.insert(i,entry)
            i += 1

    """Begin Main Driver Logic"""
    def run(self):
        self._root.mainloop()



menu = Menu()
menu.run()



"""CURRENT TEST"""



"""ADD"""

# # Add item test ~~~~~~~~~~~~~~~~~~~~~

# item = {"name":"blueberry",
#         "description":"its a blueberry",
#         "qty":"1",
#         "location":"104"}

# inv.add_item(item)

# # End of Add item test ~~~~~~~~~~~~~~~~~~~~~


"""SEARCH"""


# # Search Test ````````````````````````

# # search method test
# results = inv.search("b")
# for entry in results:
#     print(str(entry))

# # End of Search Test ````````````````````````



"""DELETE"""


# # Delete item Test ~~~~~~~~~~~~~~~~~~~~~~~~~~

# # delete blueberry
# try:
#     name = "blueberry"
#     inv.delete_item(name)
# except KeyError:
#     print(f"{name} not in inventory")

# # End of Delete item Test ~~~~~~~~~~~~~~~~~~~~~~~~~~

"""MODIFY"""

# # Modify items Test ```````````````````````````
# try:
#     # search method test
#     results = inv.search("cook")
#     for entry in results:
#         print(str(entry))

#     name = "cookie"
#     inv.change_item(name,"qty","2")
#     # search method test
#     results = inv.search("cook")
#     for entry in results:
#         print(str(entry))

#     inv.change_item(name,"qty","5")
#     # search method test
#     results = inv.search("cook")
#     for entry in results:
#         print(str(entry))

# except KeyError:
#     print(f"You failed to modify {name}")

# # End of Modify items Test ```````````````````````````
