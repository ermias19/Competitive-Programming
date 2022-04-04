from multiprocessing.dummy import connection
import socket
ip=input('please nigga input the servers ip addres')
port= int(input('what port number do you want to communicate'))
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(2)
while 1:
    conn,addr=s.accept()
    data=conn.recv(1024)
    if not data: break
    # conn.send('wow niga you made it')
    print(data.decode('utf-8'))
    ermias='hello ermudaa ladada'
    conn.send(ermias.encode())
    conn.close()
print(addr)
    
conn.close() 