import socket
import threading
import logging
from concurrent.futures import ThreadPoolExecutor

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
executor = ThreadPoolExecutor(max_workers=10)

# Submit tugas ke executor
thread_count = 0
for _ in range(100000):
    thread_count+=1
    executor.submit(connect_to_server)
    # print(f"Threadpool amount: {thread_count}")
# Menunggu semua tugas selesai
executor.shutdown()
print(f"Threadpool amount: {thread_count}")
