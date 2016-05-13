# Phoenix
Airborne and hive code for Phoenix dance project

# main remarks
As far as possible, all is in Python2.7 language

# Architecture
## The drone folder
contains the embedded code for the raspberry pi 2 on the drone

## The hive folder
contains the code on the master computer Windows 10 which has high CPU.

## The pan-tilt folder
contains the test bench of fiducial pose estimation.

This code operates a pan-tilt turret with a Logitech c525 webcam (http://www.logitech.fr/fr-fr/product/hd-webcam-c525). The objective is to center an aruco marker with this turret and measure the relative position in centimeters.

## The test_opencv folder
contains some simple algorithms with open cv

# What to install on Raspberry Pi 2 on the drone
- get a clean image of Ubuntu 14.02 http://www.finnie.org/software/raspberrypi/2015-04-06-ubuntu-trusty.zip
- connect on board with a screen and a keyboard
- login : ubuntu, pass : ubuntu
- sudo loadkeys fr (to configure azerty keyboard)
- sudo fdisk /dev/mmcblk0 (d,2)(n,p,2,enter,enter)(w) (extend filesystem to the whole SD card)
- reboot
- sudo loadkeys fr
- sudo resize2fs /dev/mmcblk0p2
- sudo apt-get update
- sudo apt-get install linux-firmware (wifi drivers)
- sudo apt-get install dphys-swapfile (to add swap partition)
- sudo apt-get install openssh-server (to launch the SSH server for remote access)
- reboot

The Ubuntu system is now configured at the minimal configuration

Install the Desktop
- sudo apt-get upgrade (to upgrade all the packages... can take a long time)
- sudo apt-get install lubuntu-desktop (to install the desktop environment)
- sudo reboot
 
Install ROS Indigo - http://wiki.ros.org/indigo/Installation/Ubuntu
- Setup the source list following this link : https://help.ubuntu.com/community/Repositories/Ubuntu
- sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
- sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 0xB01FA116
- sudo reboot
- sudo apt-get update
- sudo apt-get install ros-indigo-desktop
- sudo rosdep init
- rosdep update
- echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
- source ~/.bashrc
- source /opt/ros/indigo/setup.bash
- sudo apt-get install python-rosinstall

ROS is installed

# What to install on the "hive" computer (Windows 10)
- Install python(x,y) distrib : http://python-xy.github.io/
- TBC

# Major links
- ARUCO main page : http://www.uco.es/investiga/grupos/ava/node/26
- ARUCO python binding : https://github.com/fehlfarbe/python-aruco
- TBC
