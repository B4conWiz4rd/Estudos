import pandas as pd

dados_df = pd.read_excel(r'C:\Users\Tec. Inf - Eddy\OneDrive\Documentos\GitHub\Estudos\IHS\Linguagem de Programação - LP\aula15\produtos_ficticios.xlsx')

dados_df['Valor em Estoque'] = dados_df ['Preço']*dados_df['Quantidade em estoque']

dados_df['Imposto (Ebaaa)'] = dados_df ['Valor em Estoque']*0.03

dados_df['Valor Final'] = dados_df['Valor em Estoque'] - dados_df['Imposto (Ebaaa)']

dados_df.to_excel('produtos_ficticios3.xlsx', index=False)