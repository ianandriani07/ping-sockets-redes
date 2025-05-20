import socket
import time


SERVER_ADDRESS = '192.168.3.7' 
SERVER_PORT = 8000
NUM_PINGS = 10


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1) 


print("Iniciando cliente Ping UDP...\n")

for seq in range(1, NUM_PINGS + 1):
    timestamp = time.time()
    message = f'Ping {seq} {timestamp}'

    try:
        start_time = time.time()

        client_socket.sendto(message.encode(), (SERVER_ADDRESS, SERVER_PORT))

        response, server = client_socket.recvfrom(1024)

        end_time = time.time()

        rtt = end_time - start_time

        print(f"Resposta do servidor Pong {seq}: {response.decode()} | RTT = {rtt:.6f} segundos")
        time.sleep(1)

    except socket.timeout:
        print(f"Ping {seq} falhou (Timeout - pacote perdido)")


client_socket.sendto("close".encode(), (SERVER_ADDRESS, SERVER_PORT))
try:
    response, server = client_socket.recvfrom(1024)
    print(f"\nServidor respondeu ao encerramento: {response.decode()}")
except socket.timeout:
    print("\nServidor não respondeu ao encerramento (Timeout).")

client_socket.close()
print("\nCliente Ping UDP finalizado.")
