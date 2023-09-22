import socket
import time
import psutil

def get_cpu_temperature():
    cpu_temperature = psutil.sensors_temperatures()['coretemp'][0].current
    return cpu_temperature

print(psutil.sensors_temperatures())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("192.168.7.158", 5000))
    t = time.time()
    while True:
        sock.send(f"temp: {get_cpu_temperature()} C, elapsed for: {time.time()-t} s".encode())
        time.sleep(5)