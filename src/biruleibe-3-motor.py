


from ev3dev2.sensor import *
from ev3dev.ev3 import *
from time import sleep

velo_rot=500
us = UltrasonicSensor('in1')
us1 = UltrasonicSensor('in2')
ts = TouchSensor('in3')
units = us.units
# reports 'cm' even though the sensor measures 'mm'

mA = LargeMotor(OUTPUT_A)
mB = LargeMotor(OUTPUT_B)
mC = LargeMotor(OUTPUT_C)
while True:
        while not ts.value():
                print("Waiting")
        Sound.beep()
        sleep(5)
        while not ts.value():
                distance = us.value()/10  # convert mm to cm
                distance1 = us1.value()/10  # convert mm to cm
                print("This is ONE" + str(distance) + " " + units)
                print("This is TWO" + str(distance1) + " " + units)
                if distance < 40 or distance1 < 40:
                        difference = distance  - distance1
                        if difference > 20: #check if distance(error) is more to the left or to the right
                                mA.run_forever(speed_sp=-500)
                                mB.run_forever(speed_sp=500)
                                mC.run_forever(speed_sp=500)
                                print("Turn LEFT")
                        elif difference < -20: 
                                mA.run_forever(speed_sp=500)
                                mB.run_forever(speed_sp=-500)
                                mC.run_forever(speed_sp=500)
                                print("Turn RIGHT")
                        else:
                                mA.run_forever(speed_sp=-900)
                                mB.run_forever(speed_sp=-900)
                                mC.run_forever(speed_sp=900)
                                print("Forwards")
                else:
                        mA.run_forever(speed_sp=500) 
                        mB.run_forever(speed_sp=-500)
                        mC.run_forever(speed_sp=500)
                        print("Searching")
                sleep(0.5)
        mA.run_forever(speed_sp=0) #stops everything. pretty sure this block can be improved
        mB.run_forever(speed_sp=0)
        mC.run_forever(speed_sp=0)


