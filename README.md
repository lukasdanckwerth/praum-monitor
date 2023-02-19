# praum-monitor

## Readings

MQ-4

- CH4 (Methan)
- LPG (Liquefied Petroleum Gas)
- H2 (Hydrogen)
- SMOKE
- ALCOHOL
- CO (Carbon monoxide)

MQ-135

- ACETON
- TOLUENO
- ALCOHOL
- CO2 (Carbon dioxide)
- NH4 (Ammonium)
- CO (Carbon monoxide)

Sound Sensor
Analoge werte von 0 1024.

Motion Sensor


## GPIOs

![](/Users/lukas/Developer/Others/praum-monitor/doc/rpi-gpio.jpg)

![](/Users/lukas/Developer/Others/praum-monitor/doc/mcp3008.png)

### Connecting RaspberryPi and MCP3008

![](/Users/lukas/Developer/Others/praum-monitor/doc/rpi-mcp3008.webp)

### GPIO distribution

| RaspberryPi Pin | MCP3008 Pin      | Device                 |
|-----------------|------------------|------------------------|
| Pin 1 (3.3V)	   | Pin 16 (VDD)     |                        |
| Pin 1 (3.3V)	   | Pin 15 (VREF)    |                        |
| Pin 6 (GND)	    | Pin 14 (AGND)    |                        |
| Pin 23 (SCLK)   | 	Pin 13 (CLK)    |                        |
| Pin 21 (MISO)	  | Pin 12 (DOUT)    |                        |
| Pin 19 (MOSI)	  | Pin 11 (DIN)     |                        |
| Pin 24 (CE0)	   | Pin 10 (CS/SHDN) |                        |
| Pin 6 (GND)	    | Pin 9 (DGND)     |                        |
|                 | CH0              | MQ-135 (AO)            |
|                 | CH1              | MQ-4 (AO)              |
|                 | CH2              | Sound Sensor V2 (A0)   |
|                 | CH3              |                        |
|                 |                  | traffic light 1 Green  |
|                 |                  | traffic light 1 Yellow |
|                 |                  | traffic light 1 Red    |
|                 |                  | traffic light 1 GND    |
|                 |                  | traffic light 2 Green  |
|                 |                  | traffic light 2 Yellow |
|                 |                  | traffic light 2 Red    |
|                 |                  | traffic light 2 GND    |
|                 |                  | traffic light 3 Green  |
|                 |                  | traffic light 3 Yellow |
|                 |                  | traffic light 3 Red    |
|                 |                  | traffic light 3 GND    |

## Operations

### Install samba

```bash
sudo apt-get install --assume-yes samba samba-common-bin
sudo smbpasswd -a pi
# user: pi
# password: pi
sudo vim /etc/samba/smb.conf
sudo mkdir /srv/praum-monitor
sudo chown pi:pi /srv/praum-monitor
sudo chmod 775 /srv/praum-monitor
```

See [smb.conf](assets/smb.config).


## Disable display sleep

```bash
# to avoid a `unable to open display` error use the following
export DISPLAY=:0

# set screen saver timeout to zero:
xset s 0

# set dpms (EnergyStar) to disabled:
xset -dpms

# verify your settings with
xset q
```

## Install Firefox

```bash
sudo apt update --assume-yes && \
sudo apt install firefox-esr --assume-yes
```

## Autostart Firefox

Edit:

```bash
sudo vim /etc/xdg/lxsession/LXDE-pi/autostart
```

## Hide taskbar / menubar

Edit `/etc/xdg/lxsession/LXDE-pi/autostart`

```bash
sudo vim /etc/xdg/lxsession/LXDE-pi/autostart
```

Comment the following line.

```bash
@lxpanel --profile LXDE
```

## Make the mouse disappear

You can also add this line if you want the mouse to disappear:

Install _unclutter_:

```bash
sudo apt-get install unclutter
```

Add the following line to your `/etc/xdg/lxsession/LXDE-pi/autostart` file.

```bash
@unclutter -idle 0.1 -root
```

## Development

### dev-server

Start a local http server for development with.

```bash
python3 dev-server.py
```
