import socket
import threading

# GLOABAL VARIABLE
PORT = 5555

# Function
def main():
    mySocket = socket.socket()
    print(mySocket.__repr__)

if __name__ == "__main__":
    main()