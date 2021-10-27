import csv
import os
from typing import Optional

PATH = "PRT_PID_system_res.csv"
CMD = "./PRT_PID_system"

kp_range = (300, 350)
ki_range = (0.5, 1.5)
kd_range = (-20, 70)


def default_print():
    os.system(CMD)
    print(open(PATH, newline='').read())


def least_squares_speed(rows) -> Optional[float]:
    # check if failed
    if max(row['customPlant.x_psgr'] for row in rows) > 0.35:
        return None

    return sum(row['customPlant.v_trolley'] ** 2 for row in rows)


def evaluate(kp, ki, kd, cost_fn) -> Optional[float]:
    os.system(CMD + " -overide")
    file = open(PATH, newline='')
    rows = csv.DictReader(file)
    return cost_fn(rows)


# ------- main code ------- #
os.chdir("/home/thomas/brol/PRT_PID_system")
default_print()
