import socket
  
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.bind(('192.168.7.158', 5000))
  
s.listen(1)
conn, addr = s.accept()

while True:
    data= conn.recv(1024)
    print('Received:' + data.decode())
 
s.close()