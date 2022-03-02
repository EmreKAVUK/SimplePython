import threading
import socket

#Starting Point
SIZE =50
SERVER='localhost'
PORT = 7979
ADDR = (SERVER,PORT)
connected = True
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET = IPV4 , SOCK_STREAM = TCP , SOCKDGRAM = UDP
server.bind(ADDR) #Dinlemeye alıncak adress

def handle_client(conn,addr):
    global connected
    print("[CONNECT] get connection {} ".format(addr))
    while connected:
        get_msg = conn.recv(SIZE).decode()#Mesajı alıp Stringe çeviriyor
        if get_msg != '':
            print(f'[{addr}] msg : ',get_msg)
            #server.send(b'True' + (b''*46))#Sıze ı 50 verdik True 4 harfli kalan 46 harflik alanı bos atıyoruz böylece 50 ye tamamlanıyor
            send ='True' + (''*46)
            conn.send(send.encode())

        if get_msg == "disconnect" :
            connected = False
    conn.close()

def main():
    print(f'[LISTENING] server on {ADDR} listening...')
    while True:
        server.listen()#Dinlemeye alıyoruz
        conn, addr = server.accept()#Serve in kullanıcı kabul etmesi için accept kullanılır 2 deger döndürür kulanıc ile iletişim kuralacak socket nesnesi conn, ve kulannıcı baglandıgı adress ver port addr

        t = threading.Thread(target=handle_client,args=(conn,addr))
        t.start()
main()