import screen
from tkinter import messagebox
import tkinter as tk
import inventory

class Inv_Mgmt_Screen(screen.Screen):
    
    """ Class Set Up"""

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

    # Attributes

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
    
    # Methods

    def focus(self):
        self._inv_entry.focus_set()

    def clear(self):
        self._inv_entry.delete(0,tk.END)
        self._inv_results_listbox.delete(0,tk.END)


    """ Screen's Widget Logic """


    # Buttons
    def modify_item_button(self):
        
        def get_item_number(selected_entry):
            selected_entry = selected_entry.split('.')
            item_number = str(int(selected_entry[0])) # Typecasted twice to remove leading zeros
            return item_number

        selected = self._inv_results_listbox.curselection() # Set variable to selected of list box
        if selected: # There is something selected
            index = selected[0]
            if index != 0: # Not a valid selected result because its the header result
                selected = self._inv_results_listbox.get(index)
                if '.' in selected:
                    selected = get_item_number(selected)
                    self.modify_item_popup(selected)
                    self.clear()

                
                else:
                    messagebox.showwarning("You must choose an item from inventory to modify")

            else:
                messagebox.showwarning("You must choose an item from inventory to modify")

            
        else: # Nothing is selected
            messagebox.showwarning("No Item Selected","You need to have an item selected to modify its details!")
            
    def add_item_button(self):
        self.add_item_popup()

    def delete_item_button(self):
        def is_valid(string):
            valid = False
            string = str(string)
            if "Item #." not in string and string != "" and string[0] != " ":
                valid = True
            return valid

        def get_item_name(selected):
            if "......" not in selected:
                raise KeyError("Please note format to this function relies on item number having exactly 6 dots after number, if this was changed please update this function") 
            selected = selected.split(".")
            for entry in selected:
                if entry.isalpha():
                    item_name = entry
            return item_name

        def get_item_number(selected):
            item_number = ''
            running = True
            i = 0 
            if ".." not in selected:
                raise KeyError(f"The format of the listbox results have changed and this function should be modified selected = {selected}")
            while running:
                if selected[i] != ".":
                    item_number += selected[i] 
                    i+=1
                else:
                    running = False
            
            if item_number.isdigit():
                item_number = int(item_number) # Removes trailing zeros
                item_number = str(item_number) # back to desired format

            else:
                raise TypeError(f"The item number must be a digit but was something else, item number = {item_number}")
            
            return item_number

        selected = self._inv_results_listbox.curselection()
        if selected: # There is something selected 
            index = selected[0]
            selected = self._inv_results_listbox.get(index)
            if is_valid(selected): # Is a item in inventory
                item_name = get_item_name(selected)
                verification = messagebox.askyesno("Confirm Deletion",f"Are you sure you would like to delete this item {item_name} from your inventory forever?")
                if verification:
                    item_number = get_item_number(selected)
                    inv = inventory.Inventory()
                    inv.delete_item(item_number)
                    messagebox.showinfo("Item Deleted",f"The item {item_name} was deleted from your inventory!")
            else: # (ERROR) is something else in the inventory not meant to be deleted like no results entry
                messagebox.showerror("Invalid Selection","You must select an item in inventory from search.")
        else: # Nothing is selected (ERROR)
            messagebox.showerror("No Item Selected", "You must select an item to delete.")
        
        self.clear()
        self.focus()

    def back_button(self):
        self._screen_changer("main_menu")

    # Widget's button handling

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

    def add_item_popup(self):
        inv = inventory.Inventory()

        def is_valid(string):
            return string.isalnum() and any(c.isalpha() for c in string) and string[0].isalpha()
        
        def config_error_label(label,new_text,entry_to_focus=None):
            label.config(text=new_text,fg="red")
            if entry_to_focus != None:
                entry_to_focus.focus_set()

        def on_cancel():
            popup.destroy()
        
        def on_submit():
            item_name = item_name_entry.get().lower()
            if len(item_name) == 0: # Item name not entered
                config_error_label(item_name_error,"You need to enter a name for the item.",item_name_entry)

            else: # Non empty entry for item name

                if is_valid(item_name): #valid item name

                    # check that item name not in inventory already
                    if item_name not in inv: #  item not in inventory
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
                                    "number":f"{int(inv.item_number_max)+1}",
                                    "description":f"{item_description}",
                                    "qty":f"{item_qty}",
                                    "location":f"{item_location}"
                                }
                                inv.add_item(item_dict)
                                inv.save()
                                popup.destroy() # finished with popup

                            else:
                                config_error_label(item_location_error,"Location must be a digit representing slot.",item_location_entry)

                        else:
                            config_error_label(item_qty_error,"Qty for item must be an integer.",item_qty_entry)

                    else: # item in inventory
                        config_error_label(item_name_error,"Name is already assigned to an item",item_name_entry)

                else: # non valid item name
                    config_error_label(item_name_error,"Item name must begin with a letter, with only a-z or 0-9",item_name_entry)

        popup = tk.Toplevel(self._screen)
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
        tk.Button(frame_action_buttons,text="Cancel",command=on_cancel).pack(padx=5,side="left")
        # Submit Button
        tk.Button(frame_action_buttons,text="Submit",command=on_submit).pack(padx=5,side="left")

        item_name_entry.focus_set()

    def modify_item_popup(self,item_number):
        def is_valid(string):
            return string.isalnum() and any(c.isalpha() for c in string) and string[0].isalpha()
        
        def on_submit():
            item_name = item_name_entry.get().lower()
            if len(item_name) == 0: # Item name not entered
                config_error_label(item_name_error,"You need to enter a name for the item.",item_name_entry)

            else: # Non empty entry for item name

                if is_valid(item_name): #valid item name

                    # check that item name not in inventory already
                    if item_name not in inv: #  item not in inventory
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
                                    "description":f"{item_description}",
                                    "qty":f"{item_qty}",
                                    "location":f"{item_location}"
                                }
                                item_number = item_number_entry.get()
                                item_to_change = inv[item_number]
                                inv.change_item(item_to_change,item_dict)
                                inv.save()
                                popup.destroy() # finished with popup

                            else:
                                config_error_label(item_location_error,"Location must be a digit representing slot.",item_location_entry)

                        else:
                            config_error_label(item_qty_error,"Qty for item must be an integer.",item_qty_entry)

                    else: # item in inventory
                        config_error_label(item_name_error,"Name is already assigned to an item",item_name_entry)

                else: # non valid item name
                    config_error_label(item_name_error,"Item name must begin with a letter, with only a-z or 0-9",item_name_entry)

        def config_error_label(label,new_text,entry_to_focus=None):
            label.config(text=new_text,fg="red")
            if entry_to_focus != None:
                entry_to_focus.focus_set()

        def on_cancel():
            popup.destroy()
            

        inv = inventory.Inventory()
        item = inv[item_number]
        popup = tk.Toplevel(self._screen)
        popup.title("Modify Item")
        popup.geometry("450x300")
        
        # Various frames needed 
        frame_item_number = tk.Frame(popup)
        frame_item_number.pack()
        
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

        # Item number
        tk.Label(frame_item_number, text="item number: ").pack(side="left")
        item_number_entry = tk.Entry(frame_item_number) # Entry Widget
        item_number_entry.pack(side="left")
        item_number_entry.insert(0,item.number)
        item_number_entry.config(state="readonly")  # Makes it uneditable

        # Item name widgets
        tk.Label(frame_item_name, text="Edit item name: ").pack(side="left")
        item_name_entry = tk.Entry(frame_item_name) # Entry Widget
        item_name_entry.pack(side="left")
        item_name_entry.insert(0,item.name)

        # Item Name error message
        item_name_error = tk.Label(frame_item_name,text="")
        item_name_error.pack(side="left")

        # Item description widgets
        tk.Label(frame_item_description,text="Edit Item description:").pack(side="left")
        item_description_entry = tk.Entry(frame_item_description) # Entry Widget
        item_description_entry.pack(side="left")
        item_description_entry.insert(0,item.description)

        # Item qty widgets
        tk.Label(frame_item_qty,text="Edit qty:").pack(side="left")
        item_qty_entry = tk.Entry(frame_item_qty) # Entry Widget
        item_qty_entry.pack(side="left")
        item_qty_entry.insert(0,item.qty)

        # Item qty error message
        item_qty_error = tk.Label(frame_item_qty,text="")
        item_qty_error.pack(side="left")

        # Item location widgets
        tk.Label(frame_item_location,text="Edit location (ex:'102')").pack(side="left")
        item_location_entry = tk.Entry(frame_item_location) # Entry Widget
        item_location_entry.pack(side="left")
        item_location_entry.insert(0,item.location)

        # Item location error message
        item_location_error = tk.Label(frame_item_location,text="")
        item_location_error.pack(side="left")

        # Cancel Button
        tk.Button(frame_action_buttons,text="Cancel",command = on_cancel).pack(padx=5,side="left")
        # Submit Button
        tk.Button(frame_action_buttons,text="Submit",command = on_submit).pack(padx=5,side="left")
