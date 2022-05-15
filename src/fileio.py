import csv
from pathlib import Path


def write_csv(data, name):
    output_path = Path(name)
    with open(Path.cwd() / output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for item in data:
            writer.writerow([item])


def load_csv(name):
    csvpath = Path(name)
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Read the CSV data
        for row in csvreader:
            data.append(row[0])
    return data