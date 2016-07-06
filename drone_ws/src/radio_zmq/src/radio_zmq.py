#!/usr/bin/env python

import zmq
import rospy
from geometry_msgs.msg import Twist

IP = '0.0.0.0'
port = '8000'

rospy.init_node('zmq')

pub_cmd = rospy.Publisher('cmd',Twist,queue_size=1)

c = zmq.Context()
s = c.socket(zmq.REP)
s.bind("tcp://"+IP+":"+port)

# this node publishes the cmd given by the user connected to another computer with a control device.

cmd = Twist()

while not rospy.is_shutdown():
    reply = s.recv_json()
    if reply.has_key("pad"):
        pad = reply["pad"]
        if pad["name"] == "Thrustmaster":
            cmd.linear.y = pad["stickRoll"]
            cmd.linear.x = pad["stickPitch"]
            cmd.linear.z = 0.5*(-pad["thrust"]+1.0)
            cmd.angular.z = pad["stickYaw"]
            pub_cmd.publish(cmd)
    s.send_json({})
            
            


