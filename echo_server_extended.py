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
        conn, client_address = server_socket.accept()

        with conn:
            print(f"[SERVER] Connected by {client_address}")

            while True:
                data = conn.recv(1024)

                if not data:
                    break

                message = data.decode()
                receive_time = datetime.datetime.now()
                client_ip = client_address[0]

                print(f"[SERVER] Vrijeme primitka: {receive_time}")
                print(f"[SERVER] Sadržaj poruke: {message}")
                print(f"[SERVER] IP adresa klijenta: {client_ip}")

                if message.lower() == "vaše_ime_prezime":
                    response = "Unos nije podržan."
                else:
                    response = message

                conn.sendall(response.encode())