# DES_Project1

## 1. Install Ubuntu 22.04 Server in Raspberry Pi (Use Raspberry Pi Imager)

<img src = "https://github.com/Ho-mmd/DES_Project1/assets/55338823/bdaa29b5-dd84-4ec0-9239-d724b5a94a57" width = "70%" height = "70%">

### - [Download and Start Raspberry Pi Imager](https://www.raspberrypi.com/software/)
### - Choose OS
### - Select USB Driver
### - Go Setting (Advanced Option)

#### * Enable SSH and Set User_Name, Password
<img src = "https://github.com/Ho-mmd/DES_Project1/assets/55338823/1835122e-955a-4415-9638-0cb4549a7f07" width = "70%" height = "70%">

#### * Configure Wireless Lan
<img src = "https://github.com/Ho-mmd/DES_Project1/assets/55338823/3b8c98b3-c74e-4de8-969d-4c75220c7dff" width = "70%" height = "70%">

#### * Press Save Button

### - Press Write Button
### - Insert USB Driver in to Raspberry Pi, Start to install Ubuntu

## 2. Follow the Manual (H/W)

### - [Piracer Assembly Manual](https://www.waveshare.com/wiki/PiRacer_Assembly_Manual)

## 3. Follow the Guide Line (S/W)

### - [Piracer-py](https://pypi.org/project/piracer-py/)

#### - Important!! (You need to install some libraries and tools under below.)
##### - gcc 
##### - v4l-utils 
##### - i2c-tools 
##### - raspi-config 
##### - python3-dev 
##### - python3-setuptools 
##### - python3-venv 
##### - libopencv-dev
##### - piracer-py 

## After follwing some steps, you can trying example code in the [link](https://pypi.org/project/piracer-py/)

### - basic_example.py: Operating throttle and streering
### - rc_example.py: Check the Controller (Check Connect, Throttle, Steering works correctly)
<img src = "https://github.com/Ho-mmd/DES_Project1/assets/55338823/f459b2e5-dbe7-48ee-a0ef-824d6a074ca3" width = "20%" height = "20%">

### - camera_grab_example.py: Check the Camera
