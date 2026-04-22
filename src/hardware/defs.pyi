"""Auto-generated type stub — Raccoon Toolchain (Tobias Madlberger / RaccoonOS Team)"""

from raccoon import AnalogSensor
from raccoon import DigitalSensor
from raccoon import IMU as Imu
from raccoon import Motor
from raccoon.step.servo.preset import ServoPreset, _PresetPosition
from typing import List


class Defs:
    imu: Imu
    button: DigitalSensor
    front_left_motor: Motor
    front_right_motor: Motor
    rear_left_motor: Motor
    rear_right_motor: Motor
    analog_sensors: List[AnalogSensor]
