from pymongo import MongoClient
import json
import os

# URL de conexão com o banco de dados
url = 'mongodb://localhost:27017/CAT_COMPLETO'
nome = 'cat_não_ENCONTRADOS_CAT_COMPLETO_2021_8'

# Caminho para o diretório onde o arquivo JSON será salvo
diretorio_salvar = 'C:/Users/PREDATOR/Documents/SERVIDOR/appWeb-desenvolvimento/leads'

# Caminho do arquivo JSON com os CPFs
file_path = 'C:/Users/PREDATOR/Documents/SERVIDOR/CPFJSON/CAT_2021_8.json'

def consultar_banco_de_dados():
    client = MongoClient(url)

    try:
        # Verificar se o arquivo JSON existe
        if not os.path.exists(file_path):
            print(f"Arquivo JSON não encontrado: {file_path}")
            return

        database = client.get_database()  # Selecionar o banco de dados
        collections = database.list_collection_names()  # Listar todas as coleções

        # Ler o arquivo JSON com os CATs
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_data = json.load(file)
        except Exception as error:
            print(f"Erro ao ler o arquivo JSON: {error}")
            return

        CAT = [item['CAT_NUMERO'] for item in file_data]

        # Set para armazenar os CATs encontrados
        encontrados = set()

        # Iterar sobre as coleções
        for collection_name in collections:
            collection = database.get_collection(collection_name)

            # Realizar a consulta na coleção atual
            result = collection.find({ 'CAT_NUMERO': { '$in': CAT } })

            for item in result:
                encontrados.add(item['CAT_NUMERO'])

        # Determinar os CATs não encontrados
        nao_encontrados = [cat for cat in CAT if cat not in encontrados]

        # Salvar os CATs não encontrados em um arquivo JSON
        caminho_arquivo_nao_encontrados = os.path.join(diretorio_salvar, f"{nome}_nao_encontrados.json")
        with open(caminho_arquivo_nao_encontrados, 'w', encoding='utf-8') as file:
            json.dump(nao_encontrados, file, indent=2, ensure_ascii=False)
        print(f"CATs não encontrados salvos em: {caminho_arquivo_nao_encontrados}")

    except Exception as error:
        print(f"Erro ao consultar o banco de dados: {error}")
    finally:
        client.close()  # Fechar a conexão com o banco de dados

# Chamar a função para iniciar a consulta
consultar_banco_de_dados()
