import os
import pandas as pd

# Caminho do arquivo txt
file_path = 'D:/TXT_EXCEL/2022_bd.txt'

# Diretório de saída
output_dir = 'D:/TXT_EXCEL/saida_de_arquivos'

# Certificar-se de que o diretório de saída existe
os.makedirs(output_dir, exist_ok=True)

# Tamanho do bloco de linhas para ler e processar de cada vez
chunk_size = 500000  # Ajuste conforme necessário

# Inicializando o contador de partes
part_num = 1

# Lendo e processando o arquivo em blocos
for chunk in pd.read_csv(file_path, sep='\t', chunksize=chunk_size, low_memory=False):
    output_file = os.path.join(output_dir, f'arquivo_parte_{part_num}.xlsx')
    chunk.to_excel(output_file, index=False)
    print(f'Parte {part_num} salva em {output_file}')
    part_num += 1

print(f'Processamento concluído. {part_num - 1} arquivos gerados.')
