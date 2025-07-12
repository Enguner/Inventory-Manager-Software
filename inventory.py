import item

class Inventory:
    _file = "items.txt"
    _intstance = None
    _initialized = False

    def __new__(cls, *args):
        if cls._intstance is None:
            cls._intstance = super().__new__(cls)
        return cls._intstance

    def __init__(self):
        if not Inventory._initialized:
            self._items = {}
            try:
                file = open(Inventory._file,"r")
                
            except FileNotFoundError:
                file = open(Inventory._file,"w")
                file.close()
                file = open(Inventory._file,"r")
            
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
        Inventory._initialized = True
        
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
        file = open(Inventory._file,'w')
        item_numbers = self.item_numbers
        for entry in item_numbers:
            file.write(repr(self._items[entry]))
        file.close()

    def add_item(self,item_dict,item_number=None): 
        # CAN RAISE ERROR
        # Should not include number as key, will be ignored
        if item_number is not None:
            if item_number in self:
                raise KeyError("The system cannot contain 2 items with the same number")

        else:
            item_dict["number"] = int(self.item_number_max) + 1
        used_names = self.item_names
        
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

    def change_item(self,old_item,new_item):
        """
        Change some attribute of an item in inventory

        Params:
            -name: name it goes by inventory system
            -attribute: attribute that should be changed
            -new_val: new value it should be set to
        """
        item_numbers = self.item_numbers
        attributes = old_item.keys()
        for attribute in attributes:
            if old_item[attribute] != new_item[attribute]:
                old_item
        
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
        if len(keys) == 0:
            return 0
        else:
            return keys[-1]





