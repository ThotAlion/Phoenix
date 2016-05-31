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

This code operates a pan-tilt turret with a Logitech [c525 webcam](http://www.logitech.fr/fr-fr/product/hd-webcam-c525). The objective is to center an aruco marker with this turret and measure the relative position in centimeters.

## The test_opencv folder
contains some simple algorithms with open cv

# How to install ROS Jade on Raspberry Pi 3 (Jessie)

If any issue, please refer to :
- https://forum.poppy-project.org/t/raspberry-pi-3-experiments/2456/6
- http://wiki.ros.org/jade/Installation/Source
- http://wiki.ros.org/jade/Installation/Ubuntu#jade.2BAC8-Installation.2BAC8-Sources.Setup_your_sources.list

## install Jessie Lite on Raspberry Pi 3
- get a [clean image of Jessie Lite for Raspberry Pi 3](https://downloads.raspberrypi.org/raspbian_lite_latest)
- Flash it on a micro-SD card (with [Win32diskimager](https://sourceforge.net/projects/win32diskimager/) on Windows)
- Insert the SD in the Raspberry Pi and plug Ethernet and Power
- Login in SSH mode login : pi, pass : raspberry
```sudo raspi-config```
- Expand File system
- boot without login
- choose slow boot to be sure to have network access
- activate raspberry pi camera
- ```sudo nano /etc/dphys-swapfile```
- Configure so that ```CONF_SWAPSIZE=1024``` (the swap size must be enlarged to allow ROS installation)
- ```sudo reboot```

## Install ROS Jade
- ```sudo nano /etc/apt/sources.list```
- add the following line to this file : ```deb http://packages.ros.org/ros/ubuntu jessie main```
- ```sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 0xB01FA116```
- ```sudo apt-get update```
- ```sudo apt-get upgrade```
- ```sudo apt-get install python-rosdep```
- ```sudo apt-get install python-rosinstall-generator```
- ```sudo apt-get install python-wstool```
- ```sudo apt-get install python-rosinstall```
- ```sudo apt-get install build-essential```
- ```sudo rosdep init```
- ```rosdep update```
- ```mkdir ros_catkin_ws```
- ```cd ros_catkin_ws/```
- For this project, I decided to install a restriction of ROS linked with perception and visual processing. With the line below, you can adapt according to your needs.
- ```rosinstall_generator robot --rosdistro jade --deps --wet-only --tar > jade-robot-wet.rosinstall```
- ```wstool init -j8 src jade-robot-wet.rosinstall```
- ```rosdep install --from-paths src --ignore-src --rosdistro jade -y```
- ```sudo nano src/robot_model/collada_urdf/src/collada_urdf.cpp```
- add the following lines :

```
#ifdef __arm__                 // fix for ARM build
#include <strings.h>
bool Assimp::IOSystem::ComparePaths(const char *p1, const char *p2) const
{
   return !::strcasecmp(p1, p2);
}
#  endif
```
- ```./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release```
- ```nano ~/.bashrc```
- add to this file : ```source ~/ros_catkin_ws/install_isolated/setup.bash```

## Install specific tools
- ```sudo apt-get install python-pip```
- ```sudo apt-get install ipython```
- ```sudo pip install picamera```

## Wifi configuration (WIFI N)
For the moment, let's install a classical WIFI 802.11N dongle as [EDIMAX-EW-7811UN](https://www.amazon.fr/Edimax-EW-7811UN-Nano-Adaptateur-sans/dp/B003MTTJOY) Or use the integrated Wifi of the RPI3
- connect the WIFI dongle to the card
- Edit the file /etc/network/interfaces and add the following lines :
```
allow-hotplug wlan0
iface wlan0 inet dhcp
  wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```
- Edit the file /etc/wpa_supplicant/wpa_supplicant.conf which must be like this :
```
ctrl_interface=/var/run/wpa_supplicant
network={
    ssid="XXXXXXXXXX"
    psk="xxxxxxx"
}
```
- sudo reboot
The Pi shall connect to your WIFI. The Pi is now able to live completely wireless.

## Wifi configuration (WIFI AC)
For further experiments, we will use cristal clear Wifi 802.11ac with the dongle :
[EDIMAX-EW-7811UTC](https://www.amazon.fr/Edimax-EW-7811UTC-Adaptateur-Wi-Fi-Noir/dp/B00GMY40T0/ref=sr_1_5?s=computers&ie=UTF8&qid=1464621556&sr=1-5)
The process to install on Jessie : 
```
1. Connect the Pi to Ethernet.
2. Update:
sudo apt-get update
sudo apt-get upgrade

3. Check OS version:
uname -a

Mine was 4.1.7-v7+ #817
4. So the next step is (do this is a folder in your home directory):
wget https://dl.dropboxusercontent.com/u/80256631/8812au-4.1.7-v7-817.tar.gz

You have to update this according to your OS version (hopefully there is a build there).
5. Next:
tar xzf 8812au-4.1.7-v7-817.tar.gz

6. Next:
./install.sh

7. Next:
sudo reboo

Then check that module was installed with:
lsmod
```

# What to install on the "hive" computer (Windows 10)
- Install python(x,y) distrib : http://python-xy.github.io/
- TBC

# Major links
- ARUCO main page : http://www.uco.es/investiga/grupos/ava/node/26
- ARUCO python binding : https://github.com/fehlfarbe/python-aruco
- TBC
