import socket,platform,os
addr="192.168.1.113"
port=123
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((addr,port))

s.listen(1)
connection,addr=s.accept()
while 1:
    try: 
        data=connection.rev(1024)
    except:
        continue
    if (data.decode('utf-8'))=='1':
        tosend=platform.paltform()+" "+ platform.machine()
        connection.sendall(tosend.encode())
    elif(data.decode('utf-8'))=='2':
        data=connection.recv(1024)
        try:
            filelist=os.listdir(data.decode('utf-8'))
            tosend=""
            for x in filelist:
                tosend+=","+x
        except:
            tosend="wrongpath"
        connection.sendall(tosend.encode())
    elif(data.decode('utf-8'))=='0':
        connection.cloe()
        connection, address=s.accept()
