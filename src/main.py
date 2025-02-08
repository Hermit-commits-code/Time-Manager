import sys
import os
import tkinter as tk
from tkinter import ttk
from data_handler import DataHandler
from gui import TimeTrackerGUI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
def main():
    # Create a new Tkinter window
    root = tk.Tk()
    # Set the title of the window
    root.title("Time Management Program")
    # Create an instance of the DataHandler class, passing in the path to the CSV file.
    data_handler = DataHandler("data/time_logs.csv")
    # Create an instance of the TimeTrackerGUI class, passing in the root window and the data_handler object.
    app = TimeTrackerGUI(root, data_handler)
    # Start the Tkinter main event loop, which will keep the window open until it is closed.
    root.mainloop()

# Entry Point check
# If the script is being run directly, call the main function
if __name__ == "__main__":
    main()