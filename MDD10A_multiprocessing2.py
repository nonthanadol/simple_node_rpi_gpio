import sys, tty, termios, os
import MDD10A as HBridge
import multiprocessing

speedleft = 0 #22,17
speedright = 0 #23,18

start_setuv = multiprocessing.Process(target=HBridge.setuv,args=[1])
stop_setuv = multiprocessing.Process(target=HBridge.setuv,args=[0])

# Instructions for when the user has an interface
print("w/s: direction")
print("a/d: steering")
print("q: stops the motors")
print("p: print motor speed (L/R)")
print('r : on uvc')
print('f : off uvc')
print("x: exit")
HBridge.LEDstart()

# The catch method can determine which key has been pressed
# by the user on the keyboard.
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Infinite loop
# The loop will not end until the user presses the
# exit key 'X' or the program crashes...

def printscreen():
	# Print the motor speed just for interest
	os.system('clear')
	print("w/s: direction")
	print("a/d: steering")
	print("q: stops the motors")
	print("x: exit")
	print("========== Speed Control ==========")
	print "left motor:  ", speedleft
	print "right motor: ", speedright

while True:
    # Keyboard character retrieval method. This method will save
    # the pressed key into the variable char
	char = getch()


	
	# The car will drive forward when the "w" key is pressed
	if(char == "w"):
	
		# synchronize after a turning the motor speed
			
		# if speedleft > speedright:
			# speedleft = speedright
		
		# if speedright > speedleft:
			# speedright = speedleft
				
		# accelerate the RaPi car
		speedleft = speedleft + 0.1
		speedright = speedright + 0.1

		if speedleft > 1:
			speedleft = 1
		if speedright > 1:
			speedright = 1
		
		HBridge.setMotorLeft(speedleft)
		HBridge.setMotorRight(speedright)
		printscreen()

    # The car will reverse when the "s" key is pressed
	if(char == "s"):
	
		# synchronize after a turning the motor speed
			
		# if speedleft > speedright:
			# speedleft = speedright
			
		# if speedright > speedleft:
			# speedright = speedleft
			
		# slow down the RaPi car
		speedleft = speedleft - 0.1
		speedright = speedright - 0.1

		if speedleft < -1:
			speedleft = -1
		if speedright < -1:
			speedright = -1
		
		HBridge.setMotorLeft(speedleft)
		HBridge.setMotorRight(speedright)
		printscreen()

    # Stop the motors
	if(char == "q"):
		speedleft = 0
		speedright = 0
		HBridge.setMotorLeft(speedleft)
		HBridge.setMotorRight(speedright)
		printscreen()

    # The "d" key will toggle the steering right
	if(char == "d"):		
		#if speedright > speedleft:
		speedright = speedright - 0.1
		speedleft = speedleft + 0.1
		
		if speedright < -1:
			speedright = -1
		
		if speedleft > 1:
			speedleft = 1
		
		HBridge.setMotorLeft(speedleft)
		HBridge.setMotorRight(speedright)
		printscreen()
		
    # The "a" key will toggle the steering left
	if(char == "a"):
		#if speedleft > speedright:
		speedleft = speedleft - 0.1
		speedright = speedright + 0.1
			
		if speedleft < -1:
			speedleft = -1
		
		if speedright > 1:
			speedright = 1
		
		HBridge.setMotorLeft(speedleft)
		HBridge.setMotorRight(speedright)
		printscreen()
	
	if(char == 'r'):
        start_setuv.start()
		printscreen()

	if(char == 'f'):
		stop_setuv.start()
		printscreen()

	# The "x" key will break the loop and exit the program
	if(char == "x"):
		HBridge.setMotorLeft(0)
		HBridge.setMotorRight(0)
		HBridge.exit()
		print("Program Ended")
		break

	
    # The keyboard character variable char has to be set blank. We need
	# to set it blank to save the next key pressed by the user
	char = ""
# End
