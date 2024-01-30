#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()

# Initialize motors and color sensor "S"
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

sensor_left = ColorSensor(Port.S1)
sensor_right = ColorSensor(Port.S4)

wheel_diameter = 51  # adjust this value based on your robot's wheel size
axle_track = 94     # adjust this value based on your robot's axle track

robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Global Variable
main_flag = True

robot.drive(180, 0)

# Main loop
while main_flag:
        color_value_left = sensor_left.color()
        color_value_right = sensor_right.color()
    
        if (sensor_left.color() == Color.WHITE) & (sensor_right.color() == Color.WHITE):
            robot.drive(190, 0)

        if (sensor_left.color() == Color.BLACK) & (sensor_right.color() == Color.WHITE):
            while sensor_left.color() == Color.BLACK:
                robot.drive(50, -90)
                
        if (sensor_left.color() == Color.WHITE) & (sensor_right.color() == Color.BLACK):
            while sensor_right.color() == Color.BLACK:
                robot.drive(155, 110)
          
        if (sensor_left.color() == Color.RED) | (sensor_right.color() == Color.RED):
            robot.brake()
            main_flag = False