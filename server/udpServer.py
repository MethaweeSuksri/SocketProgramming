import socket
import threading
import logging
import time

logger = logging.Logger( 'Fak' )

# GLOABAL VARIABLE
PORT = 5555
SERVER = socket.gethostbyname( socket.gethostname() )

# Function
def messageEncoder( serverSocket ):
    while True:
        message, clientAddress = serverSocket.recvfrom( 2048 )
        modifiedMessage = message.decode().upper()
        serverSocket.sendto( modifiedMessage.encode() , clientAddress )

def timerPrint():
    for i in range(5):
        time.sleep( 1 )
        print( 'here' )

def main():
    serverSocket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    serverSocket.bind( ( "", PORT ) )
    print( "server ready to recive" )

    encoder = threading.Thread( target = messageEncoder, args = ( serverSocket, ) )
    timer = threading.Thread( target = timerPrint )

    encoder.start()
    timer.start()

    encoder.join()
    timer.join()

    # while True:
    #     message, clientAddress = serverSocket.recvfrom( 2048 )
    #     modifiedMessage = message.decode().upper()
    #     serverSocket.sendto( modifiedMessage.encode() , clientAddress )

if __name__ == "__main__":
    main()