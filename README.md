# public-archive

This repository is a public archive of previous projects. 

<br><br>

## ISEF 2023

![version](https://img.shields.io/badge/release-v3.0.0-blue)
![python-versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11-limegreen)

Various project files for 2022-2023 Science Fair. 

### Components
- Vehicle Routing Problem (VRP) solver using `Google OR-Tools`
- VRP scenario and solution visualizer using `NumPy` and `maplotlib`
- Visualization of restaurants in D.C.'s Chinatown using `gmplot`
- AnyLogic configuration file (`.ALP` file) parser

### Dependencies
- Python 3.9 or newer
- PyPi `pandas` library for reading CSV files
- PyPi `NumPy` for matrix comprehension
- PyPi `matplotlib.pyplot` for data and VRP visualization
- PyPi `ortools` for VRP optimization using Google OR-Tools
- PyPi `gmplot` library for map generation with Python

Installing all PyPi dependencies: `pip install pandas numpy matplotlib ortools gmplot`

<br><br>


## RiverSentinel
![version](https://img.shields.io/badge/release-v3.1.0-blue)
![python-versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11-limegreen)
![arduino](https://img.shields.io/static/v1?label=Arduino&message=v2.2.1&logo=arduino&logoColor=white&color=blue)

Files for RiverSentinel: a project to enhance water quality monitoring 

### Components
- RiverSentinel probe configuration software for Arduino and Python
- Live water quality monitoring interface

### Depencencies
- Python 3.9 or newer
- Arduino IDE
- Raspberry Pi 4.0

<br><br>



## arduino
![version](https://img.shields.io/badge/release-v1.0.0-blue)

This folder contains code for events involving the Arduino platform. 

### Installation
Compiling and uploading code requires using the Arduino IDE. For Windows 11 school laptops, go to `Software Center` and install `Arduino`. For personal laptops, visit [Arduino's Software Page](https://www.arduino.cc/en/software) and install the latest IDE.


### Code Setup - Robot Tour

Getting the code on your computer: 
- Navigate to `Documents\Arduino` on your local drive
- Create new a new folder `Robot`
- Download `Robot.ino` from this reposity and copy to your new folder

Adding the MakeBlock library:
- Install the MakeBlock Drive library by installing this [zip](https://codeload.github.com/Makeblock-official/Makeblock-Libraries/zip/master) file
- Unzip file and copy entire file to `Documents\Ardunio\libraries`

Running your mBot:
- Connect your robot to your computer via a USB-B cable
- Select the right port/board and your board to `Ardunio Uno`
- Hit the arrow or "upload" button to flash code to the Arduino
- If you installed the MakeBlock library, your mBot should be up and running


### Code Setup - Detector Building

Ignore the LiquidCrystal library if you are using a laptop to display your readings.

