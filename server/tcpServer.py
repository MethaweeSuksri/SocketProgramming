import socket
import threading
import logging

logger = logging.Logger( 'Fak' )

# GLOABAL VARIABLE
PORT = 5555
SERVER = socket.gethostbyname( socket.gethostname() )

# Function

def main():
    serverSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    serverSocket.bind( ( '', PORT ) )
    serverSocket.listen( 1 )
    print( 'Server is ready to receive' )

    while True:
        connectionSocket, addr = serverSocket.accept()
        print(addr)
        print(addr)
        print(addr)
        message = connectionSocket.recv( 1024 ).decode()
        capitalizedMessage = message.upper()
        connectionSocket.send( capitalizedMessage.encode() )
        connectionSocket.close()

if __name__ == "__main__":
    main()