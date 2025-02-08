import csv
from datetime import datetime

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def log_time(self, project_name, start_time, end_time):
        duration = (end_time - start_time).total_seconds() / 60
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().date(), project_name, start_time.strftime("%H:%M"), end_time.strftime("%H:%M"), duration])