import multiprocessing
import socket
import logging

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")
    server_address = ('172.16.16.101', 45000)
    logging.warning(f"opening socket {server_address}")
    client_socket.connect(server_address)

    request = "TIME\r\n"
    logging.warning(f"[CLIENT] request {request}")
    client_socket.sendall(request.encode('utf-8'))

    response = client_socket.recv(1024)
    print("[DITERIMA DARI SERVER] " + response.decode('utf-8').strip())

    client_socket.close()

# Membuat 10 thread yang akan terhubung ke server
processes = []
thread = 0
for _ in range(10000):
    thread += 1
    process = multiprocessing.Process(target=connect_to_server)
    processes.append(process)
    process.start()

    print(f"Process amount: {thread}")
# Menunggu semua proses selesai
for process in processes:
    process.join()

