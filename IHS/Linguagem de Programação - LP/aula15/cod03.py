import pandas as pd

dados_df = pd.read_excel(r'C:\Users\Tec. Inf - Eddy\OneDrive\Documentos\GitHub\Estudos\IHS\Linguagem de Programação - LP\aula15\produtos_ficticios.xlsx')

# Encontra a linha do produto mais caro e mais barato
caro = dados_df.loc[dados_df['Preço'].idxmax()]
barato = dados_df.loc[dados_df['Preço'].idxmin()]

# Acessa os valores específicos (nome do produto e preço) e formata a saída
print(f'O produto mais caro é {caro["Nome do produto"]} e custa R${caro["Preço"]}.')
print(f'O produto mais barato é {barato["Nome do produto"]} e custa R${barato["Preço"]}.')