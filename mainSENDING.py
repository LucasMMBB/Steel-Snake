# main.py -- put your code here!
# main.py -- put your code here!
'''
main.py used in pyboard.
Author: Maoxu Liu
Team: Grant, Dwight
Version: 3 
Description: Demo for Steel Snake moving like a real snake and in this version
i added the function to use accelerometer to control snake movement.
Improvment: Detect the angle of pyboard by use of accelerometer and use this
angle as a parameter to control it.
Create date: 3/15/2016   Last modified date: 4/6/2016
'''


import pyb
from pyb import Pin
from pyb import Servo
from pyb import LED
from pyb import Accel

l1=LED(1)
l2=LED(2)
l3=LED(3)
l4=LED(4)
# creat servo projects.
s1 = Servo(1)
s2 = Servo(2) 
s3 = Servo(3)
# creat accelerometer
ax=Accel()
'''
# Date: 3/30/2016
# Movement 8: Here we added 3 switches to control device in different movement modes.
'''

'''    Define movement functions    '''

# Straight funciton
def straight():
	s1.angle(0,2000)
	pyb.delay(1000)  
	s2.angle(0,2000)
	pyb.delay(1000)
	s3.angle(0,2000)
	pyb.delay(2000)
# Left function
def left():
	s1.angle(-50,2000)
	pyb.delay(2000)
	s2.angle(-50,2000)
	pyb.delay(2000)
	s3.angle(-50,2000)
	pyb.delay(2000)
# Right function
def right():
	s1.angle(50,2000)
	pyb.delay(2000)
	s2.angle(50,2000)
	pyb.delay(2000)
	s3.angle(50,2000)
	pyb.delay(2000)
# Half square shape
def halSquleft():
	s1.angle(-45,2000)
	pyb.delay(1000)
	s2.angle(45,2000)
	pyb.delay(1000)
	s3.angle(45,2000)
	pyb.delay(1000)
def halSquRight():
	s2.angle(-45,1000)
	s3.angle(-45,1000)
	pyb.delay(1000)
	s1.angle(45,2000)
	pyb.delay(2000)
# slow snake:
def slowsnake():
	for i in range(10):
		s1.angle(-30,1500)
		s2.angle(60,1500)
		s3.angle(-60,1500)
		pyb.delay(1000)
		s1.angle(30,1500)
		s2.angle(-60,1500)
		s3.angle(30,1500)
		pyb.delay(1000)
def fastsnake():
	for i in range(10):
		s1.angle(-30,500)
		s2.angle(60,500)
		s3.angle(-60,500)
		pyb.delay(1000)
		s1.angle(30,500)
		s2.angle(-60,500)
		s3.angle(30,500)
		pyb.delay(1000)
		
def endLight():
	for i in range(5):
		l1.toggle()
		pyb.delay(200)
		l2.toggle()
		pyb.delay(200)
		l3.toggle()
		pyb.delay(200)
		l4.toggle()
		pyb.delay(200)
	l1.off()
	l2.off()
	l3.off()
	l4.off()

def XangleControl():
	l1.on()
	l2.on()
	l3.on()
	l4.on()
	for i in range(200):
		s3.angle(3*ax.x())
		pyb.delay(250)
	l1.off()
	l2.off()
	l3.off()
	l4.off()
def XControlAll():
	l1.on()
	l2.on()
	l3.on()
	l4.on()
	for i in range(20):
		s1.angle(ax.x())
		s2.angle(2*ax.x())
		s3.angle(3*ax.x())
		pyb.delay(500)
	l1.off()
	l2.off()
	l3.off()
	l4.off()
# function definations ends
'''
# Define input pins with PULL UP mode
Pinsw1 = Pin('Y6', Pin.IN,Pin.PULL_UP)
Pinsw2 = Pin('Y7', Pin.IN,Pin.PULL_UP)
Pinsw3 = Pin('Y8', Pin.IN,Pin.PULL_UP)
#swArr = [Pinsw1.value(),Pinsw2.value(),Pinsw3.value()];
index = 0
while (index==0):
	swArr = [Pinsw1.value(),Pinsw2.value(),Pinsw3.value()];
	if(swArr==[1,1,1]):
		straight()
		XControlAll()
		# Don't move
		#index=index+1
		#pyb.delay(2000)
		endLight()
	elif(swArr==[0,0,1]):
		# Go to straight
		straight()
		halSquleft()
		halSquRight()
		endLight()
		#index=index+1
		#pyb.delay(2000)
	elif(swArr==[0,1,0]):
		# Move to left
		left()
		endLight()
		#index=index+1
		#pyb.delay(2000)
	elif(swArr==[0,1,1]):#test case
		# Move to right
		right()
		endLight()
		#index=index+1
		#pyb.delay(2000)
	elif(swArr==[1,0,0]):
		# Slow snake
		halSquleft()
		slowsnake()
		endLight()
		#index=index+1
		#pyb.delay(2000)
	elif(swArr==[1,0,1]):# test case
		# Half square shape
		halSquRight()
		fastsnake()
		endLight
		#index=index+1
		#pyb.delay(2000)
	elif(swArr==[1,1,0]):#test case
		# Half square shape
		halSquRight()
		slowsnake()
		endLight()
		#index=index+1
		#pyb.delay(2000)
	else:
		# [0,0,0]
		# Fast snake
		fastsnake()
		straight()
		XangleControl()
		#index=index+1
		#pyb.delay(2000)
		#pyb.delay(2000)
		
'''