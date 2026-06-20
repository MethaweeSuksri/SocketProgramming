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

if __name__ == "__main__":
    main()