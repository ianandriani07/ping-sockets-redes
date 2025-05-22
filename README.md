# Relatório — Exercício de Ping Pong com UDP e TCP

## 🎯 Objetivo

Implementar um sistema cliente-servidor em Python utilizando sockets com as seguintes funcionalidades:

- Cliente envia 10 mensagens de **"ping"** ao servidor.
- O servidor responde com **"pong"** a cada mensagem.
- O cliente calcula o **RTT (Round Trip Time)** de cada interação.
- Implementação realizada com dois protocolos:
  - **UDP (User Datagram Protocol)**
  - **TCP (Transmission Control Protocol)**

---

## ⚙️ Configuração do Experimento

- Linguagem: **Python**
- Protocolos: **UDP e TCP**
- Ambiente de teste: Rede local com endereços IP privados.
- Porta utilizada: **8000**

---

## 🚀 Execução e Resultados

### ✅ UDP — User Datagram Protocol

- **Características**:
  - Não orientado à conexão.
  - Não garante entrega ou ordem.
  - Mais rápido, mas menos confiável.

#### ▶️ Saída do Servidor UDP

- O servidor recebeu **11 pings**.
- Tempo de processamento próximo de **0 segundos** para todas as mensagens.
- O servidor respondeu rapidamente a todas as mensagens.

![Imagem do WhatsApp de 2025-05-20 à(s) 19 45 22_1b8422eb](https://github.com/user-attachments/assets/4222f455-ec63-4112-a643-00eaf180fde6)

---

#### ▶️ Saída do Cliente UDP

- Todas as mensagens receberam resposta **"accepted"**.
- RTT variou entre aproximadamente **0.0029 s** e **0.061 s**.
- Nenhuma mensagem foi considerada perdida.

**Exemplo de resultados:**

| Ping | RTT (s)   |
|-------|----------|
| 1     | 0.015439 |
| 2     | 0.041243 |
| 3     | 0.002929 |
| 4     | 0.009583 |
| 5     | 0.061230 |
| 6     | 0.004998 |
| 7     | 0.005239 |
| 8     | 0.005142 |
| 9     | 0.004268 |
| 10    | 0.004833 |

![Imagem do WhatsApp de 2025-05-20 à(s) 19 45 59_74e20d3a](https://github.com/user-attachments/assets/322a4cb7-2392-49d2-8ddd-3f74158afc45)

---

### ✅ TCP — Transmission Control Protocol

- **Características**:
  - Orientado à conexão.
  - Garante entrega, ordem e integridade dos dados.
  - Mais confiável, mas com maior overhead.

#### ▶️ Saída do Servidor TCP

- O servidor aceitou a conexão de **192.168.3.71**.
- Recebeu todas as mensagens "Ping".
- Alguns pings tiveram tempo de processamento diferente de **zero**, por exemplo: 

  - **Ping 3**: ~0.0159 s
  - **Ping 9**: ~0.0179 s

![Imagem do WhatsApp de 2025-05-20 à(s) 19 47 38_9fbd4b32](https://github.com/user-attachments/assets/ec7d61e5-7193-4d86-82df-3fd1539fde65)

---

#### ▶️ Saída do Cliente TCP

- Todas as mensagens "pong" foram recebidas com sucesso.
- RTT variou mais do que no UDP, com alguns picos elevados.

**Exemplo de resultados:**

| Ping | RTT (s)   |
|-------|----------|
| 1     | 0.008502 |
| 2     | 0.004173 |
| 3     | 0.074939 |
| 4     | 0.003664 |
| 5     | 0.004571 |
| 6     | 0.004503 |
| 7     | 0.079187 |
| 8     | 0.233031 |
| 9     | 0.128301 |
| 10    | 0.119791 |

![Imagem do WhatsApp de 2025-05-20 à(s) 19 48 10_1d5b726d](https://github.com/user-attachments/assets/5c9d2f3d-002c-4a4f-b9d8-a396555bdf61)

---

## 🧐 Análise Comparativa

| Protocolo | Garantia de entrega | Overhead | RTT médio | Variabilidade |
|-----------|---------------------|----------|----------|--------------|
| UDP       | Não                 | Baixo    | Baixo    | Baixa        |
| TCP       | Sim                 | Alto     | Variável | Alta         |

### ✅ UDP
- Mais eficiente.
- RTTs estáveis.
- Não houve perda de pacotes no experimento.

### ✅ TCP
- Mais confiável.
- RTTs mais variáveis e, em alguns casos, altos.
- Ideal para aplicações onde a integridade dos dados é mais importante que a latência.

---

## 📌 Conclusões

- O UDP se mostrou mais rápido e com RTTs menores, como esperado.
- O TCP apresentou maior variabilidade, o que é coerente com o seu comportamento orientado à conexão.
- Nenhuma perda de pacotes foi detectada neste experimento, indicando boas condições da rede local.

---

## 📝 Aprendizados

- Como programar sockets em Python usando **TCP** e **UDP**.
- Como calcular **RTT** de forma simples.
- Diferenças práticas entre **protocolos orientados e não orientados à conexão**.

---

## 💡 Sugestões de aprimoramento

- Introduzir **simulação de perda de pacotes** no servidor.
- Testar em redes com maior latência ou instabilidade.
- Adicionar gráficos de RTT para melhor visualização.
- Implementar **controle de fluxo** no UDP para evitar perda.

---

