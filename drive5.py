import Adafruit_PCA9685
import time
import curses
import threading

#screen = curses.initscr()
#curses.noecho()
#curses.cbreak()
#screen.keypad(True)

left_max = 600 #250
right_max = 200 #470
center = 340
max_speed = 320
min_speed =380
steer = center
speed = min_speed
jump = 1
second = 0.0

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
driveLoop = True
sec = 1
pwm.set_pwm(1,0,center)
time.sleep(1)
while sec > 0:
	#pwm.set_pwm(1, 0, center)
        pwm.set_pwm(2, 0, 375)
	time.sleep(1)
	print(sec)
	sec-=1

sec = 1
pwm.set_pwm(2,0,376)
pwm.set_pwm(1,0,220)
time.sleep(2)
#pwm.set_pwm(1,0,center)
#time.sleep(0.5)
#pwm.set_pwm(1,0,227)
#time.sleep(1.2)
pwm.set_pwm(1,0,center)
time.sleep(0.7)

while sec > 0:
	pwm.set_pwm(2,0,375)
	time.sleep(0.7)
	print(sec)
	sec-=1

pwm.set_pwm(2,0,380)
pwm.set_pwm(1,0, center)

