import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Create a new class called TimeTrackerGUI
class TimeTrackerGUI:
    # The __init__ method is a special method that is called when a new object of the class is created.
    # It takes two parameters: root and data_handler.
    # The root parameter is the Tkinter root window, and the data_handler parameter is an instance of the DataHandler class.
    def __init__(self, root, data_handler):
        self.root = root
        self.data_handler = data_handler
        # Call the create_widgets method to create the GUI elements.
        self.create_widgets()

    def create_widgets(self):
        self.project_label = ttk.Label(self.root, text="Project:")
        self.project_label.grid(row=0, column=0, padx=10, pady=10)

        self.project_entry = ttk.Entry(self.root)
        self.project_entry.grid(row=0, column=1, padx=10, pady=10)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_tracking)
        self.start_button.grid(row=1, column=0, padx=10, pady=10)

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_tracking)
        self.stop_button.grid(row=1, column=1, padx=10, pady=10)

        self.log_listbox = tk.Listbox(self.root)
        self.log_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Add the start_tracking and stop_tracking methods to the TimeTrackerGUI class.
    def start_tracking(self):
        self.start_time = datetime.now()
        self.log_listbox.insert(tk.END, f"Started tracking at {self.start_time.strftime('%H:%M')}")

    def stop_tracking(self):
        self.end_time = datetime.now()
        project_name = self.project_entry.get()
        self.data_handler.log_time(project_name, self.start_time, self.end_time)
        self.log_listbox.insert(tk.END, f"Stopped tracking at {self.end_time.strftime('%H:%M')}")