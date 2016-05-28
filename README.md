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
- Configure so that ```CONF_SWAPSIZE=1024``` (the swap size must be enlarged to allow ROS installation
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


# How to install ROS on Raspberry Pi 2 on the drone
Instead of having a "megascript" installing all, I describe the whole process of installation with explanations so that if you have an issue, you can understand easily and repair.
## Install Ubuntu Trusty 14.04
- get a [clean image of Ubuntu 14.02](http://www.finnie.org/software/raspberrypi/2015-04-06-ubuntu-trusty.zip)
- Flash it on a micro-SD card (with [Win32diskimager](https://sourceforge.net/projects/win32diskimager/) on Windows)
- connect on board with a screen, a keyboard and an Ethernet connection to the web
- login : ubuntu, pass : ubuntu
- sudo loadkeys fr (to configure azerty keyboard)
- sudo fdisk /dev/mmcblk0 (d,2)(n,p,2,enter,enter)(w) (extend filesystem to the whole SD card)
- reboot
- sudo loadkeys fr (to configure azerty keyboard)
- sudo resize2fs /dev/mmcblk0p2
- sudo apt-get update
- sudo apt-get install linux-firmware (wifi drivers)
- sudo apt-get install dphys-swapfile (to add swap partition)
- sudo apt-get install openssh-server (to launch the SSH server for remote access)
- reboot

The Ubuntu system is now configured at the minimal configuration and SSH remote access

## Install the Desktop environment
- sudo loadkeys fr (to configure azerty keyboard)
- sudo apt-get upgrade (to upgrade all the packages... can take a long time)
- sudo apt-get install lubuntu-desktop (to install the desktop environment)
- sudo reboot
- On the desktop environment, change the language settings and date and time settings (on desktop tray).
 
## Install ROS Indigo
Instructions are taken from [this tutorial.](http://wiki.ros.org/indigo/Installation/Ubuntu)
- Setup the source list following this link : (https://help.ubuntu.com/community/Repositories/Ubuntu)
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

## Wifi configuration (WIFI N)
For the moment, let's install a classical WIFI 802.11N dongle as [EDIMAX-EW-7811UN](https://www.amazon.fr/Edimax-EW-7811UN-Nano-Adaptateur-sans/dp/B003MTTJOY)
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
For further experiments, we will use cristal clear Wifi 802.11ac... to be completed

## Install Raspberry Pi Cam V2.0
the procedure is taken from [here](https://www.raspberrypi.org/forums/viewtopic.php?f=56&t=100553)
- sudo nano /boot/config.txt
- add the following lines at the end of the file /boot/config.txt : 
```
start_x=1
gpu_mem=128
```
- git clone https://github.com/raspberrypi/userland
- perform the following modifications :
```
diff --git a/buildme b/buildme
index ce8f516..7cef87d 100755
--- a/buildme
+++ b/buildme
@@ -2,10 +2,11 @@

 if [ "armv6l" = `arch` ]; then
        # Native compile on the Raspberry Pi
+       export LDFLAGS="-Wl,--no-as-needed"
        mkdir -p build/raspberry/release
        pushd build/raspberry/release
        cmake -DCMAKE_BUILD_TYPE=Release ../../..
-       make
+       make -j4
        if [ "$1" != "" ]; then
         sudo make install DESTDIR=$1
        else
diff --git a/makefiles/cmake/toolchains/arm-linux-gnueabihf.cmake b/makefiles/cmake/toolchains/arm-linux-gnueabihf.cmake
index 575cc0e..a5bebcd 100644
--- a/makefiles/cmake/toolchains/arm-linux-gnueabihf.cmake
+++ b/makefiles/cmake/toolchains/arm-linux-gnueabihf.cmake
@@ -10,7 +10,8 @@ SET(CMAKE_ASM_COMPILER arm-linux-gnueabihf-gcc)
 SET(CMAKE_SYSTEM_PROCESSOR arm)

 #ADD_DEFINITIONS("-march=armv6")
-add_definitions("-mcpu=arm1176jzf-s -mfpu=vfp -mfloat-abi=hard")
+#add_definitions("-mcpu=arm1176jzf-s -mfpu=vfp -mfloat-abi=hard")
+add_definitions("-march=armv7-a -mfpu=neon -mfloat-abi=hard")

 # rdynamic means the backtrace should work
 IF (CMAKE_BUILD_TYPE MATCHES "Debug")
```
- cd /home/ubuntu/userland
- sudo ./buildme (to compile the new version of userland)
- export LD_LIBRARY_PATH=/opt/vc/lib/:$LD_LIBRARY_PATH
- sudo reboot
- 
## needed Packages for drone
[The packages availables for this configuration.](http://repositories.ros.org/status_page/ros_indigo_default.html)
Install ARUCO
- sudo apt-get install ros-indigo-aruco

# What to install on the "hive" computer (Windows 10)
- Install python(x,y) distrib : http://python-xy.github.io/
- TBC

# Major links
- ARUCO main page : http://www.uco.es/investiga/grupos/ava/node/26
- ARUCO python binding : https://github.com/fehlfarbe/python-aruco
- TBC
