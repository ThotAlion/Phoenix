import pygame
import zmq
import time

IP = '10.0.0.3'

c = zmq.Context()
s = c.socket(zmq.REQ)
s.connect('tcp://'+IP+':8080')

pygame.init()
pygame.joystick.init()

goon = True
req = {}
req["pad"] = [1000,1000,1000,1000,1000,1000,1000,1000]
while goon:
    pygame.event.get()
    j = pygame.joystick.Joystick(0)
    j.init()
    req["pad"][0] = int(1500+500*0.5*j.get_axis(4))
    req["pad"][1] = int(1500-500*0.5*j.get_axis(3))
    req["pad"][2] = int(1000-700*j.get_axis(2))
    req["pad"][3] = int(1500+1000*0.5*j.get_axis(0))
    for i in range(8):
        if req["pad"][i]<1010:
            req["pad"][i]=1000
        if req["pad"][i]>1990:
            req["pad"][i]=2000
    s.send_json(req)
    s.recv_json()
    time.sleep(0.01)