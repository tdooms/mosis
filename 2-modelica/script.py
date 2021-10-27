import csv
import os

os.chdir("/home/thomas/brol/PRT_PID_system")
os.system("./PRT_PID_system")
results_file = "PRT_PID_system_res.csv"

with open(results_file, newline='') as file:
    reader = csv.DictReader(file)
    print(max(abs(float(row['customPlant.x_psgr'])) for row in reader))
