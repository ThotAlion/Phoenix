# Phoenix
Airborne and hive code for Phoenix dance project

# main remarks
As far as possible, all is in Python2.7 language

# Architecture
## The drone folder
contains the embedded code for the raspberry pi on the drone 
(empty for the moment)
## The hive folder
contains the code on the master computer Windows 10 which has high CPU.
(empty for the moment)
## The pan-tilt folder
contains the test bench of fiducial pose estimation
This code operates a pan-tilt turret with a Logitech c525 webcam (http://www.logitech.fr/fr-fr/product/hd-webcam-c525). The objective is to center an aruco marker with this turret and measure the relative position in centimeters.

## The test_opencv folder contains some simple algorithms with open cv

# What to install on Raspberry Pi 3 on the drone
- get a clean image of Raspbian Jessie Lite (no desktop)
- sudo raspi-config to extend the file system, make the boot after network connexion
- Config the wifi : sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
- add in this file

network={
  ssid="ssid of the wifi"
  psk="password of the wifi"
}

- sudo apt-get install git (for importing this code)
- sudo apt-get install ipython (the console environment for python)

# What to install on the "hive" computer (Windows 10)
- Install python(x,y) distrib : http://python-xy.github.io/

# Major links
ARUCO main page : http://www.uco.es/investiga/grupos/ava/node/26
ARUCO python binding : https://github.com/fehlfarbe/python-aruco
