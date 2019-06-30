import Adafruit_PCA9685
import time
import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

left_max = 600 #250
right_max = 170 #470
center = 350
max_speed = 320
min_speed =380
steer = center
speed = min_speed
jump = 1
second = 0.0

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

driveLoop = True


try:
        while driveLoop:

        	char = screen.getch()

        	if (char == ord('a')):
        		steer += jump*30
        		if (steer > left_max):
        			steer = left_max
        		pwm.set_pwm(1, 0, steer)
        		time.sleep(0.01)
        		print("left turn: ", steer)

        	if (char == ord('d')):
        		steer -= jump*30
        		if (steer < right_max):
        			steer = right_max
        		pwm.set_pwm(1, 0, steer) 
        		time.sleep(0.01)
        		print("right turn: ", steer)

        	if (char == ord('w')):
        		speed -= jump
        		if (speed < max_speed):
        			speed = max_speed
        		pwm.set_pwm(2, 0, speed)
        		time.sleep(0.01)
        		print("forward: ", speed)

        	if (char == ord('s')):
        		speed += jump
        		if (speed > min_speed):
        			speed = min_speed
        		pwm.set_pwm(2, 0, speed)
        		time.sleep(0.01)
        		print("slow down: ", speed)

        	if (char == ord('x')):
        		speed = min_speed
        		pwm.set_pwm(2, 0, min_speed)
        		time.sleep(0.01)
        		steer = center
        		pwm.set_pwm(1, 0, center) 
        		time.sleep(0.01)
        		print("STOPPED!! Steering: ", steer, " Speed: ", speed)

        	if (char == ord('q')):
        		pwm.set_pwm(2, 0, min_speed)
        		time.sleep(0.01)
        		pwm.set_pwm(1, 0, center) 
        		time.sleep(0.01)
        		print("quit")
        		driveLoop = False

        	if char == ord('e'):
        		break

finally:
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()
