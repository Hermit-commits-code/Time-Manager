import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tkinter as tk
from tkinter import ttk
from data_handler import DataHandler
from gui import TimeTrackerGUI

def main():
    root = tk.Tk()
    root.title("Time Management Program")

    data_handler = DataHandler("data/time_logs.csv")
    app = TimeTrackerGUI(root, data_handler)

    root.mainloop()

if __name__ == "__main__":
    main()