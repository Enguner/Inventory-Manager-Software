import screen
import tkinter as tk

class Transaction_Screen(screen.Screen):
    def __init__(self,root,screen_changer):
        _font = screen.Screen._fixed_font
        super().__init__(root,screen_changer)
        self._current_transaction = []
                # ````ROW 1````
        tk.Label(self._screen, text="Transaction Entry").pack(pady=10)
        

        #  ````ROW 2````
        # Setting up frames for transaction screen
        row_2 = tk.Frame(self._screen)
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

        row_3 = tk.Frame(self._screen)
        row_3.pack()
        self._trans_error_label = tk.Label(row_3)
        self._trans_error_label.pack()

        # ```` ROW 4 ````

        # Row 4 frame 
        row_4 = tk.Frame(self._screen,height=400)
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
        self._trans_results_listbox = tk.Listbox(trans_listbox_col,width=45,height=20,font=_font)
        self._trans_results_listbox.pack()
        self._trans_total_items = tk.Label(trans_listbox_col,text="Total Items: 0")
        self._trans_total_items.pack()

        # Conf. Buttons
        tk.Button(conf_buttons_col,text="Finalize",width=8,command=self.button_finalize,height=8).pack(pady=20)
        tk.Button(conf_buttons_col,text="Void all",width=8,height=8).pack(pady=20)
    
    @property
    def entries(self):
        entries = []
        return entries

    @property
    def results(self):
        results = []
        return results

    def button_finalize(self):
        self._screen_changer("main_menu")
    
    def clear(self):
        pass

    def focus(self):
        pass