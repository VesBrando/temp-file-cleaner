import os
import shutil
import winshell
import tkinter as tk
from tkinter import *
from tkinter import messagebox

userid = os.environ.get('USERNAME')
tempdir = (f'C:\\Users\\{userid}\\AppData\\Local\\Temp') 


def clean_temp():
    answer = tk.messagebox.askyesno('Confirmation', 'Are you sure you want to clean your Temp folder?')
    if answer:
        for item in os.listdir(tempdir):
            itempath = os.path.join(tempdir, item)
            try:
                if os.path.isfile(itempath) or os.path.islink(itempath):
                    os.unlink(itempath)
                elif os.path.isdir(itempath):
                    shutil.rmtree(itempath)
            except Exception as e:
                print(f'Failed to delete {itempath}. Reason: {e}')
        #Clear Recycle Bin
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        tk.messagebox.showinfo('Success', 'Temp folder has been cleaned successfully!')
    else:
        tk.messagebox.showinfo('Cancelled', 'Operation cancelled by user.')


clean_temp()