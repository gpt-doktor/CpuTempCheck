import socket
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-host", help="IP address of the server")
argParser.add_argument("-port", help="port of the server")

args = argParser.parse_args()
  
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.bind((args.host, args.port))
  
s.listen(1)
conn, addr = s.accept()

while True:
    data= conn.recv(1024)
    print(data.decode())
 
s.close()