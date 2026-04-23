"""Auto-generated type stub — Raccoon Toolchain (Tobias Madlberger / RaccoonOS Team)"""

from raccoon import AnalogSensor
from raccoon import DigitalSensor
from raccoon import IMU as Imu
from raccoon import IRSensor
from raccoon import Motor
from raccoon.step.servo.preset import ServoPreset, _PresetPosition
from typing import List


class _ArmServoPreset(ServoPreset):
    up: _PresetPosition
    down: _PresetPosition

    @property
    def device(self) -> "Servo": ...


class _ClawServoPreset(ServoPreset):
    open: _PresetPosition
    closed: _PresetPosition

    @property
    def device(self) -> "Servo": ...


class Defs:
    imu: Imu
    button: DigitalSensor
    front_left_ir_sensor: IRSensor
    front_right_ir_sensor: IRSensor
    rear_left_ir_sensor: IRSensor
    rear_right_ir_sensor: IRSensor
    front_left_motor: Motor
    front_right_motor: Motor
    rear_left_motor: Motor
    rear_right_motor: Motor
    arm_servo: _ArmServoPreset
    claw_servo: _ClawServoPreset
    analog_sensors: List[AnalogSensor]
