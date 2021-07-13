#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool
import RPi.GPIO as GPIO

LED_GPIO = 20
GPIO.setwarnings(False)

def button_state_callback(msg):
    GPIO.output(LED_GPIO, msg.data)

if __name__ == '__main__':
    rospy.init_node('led_actuator')
    print('Start!!!')

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_GPIO, GPIO.OUT)

    rospy.Subscriber('button_state', Bool, button_state_callback)

    rospy.spin()

    GPIO.cleanup()
