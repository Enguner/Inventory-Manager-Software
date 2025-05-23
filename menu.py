import tkinter as tk

class Menu:
    def __init__(self):
        self._root = tk.Tk()
        label = tk.Label(self._root, text="Hello, Tkinter!")
        label.pack()
        button = tk.Button(self._root, text="Click Me!")
        button.pack()

    def run(self):
        self._root.mainloop()

