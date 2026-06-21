import socket
import threading

# GLOABAL VARIABLE
PORT = 5555
SERVER = socket.gethostbyname( socket.gethostname() )

# Function
def main():
    clientSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    clientSocket.connect( ( SERVER, PORT ) )

    message = input( 'input lowercase :' )
    clientSocket.send( message.encode() )
    modifiedMessage = clientSocket.recv( 2024 )
    print( 'From Server :', modifiedMessage.decode() )
    
    clientSocket.close

if __name__ == "__main__":
    main()