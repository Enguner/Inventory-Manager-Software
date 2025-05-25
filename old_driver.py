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
        self._transaction = []
        self._root.title("Inventory System")
        self._root.geometry("800x600")
        fixed_font = tkFont.Font(family="Courier New", size=10)

        # Create screens (frames)
        self._main_menu_screen = tk.Frame(self._root)
        self._search_items_screen = tk.Frame(self._root)
        self._inv_management_screen = tk.Frame(self._root)
        self._transaction_screen = tk.Frame(self._root)

        self._last = self._main_menu_screen 

        
        """
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Set Up Main Menu
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        
        tk.Label(self._main_menu_screen, text="Inventory System").pack(pady=30)
        
        # Search button
        button = tk.Button(self._main_menu_screen, text="Search Items", command=self.show_search_items_screen,width=20,height=2)
        button.pack(pady=10)
        # Inv. Mgmt button
        button = tk.Button(self._main_menu_screen, text="Inv. Management", command=self.show_inv_management_screen,width=20,height=2)
        button.pack(pady=10)
        # Transaction button
        button = tk.Button(self._main_menu_screen, text="Transaction", command=self.show_transaction_screen,width=20,height=2)
        button.pack(pady=10)
        # Logs button
        button = tk.Button(self._main_menu_screen, text="Logs",width=20,height=2)
        button.pack(pady=10)
        # User Setup
        button = tk.Button(self._main_menu_screen, text="User Setup", width=20,height=2)
        button.pack(pady=10)
        
        

        """
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              Set Up Search Screen
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """


        tk.Label(self._search_items_screen, text="Search Items").pack(pady=10)
        # Create Entry box (no 'text' or 'command' allowed)
        self._search_entry = tk.Entry(self._search_items_screen,width=60)
        self._search_entry.pack()
        self._search_results_listbox = tk.Listbox(self._search_items_screen,width=45,height=20,font=fixed_font)
        self._search_results_listbox.pack()
        tk.Button(self._search_items_screen, text="Back", command=self.show_main_menu_screen).pack()

        

        """
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          Set Up Inv. Management Screen
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """

        
        self._inv_entry = tk.Entry(self._inv_management_screen,width=60)
        self._inv_results_listbox = tk.Listbox(self._inv_management_screen,width=45,height=20,font=fixed_font)
        tk.Label(self._inv_management_screen, text="Inventory Management").pack(pady=10)
        self._inv_entry.pack()
        self._inv_results_listbox.pack()
        button_row = tk.Frame(self._inv_management_screen)
        button_row.pack(pady=5)

        # Two buttons packed side-by-side within the row
        tk.Button(button_row, text="Add Item",command=self.add_item, width=15).pack(side=tk.LEFT, padx=10)
        tk.Button(button_row, text="Modify Item", width=15).pack(side=tk.LEFT, padx=10)
        
        # Delete Item button
        tk.Button(button_row, text="Delete Item", width=15).pack(side=tk.LEFT, padx=10)
        
        # Return to main menu
        tk.Button(self._inv_management_screen, text="Back", command=self.show_main_menu_screen).pack()

        
        """
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Set Up Transaction Screen
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """

       
        # ````ROW 1````
        tk.Label(self._transaction_screen, text="Transaction Entry").pack(pady=10)
        

        #  ````ROW 2````
        # Setting up frames for transaction screen
        row_2 = tk.Frame(self._transaction_screen)
        row_2.pack(pady=5)
        id_col = tk.Frame(row_2)
        id_col.pack(side='left')
        # Frames set

        # Filling frames with entries and labels
        tk.Label(id_col,text="ID: ").pack(side='left')
        self._trans_entry = tk.Entry(id_col,width=60)
        self._trans_entry.pack(padx=5)
        qty_col = tk.Frame(row_2)
        qty_col.pack(side='left')
        tk.Label(qty_col,text="Qty: ").pack(side='left')
        self._trans_qty_entry = tk.Entry(qty_col,width=10)
        self._trans_qty_entry.pack()
        # Frames filled 
        
        # ```` ROW 3 ````

        row_3 = tk.Frame(self._transaction_screen)
        row_3.pack()
        self._trans_error_label = tk.Label(row_3)
        self._trans_error_label.pack()

        # ```` ROW 4 ````

        # Row 4 frame 
        row_4 = tk.Frame(self._transaction_screen,height=400)
        row_4.pack(pady=35)

        # Row 4 col 1
            # mod buttons frame (left)
        mod_buttons_col = tk.Frame(row_4,width=100)
        mod_buttons_col.pack(side='left',padx=15)

        # Row 4 col 2
            # trans listbox frame (center)
        trans_listbox_col = tk.Frame(row_4,width = 300)
        trans_listbox_col.pack(side='left',padx=15)
        
        # Row 4 col 3
            # confirmation buttons frame (right)
        conf_buttons_col = tk.Frame(row_4,width=100)
        conf_buttons_col.pack(side='right',padx=15)

        # Columns of row 4 now must be populated

        # Mod Buttons
        tk.Button(mod_buttons_col,text="Void",width=6,height=6).pack(pady=20)
        tk.Button(mod_buttons_col,text="Mod Qty",width=6,height=6).pack(pady=20)

        # List Box
        self._trans_results_listbox = tk.Listbox(trans_listbox_col,width=45,height=20,font=fixed_font)
        self._trans_results_listbox.pack()
        self._trans_total_items = tk.Label(trans_listbox_col,text="Total Items: 0")
        self._trans_total_items.pack()

        # Conf. Buttons
        tk.Button(conf_buttons_col,text="Finalize",width=8,height=8, command=self.handle_finalize).pack(pady=20)
        tk.Button(conf_buttons_col,text="Void all",width=8,height=8,command=self.handle_void_all).pack(pady=20)

        """
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               Finish Initialization
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        
        # Start with main_menu
        self._main_menu_screen.pack(fill="both", expand=True)
    
    """ Screen Switching """

    def show_main_menu_screen(self):
        self._last.pack_forget()
        if self._last == self._search_items_screen:
            self._search_entry.unbind("<Return>")
        elif self._last == self._transaction_screen:
            self._trans_entry.unbind("<Return>")
        elif self._last == self._inv_management_screen:
            self._inv_entry.unbind("<Return>")
        self._last = self._main_menu_screen
        self._main_menu_screen.pack(fill="both", expand=True)
    
    def show_search_items_screen(self):
        self._last.pack_forget()
        self._last = self._search_items_screen
        self._search_items_screen.pack(fill="both", expand=True)
        self._search_entry.delete(0, tk.END)
        self._search_results_listbox.delete(0, tk.END)
        self._search_entry.bind("<Return>", self.handle_search_input)
        self._search_entry.focus_set()  # optional: auto-focus
        
    def show_inv_management_screen(self):
        self._last.pack_forget()
        self._last = self._inv_management_screen
        self._inv_management_screen.pack(fill="both", expand=True)
        self._inv_entry.delete(0, tk.END) # Deletes search entry info
        self._inv_results_listbox.delete(0,tk.END)
        self._inv_entry.bind("<Return>", self.handle_inv_input) # Binds enter key with function
        self._inv_entry.focus_set()

    def show_transaction_screen(self):
        self._last.pack_forget()
        self._last = self._transaction_screen
        self._transaction_screen.pack(fill="both", expand=True) # Deletes search entry info
        self._trans_entry.delete(0, tk.END) # Binds enter key with function
        self._trans_results_listbox.delete(0, tk.END)
        self._trans_entry.focus_set()
        self._trans_entry.bind("<Return>", self.handle_transaction_input) # Binds enter key on item_ID entry widget
        self._trans_qty_entry.bind("<Return>", self.handle_transaction_input)

    """Event Handling"""



    """Search Screen Handling"""

    def handle_search_input(self,event):
        self._search_results_listbox.delete(0, tk.END) # Clears listbox
        self._search_results_listbox.insert(0,f"Item #....Name............Qty.....Slot")
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

            self._search_results_listbox.insert(i,entry)
            i += 1

    """Transaction Screen Handling"""

    def transaction_input_clear(self):
        self._trans_entry.delete(0,tk.END)
        self._trans_qty_entry.delete(0,tk.END)
        self._trans_entry.focus_set()

    def handle_transaction_input(self,event):
        """
        Function requirements:
            - handling multiple test cases 
            - current context of self._trans_entry widget 
                - is the entry widget empty 

                - does the entry widget have something in it
                    - should expect only numeric entries to ensure the user 
                    enters current items not previous versions no longer supported

                    - numeric is a decimal also invalid

                    - non-numeric items not allowed

        """
        id_contents = self._trans_entry.get()
        qty_contents = self._trans_qty_entry.get()

        if len(qty_contents) == 0:
            qty_contents = 1
        else: # There something in qty entry
            if qty_contents.isnumeric(): # Its a number
                if not qty_contents.isdigit(): # Its a decimal
                    qty_contents = 1
                else:
                    qty_contents = int(qty_contents)
            else:
                qty_contents = 1

        if len(id_contents) != 0: # checking Id entry widget

            if id_contents.isnumeric() and '.' not in id_contents: # must be a number and not a decimal
                if id_contents in self._inventory: # if the item is in inventory
                    self._trans_error_label.config(text="")

                    item = self._inventory[id_contents]
                    

                    # Item in inventory qty for added transaction exsist
                    self.transaction_input_clear()

                else:
                    self._trans_error_label.config(text="Item Not Find")
                    self.transaction_input_clear()
            else:
                self._trans_error_label.config(text="Item Not Find")
                self.transaction_input_clear()

    def handle_void_all(self):
        # Should later be implemented to log that user voided 
        # entire transaction as a security measure
        self.show_main_menu_screen()
    
    def handle_finalize(self):
        # Needs to actually subtract quantities after 
        self.show_main_menu_screen()
        # Should lead self._transactions [list] empty always
        pass

    """InvMgmt Screen Handling"""

    def handle_inv_input(self,event):
        self._inv_results_listbox.delete(0, tk.END) # Clears listbox
        self._inv_results_listbox.insert(0,f"Item #....Name............Qty.....Slot")
        query = self._inv_entry.get().lower() # results of text box
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

            self._inv_results_listbox.insert(i,entry)
            i += 1

    def add_item_popup(self):

        def is_valid(string):
            return string.isalnum() and any(c.isalpha() for c in string) and string[0].isalpha()
        
        def config_error_label(label,new_text,entry_to_focus=None):
            label.config(text=new_text,fg="red")
            if entry_to_focus != None:
                entry_to_focus.focus_set()

        def cancel():
            popup.destroy()
        
        def on_submit():
            item_name = item_name_entry.get().lower()
            if len(item_name) == 0: # Item name not entered
                config_error_label(item_name_error,"You need to enter a name for the item.",item_name_entry)

            else: # Non empty entry for item name

                if is_valid(item_name): #valid item name

                    # check that item name not in inventory already
                    if item_name not in self._inventory: #  item not in inventory
                        config_error_label(item_name_error,"")
                        # Item name tests passed
                        item_qty = item_qty_entry.get()
                        item_description = item_description_entry.get()

                        if item_qty.isdigit(): # Int entry
                            # Qty tests passed
                            config_error_label(item_qty_error,"")
                            item_location = item_location_entry.get()
                            if item_location.isdigit(): # item location is digit
                                # All tests passed
                                item_dict = {
                                    "name":f"{item_name}",
                                    "number":f"{int(self._inventory.item_number_max)+1}",
                                    "description":f"{item_description}",
                                    "qty":f"{item_qty}",
                                    "location":f"{item_location}"
                                }
                                self._inventory.add_item(item_dict)
                                self._inventory.save()
                                popup.destroy() # finished with popup

                            else:
                                config_error_label(item_location_error,"Location must be a digit representing slot.",item_location_entry)

                        else:
                            config_error_label(item_qty_error,"Qty for item must be an integer.",item_qty_entry)

                    else: # item in inventory
                        config_error_label(item_name_error,"Name is already assigned to an item",item_name_entry)

                else: # non valid item name
                    config_error_label(item_name_error,"Item name must begin with a letter, with only a-z or 0-9",item_name_entry)



        
        popup = tk.Toplevel(self._root)
        popup.title("Add Item")
        popup.geometry("450x300")

        # Various frames needed 
        frame_item_name = tk.Frame(popup)
        frame_item_name.pack()

        frame_item_description = tk.Frame(popup)
        frame_item_description.pack()

        frame_item_qty = tk.Frame(popup)
        frame_item_qty.pack()

        frame_item_location = tk.Frame(popup)
        frame_item_location.pack()

        frame_action_buttons = tk.Frame(popup)
        frame_action_buttons.pack()

        # Item name widgets
        tk.Label(frame_item_name, text="Add item name: ").pack(side="left")
        item_name_entry = tk.Entry(frame_item_name)
        item_name_entry.pack(side="left")

        # Item Name error message
        item_name_error = tk.Label(frame_item_name,text="")
        item_name_error.pack(side="left")

        # Item description widgets
        tk.Label(frame_item_description,text="Item description:").pack(side="left")
        item_description_entry = tk.Entry(frame_item_description)
        item_description_entry.pack(side="left")

        # Item qty widgets
        tk.Label(frame_item_qty,text="Enter qty:").pack(side="left")
        item_qty_entry = tk.Entry(frame_item_qty)
        item_qty_entry.pack(side="left")

        # Item qty error message
        item_qty_error = tk.Label(frame_item_qty,text="")
        item_qty_error.pack(side="left")

        # Item location widgets
        tk.Label(frame_item_location,text="Enter location (ex:'102')").pack(side="left")
        item_location_entry = tk.Entry(frame_item_location)
        item_location_entry.pack(side="left")

        # Item location error message
        item_location_error = tk.Label(frame_item_location,text="")
        item_location_error.pack(side="left")

        # Cancel Button
        tk.Button(frame_action_buttons,text="Cancel",command=cancel).pack(padx=5,side="left")
        # Submit Button
        tk.Button(frame_action_buttons,text="Submit",command=on_submit).pack(padx=5,side="left")

        item_name_entry.focus_set()


    def add_item(self, item_dict=None):
        self.add_item_popup()
    
    def delete_item(self):
        pass
    
    def modify_item(self):
        pass
    

    """Begins Main Driver Logic"""
    def run(self):
        self._root.mainloop()



menu = Menu()


menu.run()



