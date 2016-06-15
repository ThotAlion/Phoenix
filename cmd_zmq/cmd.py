import zmq
from pyMultiwii import MultiWii
import time

IP = '0.0.0.0'
port = '8080'

c = zmq.Context()
s = c.socket(zmq.REP)
s.bind("tcp://"+IP+":"+port)

drone = MultiWii("/dev/ttyUSB0")
drone_state={}
goon = True
while goon:
    reply = s.recv_json()
    if reply.has_key("pad"):
        att = drone.getData(MultiWii.ATTITUDE)
        mot = drone.getData(MultiWii.MOTOR)
        vbat = drone.getData(MultiWii.ANALOG)
        if not att is None:
            drone_state["angx"] = float(att['angx'])
            drone_state["angy"] = float(att['angy'])
            drone_state["heading"] = float(att['heading'])
         
        if not mot is None:
            drone_state["m1"] = float(mot['m1'])
            drone_state["m2"] = float(mot['m2'])
            drone_state["m3"] = float(mot['m3'])
            drone_state["m4"] = float(mot['m4'])
        if not vbat is None:
            drone_state["vbat"] = vbat
        drone.sendCMD(16,MultiWii.SET_RAW_RC,reply["pad"])
    s.send_json(drone_state)