import wmi
import socket
import time

# data = ["CPU Package", "CPU Core #1", "CPU Core #2", "CPU Core #3", "CPU Core #4", "CPU Core #5",
#        "CPU Core #6", "CPU Core #7", "CPU Core #8"]

coreLoad = [0, 0, 0, 0, 0, 0, 0, 0]
temperature = 0

TARGET_IP = "192.168.0.193"
TARGET_PORT = 1233


while True:
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    winSensors = w.Sensor()
    for sensor in winSensors:
        if sensor.SensorType == u'Temperature':
            if sensor.Name == "CPU Package":
                temperature = f'{sensor.Value:.2f}'     # makes string of float with two numbers after point

        if sensor.SensorType == u'Load':
            if sensor.Name == "CPU Core #1":
                coreLoad[0] = f'{sensor.Value:.2f}'

            if sensor.Name == "CPU Core #2":
                coreLoad[1] = f'{sensor.Value:.2f}'

            if sensor.Name == "CPU Core #3":
                coreLoad[2] = f'{sensor.Value:.2f}'

            if sensor.Name == "CPU Core #4":
                coreLoad[3] = f'{sensor.Value:.2f}'

            if sensor.Name == "CPU Core #5":
                coreLoad[4] = f'{sensor.Value:.2f}'

            if sensor.Name == "CPU Core #6":
                coreLoad[5] = f'{sensor.Value:.2f}'

            if sensor.Name == "CPU Core #7":
                coreLoad[6] = f'{sensor.Value:.2f}'

            if sensor.Name == "CPU Core #8":
                coreLoad[7] = f'{sensor.Value:.2f}'

    out = temperature + "," + ",".join(sorted(coreLoad, reverse=True))
    # print(out)
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(out.encode("utf-8"), (TARGET_IP, TARGET_PORT))
    time.sleep(5)
