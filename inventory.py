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
                self._items[item_dict["name"]] = item.Item(item_dict)

    def __getitem__(self,key):
        if key in self._items:
            return self._items[key]
        else:
            raise KeyError("Item not in inventory")

    def __contains__(self,name):
        if name in self._items:
            return True
        else:
            return False
    
    def __len__(self):
        return len(self._items)
    
    def search(self,string):
        keys = self.names
        items = []
        for key in keys:
            if string in key:
                items.append(self._items[key])
        return items
    
    def save(self):
        file = open(self._file,'w')
        names = self.names
        for name in names:
            file.write(repr(self._items[name]))
        file.close()

    def add_item(self,item_dict): 
        # CAN RAISE ERROR
        # Should not include number as key, will be ignored
        
        item_dict["number"] = self.max + 1
        if item_dict["name"] not in self._items: # make sure name not repeated
            self._items[item_dict["name"]] = item.Item(item_dict)
            self.save()
        else:
            raise KeyError("Key already in dictionary 'aka' name already in use")

    def delete_item(self,name):
        # CAN RAISE ERROR
        if name not in self._items:
            raise KeyError("Name not found in items dictionary")
        else:
            self._items.__delitem__(name)
            self.save()

    def change_item(self,name,attribute,new_val):
        """
        Change some attribute of an item in inventory

        Params:
            -name: name it goes by inventory system
            -attribute: attribute that should be changed
            -new_val: new value it should be set to
        """
        try:
            # remember item returned should still be a dictionary structure
            item = self[name] # item dictionary 
            try:
                item[attribute] = new_val

            except KeyError:
                raise KeyError("Attribute category doesnt exsist")

        except KeyError:
            raise KeyError("Item not in inventory")
        
        self.save()

    @property
    def names(self):
        names = list(self._items.keys()) 
        names.sort()
        return names
    
    @property
    def max(self):
        max = 1
        for item in self._items.values():
            current = int(item["number"])
            if current > max:
                max = current
        return max