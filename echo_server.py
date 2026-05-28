import socket
import datetime
from local_machine_info import print_machine_info

print_machine_info()
print(datetime.datetime.now())

HOST = "0.0.0.0"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[SERVER] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()

        with conn:
            print(f"[SERVER] Connected by {addr}")

            while True:
                data = conn.recv(1024)

                if not data:
                    break

                message = data.decode()
                print(f"[SERVER] Received: {message}")

                if message.lower() == "vaše_ime_prezime":
                    response = "Unos nije podržan."
                else:
                    response = message

                conn.sendall(response.encode())