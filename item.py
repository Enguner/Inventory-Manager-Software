class Item:
    attributes =["number","description","qty","location"]
    def __init__(self,item_dict):
        self._name = item_dict["name"]
        """Attributes val can be None if dict not passed in right"""
        self._item_dict = {}
        


        for attribute in self.attributes:
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
        return self._name
    
    def __repr__(self):
        describing_string = ""
        describing_string += f"{self.name},"
        for attribute in self.attributes:
            describing_string+=f"{self[attribute]},"
        describing_string = describing_string[:len(describing_string)-1] + "\n"
        return describing_string

class Inventory:
    def __init__(self):
        self._items = {}
        
        try:
            file = open("items.txt","r")
            
        except FileNotFoundError:
            file = open("items.txt","w")
            file.close()
            file = open("items.txt","r")
        
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
                self._items[item_dict["name"]] = Item(item_dict)

         
    def search(self,string):
        keys = self.names
        items = []
        for key in keys:
            if string in key:
                items.append(self._items[key])
        return items
                
    
    @property
    def names(self):
        names = list(self._items.keys()) 
        names.sort()
        return names

class Menu:
    inventory = Inventory()

    def print_item(self,item):
        item = item.split(',')
        #name,number,description,qty,location

        if len(item[0])<16:
            while len(item[0]) < 16:
                item[0] += " "
        elif len(item[0]) > 16:
            item[0] = item[0][:17]
        print(f"{item[0]}",end="")
        print(f"|Item Number: {item[1]}",end="\t")
        print(f"|Qty: {item[3]}",end="\t")
        print(f"|Slot: {item[4]}",end="")

    def run(self):
        running = True
        user = -1
        prompt = "1. Find Item\n" \
        "2. Enter Transaction\n" \
        "3. Quit\n"
        while running:
            user=input(prompt)
            if user.isnumeric():
                user = int(user)



                # Branches
                if user == 1:
                    search_string = input("Search: ")
                    results = self.inventory.search(search_string)
                    if len(results) < 1:
                        print("No results found")
                    else:
                        for item in results:
                            self.print_item(str(item))
                if user == 2:
                    transaction = True
                    while transaction:

                        pass

                if user == 3:
                    running = False


menu = Menu()
menu.run()
        
