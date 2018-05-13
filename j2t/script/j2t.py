#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

def notZero(n1, n2):
	if (n1 == n2) & (n2 == 0.0):
		return 0.0
	elif abs(n1) > abs(n2):
		return n1
	else:
		return n2

def callback(data):
	rospy.loginfo(rospy.get_name() + '{}'.format(data.axes))
	msg = Twist()
	msg.linear.x = notZero(data.axes[5], data.axes[1]) / 3 
	msg.angular.z = notZero(data.axes[4], data.axes[0])
	pub.publish(msg)

def listener():
	global pub
	rospy.init_node('joy2twist', anonymous = True)
	rospy.Subscriber("/joy", Joy, callback)
	pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size = 10)
	rospy.spin()

if __name__ == '__main__':
	listener()

