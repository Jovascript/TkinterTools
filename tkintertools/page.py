import tkinter as tk


class Page(tk.Frame):
    def __init__(self, parent):
        '''It is here where all widgets are initialised.'''
        super().__init__(master=parent)

    def render(self, data=False, history=False):
        '''Receives render data through data arg, and has to change values.'''
        pass

    def page_leave(self):
        '''Page is being closed, remove timers etc. for performance.
        Return True for success, False to block move.'''