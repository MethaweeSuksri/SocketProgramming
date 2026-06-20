import socket
import threading

PORT = 5555

SERVER = socket.gethostbyname( socket.gethostname() )

def main():
    clientSocket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    message = input("enter text: ")
    clientSocket.sendto(    message.encode(),
                            ( SERVER, PORT ) )

    receivedMessage, serverAddress = clientSocket.recvfrom( 2024 )
    print( receivedMessage.decode() )
    clientSocket.close

if __name__ == "__main__":
    main()