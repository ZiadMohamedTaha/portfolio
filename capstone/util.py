import os
import pickle
import tkinter as tk
from tkinter import messagebox

def zi_button(window, text, color, command, fg='white'):
    button = tk.Button(
                        window,
                        text=text,
                        activebackground="black",
                        activeforeground="white",
                        fg=fg,
                        bg=color,
                        command=command,
                        height=2,
                        width=20,
                        font=('Helvetica bold', 20)
                    )

    return button


def img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label


def text(window, text):
    label = tk.Label(window, text=text)
    label.config(font=("sans-serif", 21), justify="left")
    return label


def entry_text(window):
    inputtxt = tk.Text(window,
                       height=2,
                       width=15, font=("Arial", 32))
    return inputtxt


def msg(title, description):
    messagebox.showinfo(title, description)


def recognize(img, db_path):

    return 'functionality_not_implemented'

