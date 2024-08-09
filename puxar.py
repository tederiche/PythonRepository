import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('dados_db.db')
cursor = conn.cursor()

# Listar todas as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

if tables:
    print("Tabelas no banco de dados:", tables)
    # Para cada tabela, listar os dados com paginação
    for table in tables:
        table_name = table[0]
        print(f"\nDados na tabela {table_name}:")
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        row_count = cursor.fetchone()[0]
        print(f"Total de linhas: {row_count}")
        
        page_size = 10000
        for offset in range(0, row_count, page_size):
            cursor.execute(f"SELECT * FROM {table_name} LIMIT {page_size} OFFSET {offset};")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
else:
    print("Nenhuma tabela encontrada no banco de dados.")

# Fechar a conexão
conn.close()
