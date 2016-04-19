# main.py -- put your code here!
'''
main.py used in pyboard.
Team: Grant, Maoxu Liu, Dwight
Description: Demo for Steel Snake moving like a real snake
Create date: 3/15/2016   Last modified date: 3/30/2016
from pyb import Servo
'''


import pyb
from pyb import Pin
from pyb import Servo
from pyb import LED

l1=LED(1)
l2=LED(2)
l3=LED(3)
l4=LED(4)
# creat servo projects.
s1 = Servo(1)
s2 = Servo(2) 
s3 = Servo(3)
#s4 = Servo(4)
# go to straight line
'''
s1.angle(0,2000)
pyb.delay(1000)  
s2.angle(0,2000)
pyb.delay(1000)
s3.angle(0,2000)
pyb.delay(1000)


# Movement 1
s1.angle(-50,2000)
pyb.delay(2000)
s2.angle(-50,2000)
pyb.delay(2000)
s3.angle(-50,2000)
pyb.delay(2000)

 # wait for 3 seconds than do next demo movement

#Movement 2
s1.angle(50,2000)
pyb.delay(2000)
s2.angle(50,2000)
pyb.delay(2000)
s3.angle(50,2000)
pyb.delay(2000)

pyb.delay(4000)

# Movement 3: go back to straight line
s1.angle(0,2000)  
s2.angle(0,2000)
s3.angle(0,2000)


# led marks
l1.on()
pyb.delay(1500)
l1.off()

# Movement 4
s1.angle(-45,2000)
pyb.delay(1000)
s2.angle(45,2000)
pyb.delay(1000)
s3.angle(45,2000)
pyb.delay(1000)
# Movement 5
s2.angle(-45,1000)
s3.angle(-45,1000)
pyb.delay(1000)
s1.angle(45,2000)
pyb.delay(2000)
# Movement 6
s2.angle(-45,2000)
pyb.delay(2000)
s3.angle(-45,2000)
# Movement 7 :go back to straight.
s1.angle(-45,2000)
s2.angle(45,2000)
s3.angle(45,2000)


l1.on()
pyb.delay(1500)
l1.off()



for i in range(10):
	s1.angle(-30,1000)
	s2.angle(60,1000)
	s3.angle(-60,1000)
	pyb.delay(1000)
	s1.angle(30,1000)
	s2.angle(-60,1000)
	s3.angle(30,1000)
	pyb.delay(1000)

'''
# SHIT
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

# function definations ends

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
		endLight()
		#index=index+1
		#pyb.delay(2000)
		#pyb.delay(2000)