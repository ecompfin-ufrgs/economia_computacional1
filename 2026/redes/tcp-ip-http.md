# Guia Prático: A Pilha TCP/IP e a Web para Programadores Python

Para criar aplicações Web, não basta enviar bits pelo cabo. Os computadores precisam de falar a mesma língua. Essa língua é a **Pilha de Protocolos TCP/IP**.

Este guia explica como a Web funciona em camadas e como criar um servidor Web real usando apenas as ferramentas nativas do Python.

---

## 1. A Pilha TCP/IP: O Modelo de 4 Camadas

Imagine a rede como o serviço de correios. Para enviar uma carta (dados), ela passa por vários processos. No TCP/IP, dividimos esses processos em **4 camadas**. 

Cada camada adiciona informação (um cabeçalho) aos seus dados e passa-os para a camada inferior.

```text
+-----------------------+  -> Camada de Aplicação (Ex: HTTP - O seu site)

|  APLICAÇÃO (HTTP)     |
+-----------------------+  -> Camada de Transporte (Ex: TCP - Garante a entrega)

|  TRANSPORTE (TCP)     |
+-----------------------+  -> Camada de Rede (Ex: IP - Encontra o caminho/endereço)

|  REDE (IP)            |
+-----------------------+  -> Camada Física/Acesso (Ex: Ethernet/Wi-Fi - Os cabos)

|  FÍSICA (Interface)   |
+-----------------------+
```

---

## 2. Como as camadas interagem na Web

Quando acede a um site ou cria uma API, quatro protocolos trabalham juntos:

1. **HTTP (Aplicação):** É o formato da mensagem. Define que o cliente faz uma *Requisição* (Request) e o servidor devolve uma *Resposta* (Response) em formato de texto estruturado.
2. **TCP (Transporte):** Pega no texto do HTTP, divide-o em pedaços e garante que nenhum pedaço se perde. Abre um canal de comunicação direto entre o cliente e o servidor através de uma **Porta** (a Web usa por padrão a porta `80` ou `443`).
3. **IP (Rede):** Coloca o endereço do destinatário (IP de destino) e do remetente (IP de origem) em cada pedaço. É o GPS da rede.
4. **Física (Interface):** Transforma tudo em sinais elétricos ou luz e envia pelo cabo.

---

## 3. O Fluxo de uma Requisição Web (HTTP)

O protocolo HTTP é puramente baseado em texto. Quando o seu navegador pede uma página, ele envia uma mensagem TCP estruturada assim:

```text
GET / HTTP/1.1
Host: localhost:8000
User-Agent: Navegador
```

O servidor lê esse texto e responde de volta no mesmo canal TCP:

```text
HTTP/1.1 200 OK
Content-Type: text/html

<h1>Ola do Servidor Python!</h1>
```

---

## 4. Código Prático: Criando um Servidor Web em Python

Para entender como a camada de Aplicação (HTTP) roda em cima da camada de Transporte (TCP), vamos usar a biblioteca padrão do Python. 

### Abordagem Baixo Nível (Camada TCP pura)
Se usássemos apenas `socket`, teríamos de ler o texto do HTTP manualmente. É assim que um servidor Web lê os dados vindos do TCP:

```python
import socket

# Configura o Socket TCP (Camada de Transporte)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8000))
server.listen(1)

print("Servidor TCP aguardando conexões na porta 8000...")

while True:
    connection, address = server.accept()
    # Recebe os dados brutos que o navegador enviou (Camada de Aplicação HTTP)
    request = connection.recv(1024).decode('utf-8')
    print(f"Requisição recebida:\n{request}")
    
    # Monta a resposta manual no formato HTTP
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nOla do Socket TCP!"
    connection.sendall(response.encode('utf-8'))
    connection.close()
```

### Abordagem Alto Nível (Camada HTTP Nativa)
Como programar sockets TCP manualmente para a Web dá muito trabalho, o Python traz um módulo nativo que já entende a camada HTTP: o `http.server`.

Crie um ficheiro chamado `servidor.py` com o código abaixo:

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

# Define o comportamento da nossa Camada de Aplicação (HTTP)
class MeuHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Envia o código de status HTTP (200 significa Sucesso)
        self.send_response(200)
        
        # 2. Envia os cabeçalhos HTTP (Informa o tipo de conteúdo)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        # 3. Envia o corpo da resposta (O HTML que aparece na página)
        html = "<html><body><h1>Servidor Web Python Funciona!</h1></body></html>"
        self.wfile.write(html.encode("utf-8"))

# Configura o endereço IP local (localhost) e a Porta TCP (8000)
endereco = ("localhost", 8000)

# Inicializa o servidor que junta o TCP (rede) com o nosso Handler (HTTP)
servidor_web = HTTPServer(endereco, MeuHandler)

print("Servidor Web ativo em http://localhost:8000")
servidor_web.serve_forever()
```

### Como testar:
1. Execute o código no seu terminal: `python servidor.py`
2. Abra o seu navegador Web.
3. Visite o endereço: `http://localhost:8000`

O `HTTPServer` geriu a ligação TCP, o endereço IP e os sockets em segundo plano, permitindo que se focasse apenas na lógica do protocolo HTTP.

[próxima](mvc.md)
