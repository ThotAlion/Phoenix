#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Quaternion,Twist
import tf
from pyMultiwii import MultiWii

rospy.init_node('drone')

rate = rospy.Rate(10)
q = Quaternion()
cmd = Twist()
channels = [1000]*8
drone = MultiWii("/dev/ttyUSB0")
mode = 'att'
att = None
vbat = None

def send_command(msg):
    global channels
    channels[0] = 1500+500*msg.linear.y
    channels[1] = 1500+500*msg.linear.x
    channels[2] = 1000+1000*msg.linear.z
    channels[3] = 1500+500*msg.angular.z
    channels[4] = 1000
    channels[5] = 1000
    channels[6] = 1000
    channels[7] = 1000



pub_pose = rospy.Publisher('pose',Quaternion,queue_size=1)
sub_cmd = rospy.Subscriber('cmd',Twist,send_command)

while not rospy.is_shutdown():
    if mode == 'att':
        # get Euler angles
        att = drone.getData(MultiWii.ATTITUDE)
        mode = 'bat'
    elif mode == 'bat':
        vbat = drone.getData(MultiWii.ANALOG)
        mode = 'cmd'
    elif mode == 'cmd':
        drone.sendCMD(16,MultiWii.SET_RAW_RC,channels)
        mode = 'att'
    else:
        print 'mode '+mode+' unknown.'
    if not att is None:
        temp = tf.transformations.quaternion_from_euler(att['angx'],att['angy'],att['heading'])
        # publish
        q.x = temp[0]
        q.y = temp[1]
        q.z = temp[2]
        q.w = temp[3]
        pub_pose.publish(q)
    
    rate.sleep()
    