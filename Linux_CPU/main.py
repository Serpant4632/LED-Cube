import psutil
import socekt
import time

TARGET_IP = "XXX.XXX.XXX.XXX"
TARGET_PORT = 1234

while True:
    temperature = 0.0
    for x in rang(5):
        temperature += psutil.sensors_temperatures()["coretemp"][0].current
        time.sleep(0.5)
    temperature /= 5.0

    cores = psutil.cpu_percent(percpu=True)

    out = str(temperature) + ',' + ','.join(map(str, sorted(cores, reverse=True)))
    print(out)
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(out.encode('utf-8'), (TARGET_IP,TARGET_PORT))
    
