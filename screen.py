import tkinter as tk
import tkinter.font as tkFont
import abc



class Screen(abc.ABC):
    _fixed_font = None

    def __init__(self,root,screen_changer):
        self._screen = tk.Frame(root)
        self._screen_changer = screen_changer
        if Screen._fixed_font is None:
            Screen._fixed_font = tkFont.Font(family="Courier New", size=10)

    def format_results(results):
        formatted_results = []
        for entry in results:
            # current format is string
            entry = str(entry).split(',') # Now its a list

            """The Item Number """
            # handle item #s being from 1 - 1000
            while len(entry[0])<4: # Possible vals are ... 1,2,3,4 , system only designed for up to 9,999 items
                entry[0] = "0" + entry[0]
            while len(entry[0])<10:
                entry[0] = entry[0] + "."

            """The Item Name """
            # handle names being longer than 16 
            if len(entry[1]) > 15:
                entry[1] = entry[0][:15]
            
            while len(entry[1]) < 16:
                entry[1] = entry[1] + "."

            """Item qty"""

            while len(entry[3])<8:
                entry[3]+= "."

            entry = f"{entry[0]}{entry[1]}{entry[3]}{entry[4]}"
            formatted_results.append(entry)

        return formatted_results

    @property
    def screen(self):
        return self._screen
    
    @property
    @abc.abstractmethod
    def results(self):
        pass

    @property
    @abc.abstractmethod
    def entries(self):
        pass