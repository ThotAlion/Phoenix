import pypot.robot
import cv2
import aruco
import time
import numpy as np

json_name = "pantilt.json"
robot = pypot.robot.from_json(json_name)
cam = cv2.VideoCapture(0)
camPar = aruco.CameraParameters()
camPar.readFromXMLFile('cam.yml')
det = aruco.MarkerDetector()



robot.z.compliant = False
robot.z.goal_position = 0
robot.y.compliant = False
robot.y.goal_position = 0

kz=0.01
ky=-0.01

while True:
    t0 = time.time()
    ret, pureframe = cam.read()
    #frame = cv2.resize(pureframe,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    frame = pureframe
    print frame.shape
    m = det.detect(frame,camPar,7.5)
    t1 = time.time()
    if len(m)==1:
        c=m[0].getCenter()
        erz = pureframe.shape[0]/2.0 - c[0]
        ery = pureframe.shape[1]/2.0 - c[1]
        # print "erz"
        # print erz
        # print "ery"
        # print ery
        robot.z.compliant = False
        robot.y.compliant = False
        robot.z.goal_position = robot.z.present_position+kz*erz
        robot.y.goal_position = robot.y.present_position+ky*ery
    else:
        robot.z.compliant = True
        robot.y.compliant = True
    # cv2.imshow('frame',pureframe)
    # cv2.waitKey(5)
    #print t1-t0


