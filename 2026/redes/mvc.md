# Guia Prático: A Arquitetura MVC para Desenvolvedores Web em Python

No guia anterior, criámos um servidor Web básico onde o código HTML, a lógica do servidor e os dados estavam todos misturados dentro da mesma função (`do_GET`). 

Para aplicações reais, misturar tudo gera caos. É por isso que usamos padrões de arquitetura como o **MVC (Model-View-Controller)**. O MVC divide a sua aplicação em três partes isoladas, facilitando a manutenção do código.

---

## 1. O que significa MVC?

Imagine que o MVC é a equipa de um restaurante de fast-food:

*   **Model (O Modelo / A Cozinha):** É onde ficam os dados e as regras de negócio da sua aplicação. É quem sabe como aceder à base de dados, validar informações e fazer contas. (No restaurante: a cozinha que prepara o hambúrguer).
*   **View (A Vista / A Embalagem):** É a interface visual que o utilizador final vê (HTML, CSS, JSON). Ela apenas exibe os dados que recebe, sem saber de onde vieram. (No restaurante: a caixa bonita onde o hambúrguer é servido).
*   **Controller (O Controlador / O Atendente):** É o intermediário. Ele recebe a requisição HTTP do utilizador, decide qual *Model* deve processar a informação e escolhe qual *View* será exibida de volta. (No restaurante: o atendente do caixa que recebe o pedido, passa à cozinha e entrega o pacote ao cliente).

---

## 2. O Fluxo do MVC na Web (HTTP)

Quando liga a pilha TCP/IP ao padrão MVC, o fluxo de uma requisição funciona assim:

```text
[ Utilizador / Navegador ] 
       │      ▲
       │ (1)  │ (4) Devolve a View (HTML)
       ▼      │
┌────────────────────────┐
│ CONTROLLER             │ ◄───┐
└────────────────────────┘     │ (3) Envia os dados brutos
       │                       │     para o Controller
       │ (2) Pede os dados     │
       ▼                       │
┌────────────────────────┐   ┌────────────────────────┐
│ MODEL                  │ ──┘│ VIEW                   │
│ (Dados / Lógica)       │    │ (Interface / HTML)     │
└────────────────────────┘    └────────────────────────┘
```

---

## 3. Código Prático: Implementando MVC com Python Nativo

Vamos reorganizar o nosso servidor `http.server` do Python para seguir uma estrutura MVC simplificada. 

Crie um ficheiro chamado `app_mvc.py`:

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# ==========================================
# 1. MODEL (Camada de Dados e Lógica)
# ==========================================
class ProdutoModel:
    @staticmethod
    def listar_todos():
        # Numa aplicação real, estes dados viriam de uma Base de Dados (SQL)
        return [
            {"id": 1, "nome": "Notebook Python Pro", "preco": 4500.00},
            {"id": 2, "nome": "Roteador TCP/IP Turbo", "preco": 299.90}
        ]


# ==========================================
# 2. VIEW (Camada de Apresentação/Visual)
# ==========================================
class ProdutoView:
    @staticmethod
    def renderizar_lista_html(produtos):
        # Transforma os dados puros em código HTML legível para o navegador
        linhas_tabela = ""
        for p in produtos:
            linhas_tabela += f"<tr><td>{p['nome']}</td><td>{p['preco']}€</td></tr>"
            
        html = f"""
        <html>
            <head><title>Loja MVC</title></head>
            <body>
                <h1>Lista de Produtos (Via MVC)</h1>
                <table border='1'>
                    <tr><th>Produto</th><th>Preço</th></tr>
                    {linhas_tabela}
                </table>
            </body>
        </html>
        """
        return html


# ==========================================
# 3. CONTROLLER (O intermediário no Servidor HTTP)
# ==========================================
class LojaController(BaseHTTPRequestHandler):
    def do_GET(self):
        # O Controller analisa a rota (URL) pedida na camada HTTP
        if self.path == "/produtos":
            # 1. Controller pede os dados ao Model
            dados_produtos = ProdutoModel.listar_todos()
            
            # 2. Controller envia os dados para a View gerar o HTML
            html_final = ProdutoView.renderizar_lista_html(dados_produtos)
            
            # 3. Controller responde ao cliente via protocolo HTTP
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_final.encode("utf-8"))
            
        else:
            # Rota não encontrada
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Pagina nao encontrada (404)")


# ==========================================
# INICIALIZAÇÃO DO SERVIDOR (Infraestrutura)
# ==========================================
if __name__ == "__main__":
    endereco = ("localhost", 8000)
    servidor = HTTPServer(endereco, LojaController)
    print("Servidor MVC ativo em http://localhost:8000/produtos")
    servidor.serve_forever()
```

---

## 4. Por que razão isto é útil para si?

Se o chefe da empresa pedir para alterar o design do site, altera apenas o código da **View**. O código que mexe com os dados (Model) permanece intacto. 

Se decidir trocar o local onde guarda os dados (mudar de um ficheiro de texto para uma base de dados Postgres), altera apenas o **Model**. A interface visual (View) não precisa de saber dessa mudança.

Esta separação de responsabilidades permite que o seu código Python cresça de forma limpa e organizada.
