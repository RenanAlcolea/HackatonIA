import pandas as pd
import numpy as np
import csv

# Carregando o arquivo CSV
data = pd.read_csv("Logs_eni-03ab7af9546ef7cce-all.csv", header=None, names=['Timestamp', 'Message'])

print(data.columns)

# Atualizando a coluna 'Timestamp' com o conteúdo da coluna 'Message'
data['Timestamp'] = data['Timestamp'] + ' ' + data['Message']

# Removendo a coluna 'Message'
data.drop('Message', axis=1, inplace=True)

# Exibindo as primeiras linhas do dataframe atualizado
print(data.head())

# Remover a primeira linha
data = data.drop(0)

# Resetar o índice se desejar que ele comece de 0 novamente
data = data.reset_index(drop=True)

# Save Clean CSV
data.to_csv("Ready_to_start.csv", index=False, header=False, sep=',')


import pandas as pd
import csv

def add_commas_to_csv(file_path, output_file_path):
    # Carregar o arquivo CSV
    df = pd.read_csv(file_path)

    # Adicionar vírgulas entre as palavras onde há espaço
    df_transformed = df.apply(lambda col: col.apply(lambda x: ', '.join(x.split()) if isinstance(x, str) else x))

    # Salvar o DataFrame transformado em um novo arquivo CSV, sem adicionar aspas e com um caractere de escape
    df_transformed.to_csv(output_file_path, index=False, quoting=csv.QUOTE_NONE, escapechar='\\')

# Exemplo de uso
input_file_path = 'Ready_to_start.csv'
output_file_path = 'Ready_to_start.csv2'
add_commas_to_csv(input_file_path, output_file_path)







