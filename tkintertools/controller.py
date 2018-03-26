'''The gui controller'''
import tkinter as tk
from collections import deque

class Controller(tk.Tk):
    def __init__(self, fullscreen=False, x=400, y=400, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        if fullscreen:
            self.wm_attributes('-fullscreen','true')
            width=self.winfo_screenwidth()-self.padding
            height=self.winfo_screenheight()-self.padding
            self.geometry('{}x{}+0+0'.format(width, height))
        else:
            self.geometry('{}x{}'.format(x,y))
        

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        self.current_page = None
        self.history = deque([], 10)

    def show_page(self, name, data=False, history=False):
        if self.current_page[0].page_leave():
            self.history.append([self.current_page[1], self.current_page[2])
            self.pages[name].render(data, history=True)
            self.pages[name].tkraise()
            self.current_page = [self.pages[name], name, data]


    def go_back(self):
        last_page = self.history.pop()
        self.show_page(last_page[0], last_page[1], history=True)

    def add_page(self, page):
        self.pages[page.__name__] = page(parent=self.container)
        self.pages[page.__name__].grid(row=0, column=0, sticky="nsew")

    def add_page_instance(self, name, instance):
        self.pages[name] = instance
        self.pages[name].grid(row=0, column=0, sticky="nsew")