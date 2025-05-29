# Sistema de Comunicação Cliente-Servidor via UDP e TCP: Ping Pong

## Descrição do projeto

Este projeto consiste na implementação de um sistema de comunicação entre cliente e servidor utilizando os protocolos UDP e TCP com o objetivo de medir o tempo de resposta entre o envio de mensagens "ping" e o recebimento das respectivas mensagens "pong". A atividade foi realizada como parte do estudo prático de Redes de Computadores na UFSC.

O cliente envia 10 mensagens sequenciais de "ping" para o servidor, que responde com uma mensagem "pong" correspondente. O cliente mede o RTT (Round Trip Time) — tempo de ida e volta — para cada mensagem.

## Autores do projeto

- Ian Andriani e Pedro Magnavita

---

## Introdução

### Objetivos específicos

- Implementar um sistema cliente-servidor utilizando os protocolos UDP e TCP em Python.
- Medir o tempo de viagem de ida e volta (RTT) para cada mensagem.
- Simular um comportamento similar ao comando `ping` padrão, porém utilizando **protocolo UDP e TCP** ao invés de ICMP.
- Estudar as diferenças de confiabilidade e desempenho entre os dois protocolos.

## Software

### Softwares utilizados

- **Python 3.x**: linguagem de programação utilizada para desenvolver tanto o cliente quanto o servidor.
- **Biblioteca socket**: módulo padrão do Python usado para criar conexões TCP e UDP.
- **Windows PowerShell**: terminal utilizado para executar os scripts e visualizar as saídas.

## Configurações

- **Porta utilizada**: 8000
- **Host**: `0.0.0.0` para o servidor (aceitando conexões de qualquer interface de rede).
- **Cliente**: executado a partir de uma máquina na mesma rede local.

### Observações importantes

- No protocolo **UDP**, o cliente aguarda até **1 segundo** pela resposta do servidor, para simular a possibilidade de perda de pacotes.
- No protocolo **TCP**, o cliente estabelece uma conexão persistente até o envio de todas as mensagens.

## Resultados
### Saída do servidor UDP

![Imagem do WhatsApp de 2025-05-20 à(s) 19 45 22_1b8422eb](https://github.com/user-attachments/assets/4222f455-ec63-4112-a643-00eaf180fde6)

- O servidor recebeu corretamente as mensagens de ping.
- Tempo de processamento no servidor foi praticamente zero.
- O servidor escutou na porta 8000 e respondeu os "pong" adequadamente.

### Saída do cliente UDP

![Imagem do WhatsApp de 2025-05-20 à(s) 19 45 59_74e20d3a](https://github.com/user-attachments/assets/322a4cb7-2392-49d2-8ddd-3f74158afc45)

- O cliente conseguiu calcular o RTT para todas as mensagens.
- RTT variando entre ~1 ms a ~61 ms.
- Nenhuma mensagem foi perdida durante a execução.
- O cliente enviou uma mensagem de encerramento ao servidor ao final.

---

### Saída do servidor TCP

![Imagem do WhatsApp de 2025-05-20 à(s) 19 47 38_9fbd4b32](https://github.com/user-attachments/assets/ec7d61e5-7193-4d86-82df-3fd1539fde65)

- O servidor TCP aceitou a conexão do cliente.
- As mensagens foram recebidas sequencialmente e respondidas com o "pong".
- Alguns tempos de processamento foram superiores a 15 ms, indicando possíveis flutuações na rede ou no processamento.

### Saída do cliente TCP

![Imagem do WhatsApp de 2025-05-20 à(s) 19 48 10_1d5b726d](https://github.com/user-attachments/assets/5c9d2f3d-002c-4a4f-b9d8-a396555bdf61)

- O cliente calculou o RTT para cada mensagem enviada.
- Algumas respostas apresentaram RTTs elevados, chegando até ~230 ms, o que pode ser atribuído ao overhead do protocolo TCP.
- O cliente encerrou a conexão após o envio de todas as mensagens.

---

## Comparativo dos resultados

| Protocolo | RTT Mínimo | RTT Máximo | Mensagens Perdidas |
|-----------|------------|------------|--------------------|
| UDP       | ~0.0029 s  | ~0.0612 s  | 0                  |
| TCP       | ~0.0041 s  | ~0.2303 s  | 0                  |

- O **UDP** apresentou menor variabilidade no RTT, com tempos mais curtos e estáveis.
- O **TCP** apresentou maior variação, incluindo picos elevados de RTT, devido aos mecanismos de controle de fluxo e confiabilidade.

## Código do projeto
### Servidor UDP
```python
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
```
### Cliente UDP
```python
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
```
### Servidor TCP
```python
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
```
### Cliente TCP
```python
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
```

## Conclusão

A experiência demonstrou, na prática, as diferenças fundamentais entre UDP e TCP:

- **UDP** é mais rápido, mas não garante entrega nem ordem das mensagens.
- **TCP** é mais confiável, mas adiciona overhead, o que pode aumentar o tempo de resposta.

Ambos os protocolos foram eficazes para o propósito de enviar e receber mensagens de "ping" e "pong", com suas respectivas vantagens e desvantagens.

## Referências
- Documentação oficial Python: https://docs.python.org/3/library/socket.html
- Material de apoio da disciplina Redes de Computadores - UFSC
