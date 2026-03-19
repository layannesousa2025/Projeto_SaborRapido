import mysql.connector

# Configurações do banco
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "",  # No XAMPP normalmente é vazio
    "database": "msql_crud_python",
    "port": 3306
}

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    print("Conexão com o Banco de Dados aberta com sucesso!")
    cur = conn.cursor()

    # Criar tabela
    cur.execute("DROP TABLE IF EXISTS agenda")
    cur.execute("""
        CREATE TABLE agenda (
            id INT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            telefone VARCHAR(12)
        )
    """)
    conn.commit()
    print("Tabela criada com sucesso!")

    # Inserir
    cur.execute("INSERT INTO agenda (id, nome, telefone) VALUES (1, 'Pessoa 1', '02199999999')")
    conn.commit()
    print("Inserção realizada com sucesso!")

    # Consultar
    cur.execute("SELECT * FROM agenda WHERE id=1")
    registro = cur.fetchone()
    print("Consulta antes da atualização:", registro)

    # Atualizar
    cur.execute("UPDATE agenda SET telefone='02188888888' WHERE id=1")
    conn.commit()
    print("Registro atualizado com sucesso!")

    # Excluir
    cur.execute("DELETE FROM agenda WHERE id=1")
    conn.commit()
    print(cur.rowcount, "Registro excluído com sucesso!")

except Exception as e:
    print("Ocorreu um erro:", e)

finally:
    if conn.is_connected():
        cur.close()
        conn.close()
        print("Conexão fechada.")
