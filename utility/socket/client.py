import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    mySocket = socket.socket()
    mySocket.connect((host,port))

    message = input(" Enter Number : ")

    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()

        print ('Received from server: ' + data)
        message = input(" Enter Number : ")

    mySocket.close()

if __name__ == '__main__':
    Main()
