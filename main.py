# main.py used in pyboard.
# Team: Grant Maoxu Liu Dwight
# Description: To test whether our servos work or not
# Create date: 3/15/2016   Last modified date: 3/16/2016
from pyb import Servo

# creat servo projects.
s1 = Servo(1)
s2 = Servo(2) 
s3 = Servo(3)

# Test servo 1 at pin X1 on the pyboard
s1.angle(45,2000) # move to 45 degrees in 2 seconds
pyb.delay(1000) # wait 1 second
s1.angle(-45,2000) # move to -45 degrees in 2 seconds
pyb.delay(1000) # wait 1 second
s1.angle(0,2000) # move to 0 degrees in 2 seconds
pyb.delay(1000) # wait 1 second

# Test servo 2 at pin X2 on the pyboard
s1.angle(45,2000) 
pyb.delay(1000) 
s1.angle(-45,2000)
pyb.delay(1000)
s1.angle(0,2000)
pyb.delay(1000)

# Test servo 3 at pin X3 on the pyboard
s1.angle(45,2000)
pyb.delay(1000)
s1.angle(-45,2000)
pyb.delay(1000)
s1.angle(0,2000)
pyb.delay(1000)
