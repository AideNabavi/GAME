import socket
import json


SERVER_IP = "127.0.0.1"
PORT = 5555


name = input("Name: ")
country = input("Country: ")
profile = input("Profile image: ")


player = {
    "name": name,
    "country": country,
    "profile": profile
}


client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)


client.connect(
    (SERVER_IP, PORT)
)


client.send(
    json.dumps(player).encode()
)


message = client.recv(1024)

print(message.decode())