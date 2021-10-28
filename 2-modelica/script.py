import csv
import os
from typing import Optional
from dataclasses import dataclass
import numpy as np

PATH = "PRT_PID_system_res.csv"
CMD = "./PRT_PID_system"

# What are you doing STEP_SIZE?
# Step size is defined in terms of span(x_range) * STEP_SIZE
START_STEP_SIZE = 0.1
EPS = 1.0000001

KP_RANGE = (300, 350)
KI_RANGE = (0.5, 1.5)
KD_RANGE = (-20, 70)

KP_START = KP_RANGE[0] + (KP_RANGE[1] - KP_RANGE[0]) / 2
KI_START = KI_RANGE[0] + (KI_RANGE[1] - KI_RANGE[0]) / 2
KD_START = KD_RANGE[0] + (KD_RANGE[1] - KD_RANGE[0]) / 2


@dataclass
class Point:
    kp: float
    ki: float
    kd: float


def print_headers():
    os.system(CMD)
    file = open(PATH, newline='')
    print(csv.DictReader(file).fieldnames)


def least_squares_speed(rows) -> Optional[float]:
    accumulator = 0
    for row in rows:
        x_psgr = float(row['customPlant.x_psgr'])
        v_trolley = float(row['customPlant.v_trolley'])
        v_ideal = float(row['lookUp.v_ideal'])

        if x_psgr > 0.35:
            return None

        accumulator += (v_trolley - v_ideal)**2
    return accumulator


def get_step(x_range, step_size):
    return (x_range[1] - x_range[0]) * step_size


# avoid the previous one?
def calc_neighbours(sample: Point, step_size):
    kp_o = get_step(KP_RANGE, step_size)
    ki_o = get_step(KI_RANGE, step_size)
    kd_o = get_step(KD_RANGE, step_size)

    return [
        Point(sample.kp + kp_o, sample.ki, sample.kd),
        Point(sample.kp - kp_o, sample.ki, sample.kd),
        Point(sample.kp, sample.ki + ki_o, sample.kd),
        Point(sample.kp, sample.ki - ki_o, sample.kd),
        Point(sample.kp, sample.ki, sample.kd + kd_o),
        Point(sample.kp, sample.ki, sample.kd - kd_o)
    ]


def hill_climb(start: Point, cost_fn):
    c_value = evaluate(start, cost_fn)
    c_sample = start
    c_size = START_STEP_SIZE
    c_step = 0

    while c_size > START_STEP_SIZE / 100:
        c_step += 1

        neighbours = calc_neighbours(c_sample, c_size)
        values = [evaluate(n, cost_fn) for n in neighbours]
        index = np.argmax(values)

        # we add an EPS to avoid bouncing back and forward the whole time
        if values[index] > c_value + EPS:
            c_sample = neighbours[index]
            c_value = values[index]
        else:
            c_size = c_size / 2

        print("step", c_step, ":", c_sample, "->", c_value)


def evaluate(sample: Point, cost_fn) -> Optional[float]:
    # Very cool conversions
    cmd = f"{CMD} -override pid.Ti={sample.kp / sample.ki},pid.Td={sample.kd / sample.kp},pid.k={sample.kp} >/dev/null 2>&1"
    os.system()

    file = open(PATH, newline='')
    rows = csv.DictReader(file)
    value = cost_fn(rows)
    print("sample", sample, ":", value)
    return value


# ------- main code ------- #
os.chdir("/home/thomas/brol/PRT_PID_system")
hill_climb(Point(KP_START, KI_START, KD_START), least_squares_speed)
# print_headers()
