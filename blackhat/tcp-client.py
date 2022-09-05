import socket
import threading


def tcpCleint(host,port):
    target_host = host
    target_port = port

    #create a socket obj
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connect the client
    client.connect((target_host, target_port))

    stripWWW = target_host.split("www.")[1]

    #send data
    client.send(b"GET / HTTP/1.1\r\nHost: "+stripWWW+"\r\n\r\n")

    #receive data
    response = client.recv(4096)

    print (response)
