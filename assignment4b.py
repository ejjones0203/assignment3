# Program Name: Assignment4a.py
# Course: IT3883/Group 18
# Student Name: Enjie Jones
# Assignment Number: Assignment 4
# Due Date: 3/24/2025
# Purpose: What does the program do (in a few sentences)? server that receives a message from client program, and the server will return the message to client but in caps
# List Specific resources used to complete the assignment. https://www.geeksforgeeks.org/socket-programming-python/ | Module 4-1 Network Programming
import socket

def networkthing():
    host = '127.0.0.1' #define host and port number
    port = 50000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.bind((host, port)) #assign ip and port number, then we can run listen.
        soc.listen()

        print("The server program is listening now. You may send a message")

        conn, addr = soc.accept() #wait for client to connect. new socket object  return ip address

        with conn:
            data = conn.recv(3000) #receive 3000 bytes
            if data:
                r = data.decode().upper() #decode data, and apply .upper()
                conn.sendall(r.encode()) #send all data back to client


networkthing()