from socket import *
import os

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 4444))

file_info = str(client.recv(1024).decode().rstrip())
info = eval(file_info)

with open(info['name']+'_recebida_.'+info['extension'], "wb") as file:
    buffer = client.recv(info['size'])
    file.write(buffer)
