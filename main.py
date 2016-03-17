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
s1.angle(-45,2000) # move to -45 degrees in 2 seconds
pyb.delay(1000)

# move to -60 degrees over 1.5 seconds
s1.angle(-60, 2000)

# speed up to a speed of 20 over 2 seconds
#s2.speed(20, 1000)

# wait 3 seconds then stop servo
pyb.delay(3000)
#s2.speed(0)