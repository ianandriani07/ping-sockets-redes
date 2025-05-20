import socket
import time


def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "0.0.0.0"
    port = 8000

    server.bind((server_ip, port))
    server.listen(1)
    print(f"Servidor TCP escutando em {server_ip}:{port}")

    client_socket, client_address = server.accept()
    print(f"Conexão aceita de {client_address[0]}:{client_address[1]}")
    num = 1

    while True:
        try:
            request = client_socket.recv(1024)

            start_time = time.time()

            if not request:
                print("Cliente desconectou.")
                break

            request = request.decode("utf-8")
            print(f"Recebido: Ping {num}")

            if request.lower() == "close":
                client_socket.send("closed".encode("utf-8"))
                print("Encerrando conexão com o cliente.")
                break

            client_socket.send(f"Pong {num}".encode("utf-8"))

            end_time = time.time()

            processing_time = end_time - start_time
            print(f"Tempo de processamento deste ping: {processing_time:.6f} segundos")
            num += 1

        except Exception as e:
            print(f"Erro: {e}")
            break

    client_socket.close()
    server.close()
    print("Servidor encerrado.")


run_server()