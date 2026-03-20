# Conexão MySQL com Python - Explicação do Código

Este projeto demonstra como conectar uma aplicação Python a um banco de dados MySQL e realizar operações básicas de CRUD (Criar, Ler, Atualizar, Deletar).

## 📋 Pré-requisitos

Antes de executar o script `crud_app.py`, certifique-se de ter:

1.  **Python 3.x** instalado.
2.  **Servidor MySQL** rodando (através do XAMPP, WAMP, MySQL Workbench ou serviço nativo).
3.  **Driver MySQL Connector**: Instale a dependência necessária executando:
    ```bash
    pip install mysql-connector-python
    ```

## ⚙️ Configuração da Conexão

No arquivo `crud_app.py`, a conexão é configurada através do dicionário `DB_CONFIG`. É aqui que você define onde o Python deve buscar o banco de dados.

```python
DB_CONFIG = {
    "host": "127.0.0.1",      # Endereço do servidor (localhost)
    "user": "root",           # Usuário do banco (padrão do XAMPP)
    "password": "",           # Senha (padrão vazia no XAMPP)
    "database": "msql_crud_python", # Nome do banco de dados alvo
    "port": 3306              # Porta padrão do serviço MySQL
}
```

> **Atenção**: O banco de dados `msql_crud_python` deve ser criado previamente no seu gerenciador de banco de dados (ex: phpMyAdmin) antes de rodar o script.

## 🚀 Fluxo de Execução

O script executa os seguintes passos dentro de um bloco `try-except-finally` para garantir segurança na conexão:

1.  **Abrir Conexão**: Utiliza `mysql.connector.connect(**DB_CONFIG)` para estabelecer o vínculo com o servidor.
2.  **Criar Cursor**: O `cursor` é o objeto que nos permite enviar comandos SQL para o banco.
3.  **DDL (Definição de Dados)**: Cria a tabela `agenda` (id, nome, telefone), apagando a anterior se existir.
4.  **DML (Manipulação de Dados)**:
    -   **INSERT**: Insere um registro de teste.
    -   **SELECT**: Busca e exibe o registro inserido.
    -   **UPDATE**: Altera o telefone do registro.
    -   **DELETE**: Apaga o registro criado.
5.  **Commit**: Comandos de modificação (INSERT, UPDATE, DELETE) exigem `conn.commit()` para salvar as alterações permanentemente.
6.  **Fechar Conexão**: No bloco `finally`, verificamos se a conexão está ativa e a fechamos para liberar recursos do sistema.

## ▶️ Como Executar

Abra o terminal na pasta do projeto e execute:

```bash
python crud_app.py
```