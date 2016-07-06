import zmq
from geometry_msgs.msg import Twist

IP = '0.0.0.0'
port = '8080'

rospy.init_node('drone')

pub_cmd = rospy.Publisher('cmd',Twist,queue_size=1)

c = zmq.Context()
s = c.socket(zmq.REP)
s.bind("tcp://"+IP+":"+port)

# this node publishes the cmd given by the user connected to another computer with a control device.

cmd = Twist()

while not rospy.is_shutdown():
    reply = s.recv_json()
    if reply.has_key("pad"):


pub_pose.publish(cmd)