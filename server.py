from socket import *
import os

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 4444))
server.listen(5)

while True:
    obj, addr = server.accept()

    try:
        file_path = os.path.join("tumb.png")
        file_size = os.path.getsize(file_path)
        file_name = file_path.split('.')[0]
        file_exte = file_path.split('.')[1]

        info_file = str({
            "path":file_path,
            "size": file_size,
            "name": file_name,
            "extension": file_exte
        })

        obj.send(info_file.encode())

        with open(file_path, "rb") as file:
            obj.send(file.read(file_size))

        obj.close()

    except Exception as ex:
        print(ex)
