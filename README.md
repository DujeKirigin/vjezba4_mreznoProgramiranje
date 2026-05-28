# Vježba 4 - Socket programiranje

## Datoteke

- `local_machine_info.py`
- `server_udp.py`
- `client_udp.py`
- `echo_server.py`
- `echo_client.py`
- `echo_server_extended.py`

## Zadatak 0 - Informacije o lokalnom računalu

Datoteka `local_machine_info.py` sadrži funkciju `print_machine_info()` koja ispisuje naziv računala i IP adresu.

### Pokretanje

```bash
python3 local_machine_info.py

## Zadatak 0 - Ispis informacija o lokalnom računalu

Datoteka: `local_machine_info.py`

Funkcija `print_machine_info()` ispisuje naziv računala i njegovu IP adresu.

### Pokretanje

```bash
python3 local_machine_info.py


## Zadatak 1 - UDP klijent-server aplikacija

U ovom zadatku TCP aplikacija iz prethodne vježbe prepravljena je u UDP verziju.

UDP server koristi `socket.SOCK_DGRAM`, prima poruku od klijenta i vraća potvrdu da je poruka primljena.

### Pokretanje servera

```bash
python3 server_udp.py


## Zadatak 2 - Echo TCP server i klijent

U ovom zadatku izrađeni su `echo_server.py` i `echo_client.py`.

Server koristi TCP protokol i stalno sluša nove konekcije pomoću beskonačne petlje.  
Klijent unosi poruku pomoću `input()` funkcije, šalje je serveru, a server vraća istu poruku.

Ako korisnik unese `vaše_ime_prezime`, server vraća poruku:

```text
Unos nije podržan.


## Zadatak 3 - Analiza izlaza

Testiranje je provedeno pomoću nekoliko različitih poruka.

### Klijent - primjer ispisa

```text
Host name: codespaces-xxxxx
IP address: 127.0.0.1
[CLIENT] Connected to server.
Unesi poruku ili 'exit' za kraj: Pozdrav serveru
[CLIENT] Received: Pozdrav serveru
Unesi poruku ili 'exit' za kraj: Test poruka
[CLIENT] Received: Test poruka
Unesi poruku ili 'exit' za kraj: vaše_ime_prezime
[CLIENT] Received: Unos nije podržan.
Unesi poruku ili 'exit' za kraj: exit


## Zadatak 4 - Proširenje Echo servera

Datoteka: `echo_server_extended.py`

Server je proširen tako da svaki put kada primi poruku ispisuje:

- vrijeme primitka poruke
- sadržaj poruke
- IP adresu klijenta

### Pokretanje servera

```bash
python3 echo_server_extended.py