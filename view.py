"""
MVC View Module
"""

import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    """
    MVC View Class
    """

    PAD = 10

    def __init__(self, controller):
        """
        View Constructor
        """
        super().__init__()
        self.title("MVC Application")

        self.controller = controller
        self.value_var = tk.StringVar()

        self._make_main_frame()
        self._center_window()

    def main(self):
        """
        main entry for View
        """
        self.mainloop()

    def _make_main_frame(self):
        """
        Create the main Frame window
        """
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _center_window(self):
        self.update()  # Update widnow properties to reflect current sizes
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        self.geometry(f"{width}x{height}+{x_offset}+{y_offset}")
