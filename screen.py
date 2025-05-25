import tkinter as tk
import tkinter.font as tkFont
import abc



class Screen(abc.ABC):
    _fixed_font = None

    def __init__(self,root,screen_changer):
        self._screen = tk.Frame(root)
        self._screen_changer = screen_changer
        if Screen._fixed_font is None:
            tkFont.Font(family="Courier New", size=10)

    @property
    def screen(self):
        return self._screen

    @abc.abstractmethod
    def handle_events(self):
        pass
