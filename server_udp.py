import socket
from local_machine_info import print_machine_info

print_machine_info()

HOST = "0.0.0.0"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))

    print(f"[UDP SERVER] Listening on {HOST}:{PORT}")

    while True:
        data, addr = server_socket.recvfrom(1024)

        message = data.decode()
        print(f"[UDP SERVER] Received from {addr}: {message}")

        response = f"Server je primio poruku: {message}"
        server_socket.sendto(response.encode(), addr)