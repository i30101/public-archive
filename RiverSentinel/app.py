import serial
import json
from writer import Writer

METRICS = ["pH", "TDS", "turbidity", "temperature"]


ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def get_serial() -> dict:
    ser.reset_input_buffer()
    
    line = ''
    while(line == ''):
        line = ser.readline().decode('utf-8').rstrip()
    readings_list = [float(i) for i in line.split(", ")]
    Writer.append_reading(readings_list)
    readings = {}
    for i in range(4):
        readings[METRICS[i]] = readings_list[i]
    return readings


Writer.truncate()

while True:
    try:
        data = get_serial()
        print("RECEIVED\t", data)
        json_string = json.dumps(data)
        with open("./data/data.json", 'w') as file:
            file.write(json_string)
    
    except KeyboardInterrupt:
        break

ser.close()
