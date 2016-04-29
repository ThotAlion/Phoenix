import cv2

cam = cv2.VideoCapture(0)

for i in range(10):
    raw_input()
    ret,img = cam.read()
    cv2.imwrite('data/left'+str(i)+'.jpg',img)
    print i