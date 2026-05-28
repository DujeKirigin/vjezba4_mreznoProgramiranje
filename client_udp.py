import socket
from local_machine_info import print_machine_info

print_machine_info()

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    while True:
        message = input("Unesi poruku ili 'exit' za kraj: ")

        if message.lower() == "exit":
            break

        client_socket.sendto(message.encode(), (HOST, PORT))

        data, addr = client_socket.recvfrom(1024)
        print(f"[UDP CLIENT] Odgovor servera: {data.decode()}")