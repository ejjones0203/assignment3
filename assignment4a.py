# Program Name: Assignment4a.py
# Course: IT3883/Group 18
# Student Name: Enjie Jones
# Assignment Number: Assignment 4
# Due Date: 3/24/2025
# Purpose: What does the program do (in a few sentences)? client program that you can send a message to a server, and the server will return the message but in caps
# List Specific resources used to complete the assignment. https://www.geeksforgeeks.org/socket-programming-python/ | Module 4-1 Network Programming

import socket

def clientprogram():
    host = '127.0.0.1' #defining the host and port number. I chose 50000.
    port = 50000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((host, port)) #initiates tcp connection

        message = input("Send a message: ") #send message

        soc.sendall(message.encode()) #sends all socket data
        r = soc.recv(3000) #max number of bytes that can be read

        print("Recieved from networkingthing:", r.decode()) #decodes response, or capital letters in this case

clientprogram() #initiate program