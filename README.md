# SEA:ME / DES_Project1

## 1. Install Ubuntu 22.04 Server on Raspberry Pi (Using Raspberry Pi Imager)

![Raspberry Pi Imager](https://github.com/Ho-mmd/DES_Project1/assets/55338823/bdaa29b5-dd84-4ec0-9239-d724b5a94a57)

1. Download and start Raspberry Pi Imager from [here](https://www.raspberrypi.com/software/).
2. Choose OS: "SCL or GUI (Raspbian 64/32 bits)"
3. Select USB Driver.
4. Go to Settings (Advanced Option).

   - Enable SSH and set User_Name, Password.
   ![Enable SSH and Set User_Name, Password](https://github.com/Ho-mmd/DES_Project1/assets/55338823/1835122e-955a-4415-9638-0cb4549a7f07)

   - Configure Wireless Lan.
   ![Configure Wireless Lan](https://github.com/Ho-mmd/DES_Project1/assets/55338823/3b8c98b3-c74e-4de8-969d-4c75220c7dff)

5. Press the Save Button.
6. Press the Write Button.
7. Insert the USB Driver into Raspberry Pi to start installing Ubuntu.

## 2. Follow the Hardware (H/W) Assembly Manual

Follow the [PiRacer Assembly Manual](https://www.waveshare.com/wiki/PiRacer_Assembly_Manual).

## 3. Follow the Software (S/W) Guide

Follow the [PiRacer-py guide](https://pypi.org/project/piracer-py/).

1. Run the following commands to add the Raspberry Pi repository and update the system:

   ```bash
   sudo -s
   echo "deb http://archive.raspberrypi.org/debian/ buster main" >> /etc/apt/sources.list
   apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7FA3303E
   apt update
   exit
   ```

2. Install the required libraries and tools:

   ```bash
   sudo apt update
   sudo apt install \
       gcc \
       v4l-utils \ 
       i2c-tools \ 
       raspi-config \ 
       python3-dev \
       python3-setuptools \ 
       python3-venv \
       libopencv-dev \
       piracer-py
   ```

3. If you choose Ubuntu, mount the boot partition:

   ```bash
   mount /dev/mmcblk0p1 /boot/
   ```

4. Enable I2C and Camera using the 'raspi-config' tool:

   - i2c: Interface Options > I2C
   - Camera: Interface Options > Camera

   Afterwards, reboot the Raspberry Pi:

   ```bash
   sudo reboot
   ```

5. Install the piracer-py package:

   ```bash
   cd ~
   mkdir piracer_test/
   cd piracer_test/
   python3 -m venv venv
   source venv/bin/activate
   pip install piracer-py
   ```

After following these steps, you can try the example code provided in the [link](https://pypi.org/project/piracer-py/).

- basic_example.py: Operating throttle and steering.
- rc_example.py: Check the Controller (Check Connect, Throttle, Steering works correctly)
  ![RC Example](https://github.com/Ho-mmd/DES_Project1/assets/55338823/f459b2e5-dbe7-48ee-a0ef-824d6a074ca3)

- camera_grab_example.py: Check the Camera.

