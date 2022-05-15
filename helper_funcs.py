# IMPORTS
import os, qrcode
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


# CUSTOM FUNCTIONS
def show_error(title, error_message):
    """Show a GUI error message."""

    box = Tk()  # Create Tkinter Window Object
    box.withdraw()  # Hide Tkinter Window Object
    messagebox.showerror(title, error_message)  # Show pop up
    box.destroy()


def show_info(title, info_message):
    """Show a GUI info message."""

    box = Tk()
    box.withdraw()
    messagebox.showinfo(title, info_message)
    box.destroy()


def yes_or_no(title, question):
    """Pops up a GUI alert window that asks a yes or no question to the user.
    It returns True if user clicks yes, it returns False if user clicks no."""

    box = Tk()
    box.withdraw()
    answer = messagebox.askyesno(title, question)
    box.destroy()

    # Return user's answer (True/False)
    return answer


def get_path(message = "Select a Folder", initdir = os.getcwd()):
    """Get a Tkinter File Dialog."""

    box = Tk()
    box.withdraw()
    folder = filedialog.askdirectory(title = message, initialdir = initdir)
    box.destroy()

    return folder


def check_valid_path(path):
    """Check the given path is valid for Windows."""

    # If the length of the given path is 0, assume it is the local folder
    if len(path) == 0:
        return True

    else:
        return os.path.isdir(path)



def getQR(info):
    """Return a QR Code based on given information."""

    return qrcode.make(info)
