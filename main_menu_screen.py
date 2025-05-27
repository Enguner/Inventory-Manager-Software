import tkinter as tk
import screen

class Main_Menu_Screen(screen.Screen):

    def __init__(self,root,screen_changer):
        super().__init__(root,screen_changer)

        tk.Label(self._screen, text="Inventory System").pack(pady=30)
        # Search button
        button = tk.Button(self._screen, text="Search Items",command=self.button_search, width=20,height=2)
        button.pack(pady=10)
        # Inv. Mgmt button
        button = tk.Button(self._screen, text="Inv. Management",command=self.button_inv_mgmt, width=20,height=2)
        button.pack(pady=10)
        # Transaction button
        button = tk.Button(self._screen, text="Transaction",command=self.button_transaction, width=20,height=2)
        button.pack(pady=10)
        # Logs button
        button = tk.Button(self._screen, text="Logs",width=20,height=2)
        button.pack(pady=10)
        # User Setup
        button = tk.Button(self._screen, text="User Setup", width=20,height=2)
        button.pack(pady=10)
    
    def button_transaction(self):
        self._screen_changer("transaction")

    def button_search(self):
        self._screen_changer("search")

    def button_inv_mgmt(self):
        self._screen_changer("inv_mgmt")
    
    @property
    def entries(self):
        entries = []
        return entries

    @property
    def results(self):
        results = []
        return results

    def focus(self):
        pass

    def clear(self):
        pass