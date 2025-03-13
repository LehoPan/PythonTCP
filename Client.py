import socket
import ipaddress

# main function for client driver
if __name__ == "__main__":
    # recieves input from user about the desired IP address and port number
    ip_dest = input("Target IP address: ")
    port_dest = int(input("Target Port: "))     # convert input for the port into an integer

    # prompts user to input the message they would like to send
    message = input("Message: ")

    # creates the TCP socket
    myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connects to the server
    myTCPSocket.connect((ip_dest, port_dest))

    # continuous loop to allow multiple messages to be sent
    while True:
        # converts the message into a byte array and sends it through the TCP connection
        print("SENDING...")
        myTCPSocket.send(bytearray(str(message), encoding='utf-8'))
        serverResponse = myTCPSocket.recv(100).decode() # Recieves any responses from the server

        # prints anything the server sends back to the console
        print("SERVER: ", serverResponse)

        # asks the user if they would like to send another message, breaks from loop if not
        if input("Send another message?(Y/n)").lower() == "y":
            print()
            message = input("Message: ")
        else: 
            break

    # safely closes the TCP connection
    myTCPSocket.close()
