# SEA:ME / DES_Project1

## 1. Install Ubuntu 22.04 Server in Raspberry Pi (Use Raspberry Pi Imager)

![Raspberry Pi Imager](https://www.raspberrypi.com/software/)

- Choose OS: "SCL or GUI (Raspbian 64/32 bits)"
- Select USB Driver
- Go to Setting (Advanced Option)

### Enable SSH and Set User_Name, Password
![Enable SSH and Set User_Name, Password](https://github.com/Ho-mmd/DES_Project1/assets/55338823/1835122e-955a-4415-9638-0cb4549a7f07)

### Configure Wireless Lan
![Configure Wireless Lan](https://github.com/Ho-mmd/DES_Project1/assets/55338823/3b8c98b3-c74e-4de8-969d-4c75220c7dff)

Press Save Button

- Press Write Button
- Insert USB Driver into Raspberry Pi and start installing Ubuntu

## 2. Follow the Manual (H/W)

- [Piracer Assembly Manual](https://www.waveshare.com/wiki/PiRacer_Assembly_Manual)

## 3. Follow the Guide Line (S/W)

- [Piracer-py](https://pypi.org/project/piracer-py/)

```bash
sudo -s
echo "deb http://archive.raspberrypi.org/debian/ buster main" >> /etc/apt/sources.list
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7FA3303E
apt update
exit

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

If you choose Ubuntu, run the following command:

```bash
mount /dev/mmcblk0p1 /boot/
```

Enable i2c and Camera using 'raspi-config' tool:

- i2c: Interface Options > I2C
- Camera: Interface Options > Camera

Afterwards, reboot:

```bash
sudo reboot
```

Install piracer-py package:

```bash
cd ~
mkdir piracer_test/
cd piracer_test/
python3 -m venv venv
source venv/bin/activate
pip install piracer-py
```

After following the steps, you can try the example codes provided in the [link](https://pypi.org/project/piracer-py/):

- basic_example.py: Operating throttle and steering
- rc_example.py: Check the Controller (Check Connect, Throttle, Steering works correctly)

![rc_example.py](https://github.com/Ho-mmd/DES_Project1/assets/55338823/f459b2e5-dbe7-48ee-a0ef-824d6a074ca3)

- camera_grab_example.py: Check the Camera
```

This should provide a better formatting for the markdown content. If you still have any specific formatting requirements or face any issues, feel free to let me know!
