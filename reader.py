import csv


path = "csv/Sub_Amaya/ex01_2018.07.10_14.33.31.bp.csv"
with open(path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['TimeStamp'])