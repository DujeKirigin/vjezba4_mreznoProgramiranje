import socket
from local_machine_info import print_machine_info

print_machine_info()

HOST = "localhost"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("[CLIENT] Connected to server.")

    while True:
        message = input("Unesi poruku ili 'exit' za kraj: ")

        if message.lower() == "exit":
            break

        client_socket.sendall(message.encode())

        data = client_socket.recv(1024)
        print(f"[CLIENT] Received: {data.decode()}")