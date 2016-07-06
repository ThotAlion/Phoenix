import pygame
import zmq
import time

IP = '10.0.0.2'

c = zmq.Context()
s = c.socket(zmq.REQ)
s.connect('tcp://'+IP+':8080')

pygame.init()
pygame.joystick.init()

goon = True
req = {}
req["pad"] = {}
while goon:
    t0 = time.clock()
    pygame.event.get()
    j = pygame.joystick.Joystick(0)
    j.init()
    req["pad"]["stickPitch"] = j.get_axis(1)
    req["pad"]["stickRoll"] = j.get_axis(0)
    req["pad"]["stickYaw"] = j.get_axis(3)
    req["pad"]["thrust"] = j.get_axis(2)
    req["pad"]["stickPal"] = j.get_axis(3)
    req["pad"]["stickTrim"] = j.get_hat(0)
    req["pad"]["Fire"] = j.get_button(0)
    req["pad"]["L1"] = j.get_button(1)
    req["pad"]["L3"] = j.get_button(3)
    req["pad"]["R3"] = j.get_button(2)
    req["pad"]["T5"] = j.get_button(4)
    req["pad"]["T6"] = j.get_button(5)
    req["pad"]["T7"] = j.get_button(6)
    req["pad"]["T8"] = j.get_button(7)
    req["pad"]["T9"] = j.get_button(8)
    req["pad"]["T10"] = j.get_button(9)
    req["pad"]["SE"] = j.get_button(10)
    req["pad"]["ST"] = j.get_button(11)
    s.send_json(req)
    a = s.recv_json()
    time.sleep(0.01)