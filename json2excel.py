import json
import pandas as pd

# Carrega o arquivo JSON
with open('cat_não_ENCONTRADOS_CAT_COMPLETO_2021_8_nao_encontrados.json', 'r') as file:
    data = json.load(file)

# Converte a lista para um DataFrame
df = pd.DataFrame(data, columns=["Código"])

# Salva em um arquivo Excel
df.to_excel('2021_8_cat_não_encontrado.xlsx', index=False)

print("Arquivo Excel criado com sucesso!")
