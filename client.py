import socket
import time
import psutil
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-host", help="IP address of the server", type=str)
argParser.add_argument("-port", help="port of the server", type=int)
argParser.add_argument("-n", help="time between temperature updates", type=int)

args = argParser.parse_args()

def get_cpu_temperature():
    cpu_temperature = psutil.sensors_temperatures()['coretemp'][0].current
    return cpu_temperature

print(psutil.sensors_temperatures())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((args.host, args.port))
    t = time.time()
    while True:
        sock.send(f"temp: {get_cpu_temperature()} C, elapsed for: {time.time()-t} s".encode())
        time.sleep(args.n)