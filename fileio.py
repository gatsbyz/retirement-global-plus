

import csv
from pathlib import Path


def write_csv(data):
    output_path = Path("user_data.csv")
    with open(Path.cwd() / output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for item in data:
            writer.writerow([item])


def load_csv():
    csvpath = Path("user_data.csv")
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Read the CSV data
        for row in csvreader:
            data.append(row[0])
    return data