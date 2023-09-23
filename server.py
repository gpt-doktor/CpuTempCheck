import socket
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-host", help="IP address of the server", type=str)
argParser.add_argument("-port", help="port of the server", type=int)
argParser.add_argument("-output", help="name of the output file", type=str)

args = argParser.parse_args()
  
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.bind((args.host, args.port))
  
s.listen(1)
conn, addr = s.accept()

while True:
    with open(args.output, 'a') as f:
        data= conn.recv(1024)
        f.write("\n"+data.decode())
        
 
s.close()