import socket

target=input('please nigga input address to be hack')
port= input('enter a range of port numbers')
port.split('-')
lower=int(port.split('-')[0])
higher=int(port.split('-')[1])
for port in range(lower,higher):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status=s.connect_ex((target, port))
    if status==0:
        print('the port', port,'is open')
    else:
        print('port ',port,'closed')
