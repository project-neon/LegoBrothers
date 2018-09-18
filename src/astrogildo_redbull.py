#!/usr/bin/env python3
from ev3dev2.sensor import *
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.button import *
from ev3dev.ev3 import *
from time import sleep

#define variables
butt = Button()                                                                             ### eheheheh
mA = LargeMotor(OUTPUT_A)		#mA and mB are right and left motors, for locomotion
mB = LargeMotor(OUTPUT_B)
mC = LargeMotor(OUTPUT_C) 		#mC and mD are the arms' motors
mD = LargeMotor(OUTPUT_D)
velo_rot=500
us = UltrasonicSensor('in1')
us1 = UltrasonicSensor('in2')
units = us1.units

while True:
	while not butt.any(): 		#	#### wait for button press to begin
		print("Esperando")


	sleep(5) 						#### standard wait time for robot competitions

	mA.run_forever(speed_sp=750)	#### this block moves the robot backwards,
	mB.run_forever(speed_sp=750)	#### so that he can drop his arms
	sleep(0.5)
	mA.run_forever(speed_sp=0)		#### it then returns the motors to normal,
	mB.run_forever(speed_sp=0) 		#### so that it does not conflict with main behaviour program
	sleep(0.1)

	while not butt.any():			#### the main behaviour program will run untill any button is
									#### pressed by the user

		mC.run_forever(speed_sp=-900)	
		mD.run_forever(speed_sp=-900)

		distance = us.value()/10  		# convert mm to cm
		distance1 = us1.value()/10  	# convert mm to cm
		print("This is sensor ONE " + str(distance) + " " + units)
		print("This is sensor TWO " + str(distance1) + " " + units)

		if distance < 40 or distance1 < 40:
			difference = distance  - distance1
			if difference > 20: 		#check if distance(error) is more to the left or to the right
				mA.run_forever(speed_sp=-500)
				mB.run_forever(speed_sp=500)
				print("Turn LEFT")
			elif difference < -20: 		
				mA.run_forever(speed_sp=500)
				mB.run_forever(speed_sp=-500)
				print("Turn RIGHT")
			else:
				mA.run_forever(speed_sp=-800)
				mB.run_forever(speed_sp=-800)
				print("Forward")
		else:
			mA.run_forever(speed_sp=500)
			mB.run_forever(speed_sp=-500)
			print("Search")
		sleep(0.5)
	mA.run_forever(speed_sp=0)
	mB.run_forever(speed_sp=0)
	mC.run_forever(speed_sp=0)
	mD.run_forever(speed_sp=0)
	print("Stop")
