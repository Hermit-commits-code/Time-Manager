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
    # The create_widgets method is responsible for creating and arranging the GUI elements.
    def create_widgets(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)

        # Create a label for the project selection dropdown.
        self.project_label = ttk.Label(self.root, text="Project:")
        self.project_label.grid(row=0, column=0, padx=10, pady=10)

        # Create a dropdown menu for selecting the project.
        self.project_var = tk.StringVar()
        self.project_dropdown = ttk.Combobox(self.root, textvariable=self.project_var, values=self.data_handler.projects)
        self.project_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Create a start button for tracking time.
        self.start_button = ttk.Button(self.root, text="Start", command=self.start_tracking)
        self.start_button.grid(row=1, column=0, padx=10, pady=10)

        # Create a stop button for stopping the time tracking.
        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_tracking)
        self.stop_button.grid(row=1, column=1, padx=10, pady=10)
        
        # Create a label for manual entry selection
        self.manual_entry_label = ttk.Label(self.root, text="Manual Entry:")
        self.manual_entry_label.grid(row=2, column=0, padx=10, pady=10)

        # Create an entry widget for entering the start time.
        self.start_time_entry = ttk.Entry(self.root)
        self.start_time_entry.grid(row=2, column=1, padx=10, pady=10)
        self.start_time_entry.insert(0, "Start Time: (HH:MM)")

        # Create an entry widget for entering the end time.
        self.end_time_entry = ttk.Entry(self.root)
        self.end_time_entry.grid(row=3, column=1, padx=10, pady=10)
        self.end_time_entry.insert(0, "End Time: (HH:MM)")

        # Create a button for logging the manual entry.
        self.manual_entry_button = ttk.Button(self.root, text="Log Time", command=self.log_manual_entry)
        self.manual_entry_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

        # Create a listbox for displaying the log messages.
        self.log_listbox = tk.Listbox(self.root)
        self.log_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Add the start_tracking and stop_tracking methods to the TimeTrackerGUI class.
    def start_tracking(self):
        self.start_time = datetime.now()
        self.log_listbox.insert(tk.END, f"Started tracking at {self.start_time.strftime('%H:%M')}")

    def stop_tracking(self):
        self.end_time = datetime.now()
        project_name = self.project_var.get()
        self.data_handler.log_time(project_name, self.start_time, self.end_time)
        self.log_listbox.insert(tk.END, f"Stopped tracking at {self.end_time.strftime('%H:%M')}")
    
    def log_manual_entry(self):
        project_name = self.project_var.get()
        start_time_str = self.start_time_entry.get()
        end_time_str = self.end_time_entry.get()
        try:
            start_time = datetime.strptime(start_time_str, "%H:%M")
            end_time = datetime.strptime(end_time_str, "%H:%M")
            self.data_handler.log_time(project_name, start_time, end_time)
            self.log_listbox.insert(tk.END, f"Logged manual entry for {project_name} from {start_time_str} to {end_time_str}")
        except ValueError:
            self.log_listbox.insert(tk.END, "Invalid time format. Please use HH:MM format.")