class Item:
    def __init__(self,item_dict):
        attributes =["number","name","description","qty","location"]
        """Attributes val can be None if dict not passed in right"""
        self._item_dict = {}
        for attribute in attributes:
            # loop 1, attribute = "number"
            if attribute in item_dict:
                self._item_dict[attribute] = item_dict[attribute]
            else:
                self._item_dict[attribute] = None
    
    def __getitem__(self,key):
        """
        Can return None on thing not found
        """
        if key in self._item_dict:
            return self._item_dict[key]
        else:
            return None
    
    @property
    def name(self):
        return self._item_dict["name"]

    @property
    def qty(self):
        return self._item_dict["qty"]
    
    @property
    def number(self):
        return self._item_dict["number"]

    @property
    def description(self):
        return self._item_dict["description"]

    @property
    def location(self):
        return self._item_dict["location"]

    def __repr__(self):
        attributes =["number","name","description","qty","location"]
        describing_string = ""
        for attribute in attributes:
            describing_string+=f"{self[attribute]},"
        describing_string = describing_string[:len(describing_string)-1] + "\n"
        return describing_string

    def __setitem__(self, key, value):
        if key in self._item_dict:
            self._item_dict[key] = value
        else:
            raise KeyError(f"{key} is not a valid attribute")

