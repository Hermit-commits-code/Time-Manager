import csv
from datetime import datetime

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.projects = ["Project A", "Project B", "Project C", "Project D", "Project E"]
    # This method reads the data from the CSV file and returns it as a list of dictionaries.
    def log_time(self, project_name, start_time, end_time):
        # Calculate the duration of the time entry in minutes
        duration = (end_time - start_time).total_seconds() / 60
        # Open the CSV file in append mode and write the new time entry to the file
        with open(self.file_path, mode='a', newline='') as file:
            # Create a CSV writer object
            writer = csv.writer(file)
            # Write the new time entry to the CSV file
            writer.writerow([datetime.now().date(), project_name, start_time.strftime("%H:%M"), end_time.strftime("%H:%M"), duration])