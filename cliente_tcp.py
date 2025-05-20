import socket
import time


SERVER_ADDRESS = '192.168.3.7' 
SERVER_PORT = 8000
NUM_PINGS = 10


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(1)  

try:
    client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
    print(f"Conectado ao servidor {SERVER_ADDRESS}:{SERVER_PORT}\n")

    print("Iniciando cliente Ping TCP...\n")

    for seq in range(1, NUM_PINGS + 1):
        timestamp = time.time()
        message = f'Ping {seq} {timestamp}'

        try:
            start_time = time.time()

            client_socket.send(message.encode())

            response = client_socket.recv(1024)

            end_time = time.time()

            rtt = end_time - start_time

            print(f"Resposta do servidor: {response.decode()} | RTT = {rtt:.6f} segundos")

            time.sleep(1)

        except socket.timeout:
            print(f"Ping {seq} falhou (Timeout - pacote considerado perdido)")

    client_socket.send("close".encode())
    try:
        response = client_socket.recv(1024)
        print(f"\nServidor respondeu ao encerramento: {response.decode()}")
    except socket.timeout:
        print("\nServidor não respondeu ao encerramento (Timeout).")

except Exception as e:
    print(f"Erro: {e}")

finally:
    client_socket.close()
    print("\nCliente Ping TCP finalizado.")
