import item

class Inventory:
    _file = "items.txt"

    def __init__(self):
        self._items = {}
        
        try:
            file = open(self._file,"r")
            
        except FileNotFoundError:
            file = open(self._file,"w")
            file.close()
            file = open(self._file,"r")
        
        contents = file.read()
        file.close()
        if len(contents) == 0:
            pass
        else:
            contents = contents.split("\n")
            keys = ["number","name","description","qty","location"]
            item_dict = {}

            for entry in contents:
                if entry.strip() == "":
                    continue
                i = 0
                entry = entry.split(",")
                for key in entry:
                    item_dict[keys[i]] = key
                    i+=1 
                self._items[item_dict["number"]] = item.Item(item_dict)

    def __getitem__(self,key):
        item_numbers = self.item_numbers
        if key in item_numbers:
            return self._items[key]
        else:
            raise KeyError("Item not in inventory")

    def __contains__(self,search_string):
        item_numbers = self.item_numbers
        item_names = self.item_names

        if search_string.isalpha(): # name look up
            if search_string in item_names:
                return True
            else:
                return False
        
        elif search_string.isnumeric():
            if search_string in item_numbers:
                return True
            else:
                return False
    
        else:
            return False
 
    def __len__(self):
        return len(self._items)
    
    def search(self,search_string): # Returns items
        results = []
        item_numbers = self.item_numbers

        if search_string.isnumeric(): # Used a item_number to find items
            # Should return items with matching numbers
            for entry in item_numbers:
                if entry.startswith(search_string):
                    results.append(self[entry])

        elif search_string.isalpha(): # Used name to find items
            for entry in item_numbers:
                if self[entry]["name"].startswith(search_string): # if the entry name starts with the search string return item
                    results.append(self[entry])

        return results
    
    def save(self):
        file = open(self._file,'w')
        item_numbers = self.item_numbers
        for entry in item_numbers:
            file.write(repr(self._items[entry]))
        file.close()

    def add_item(self,item_dict): 
        # CAN RAISE ERROR
        # Should not include number as key, will be ignored
        used_names = self.item_names
        
        item_dict["number"] = int(self.item_number_max) + 1
        if item_dict["name"] not in used_names: # make sure name not repeated
            self._items[item_dict["number"]] = item.Item(item_dict)
            self.save()
        else:
            raise KeyError("Key already in dictionary 'aka' name already in use")

    def delete_item(self,number):
        # CAN RAISE ERROR
        if number not in self._items:
            raise KeyError("Name not found in items dictionary")
        else:
            self._items.__delitem__(number)
            self.save()

    def change_item(self,number,attribute,new_val):
        """
        Change some attribute of an item in inventory

        Params:
            -name: name it goes by inventory system
            -attribute: attribute that should be changed
            -new_val: new value it should be set to
        """
        try:
            # remember item returned should still be a dictionary structure
            item = self[number] # item dictionary 
            try:
                item[attribute] = new_val

            except KeyError:
                raise KeyError("Attribute category doesnt exsist")

        except KeyError:
            raise KeyError("Item not in inventory")
        
        self.save()

    @property
    def item_names(self):
        names = []
        for entry in self._items.values():
            names.append(entry["name"])
        return names
        
    
    @property
    def item_numbers(self):
        return self._items.keys()
    
    @property
    def item_number_max(self):
        keys = list(self.item_numbers)
        keys.sort()
        return keys[-1]





# inv = Inventory()
# if '3' in inv:
#     print("hello")
# else:
#     print("no")
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
