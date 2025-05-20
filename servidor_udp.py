import socket
import time

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_ip = "0.0.0.0"
    port = 8000

    server_socket.bind((server_ip, port))
    print(f"Servidor UDP escutando em {server_ip}:{port}")
    num = 1

    while True:
        request, client_address = server_socket.recvfrom(1024)
        start_time = time.time()
        request = request.decode('utf-8')
        
        end_time = time.time()

        processing_time = end_time - start_time
            
        print(f"Ping de {client_address}: Ping {num} - Tempo de processamento: {processing_time:.6f} segundos")
        num += 1
        if request.lower() == "close":
            server_socket.sendto("closed".encode('utf-8'), client_address)
            print("Fechando servidor.")
            break

        response = "accepted".encode('utf-8')
        server_socket.sendto(response, client_address)

    server_socket.close()


run_server()
