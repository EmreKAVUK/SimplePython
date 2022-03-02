import socket

SIZE =50
SERVER='localhost'
PORT = 7979
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send():
    send_data = input("[client] Enter your data : ")
    send_lenght = len(send_data)
    client.send(send_data.encode() + (b'' * (50-send_lenght)))
    get_data = client.recv(50)
    print("[Data] GET Data : {} ".format((get_data)))
send()
