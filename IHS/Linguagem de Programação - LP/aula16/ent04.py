import pandas as pd

dados_df = pd.read_excel(r'C:\Users\Tec. Inf - Eddy\OneDrive\Documentos\GitHub\Estudos\IHS\Linguagem de Programação - LP\aula15\produtos_ficticios.xlsx')

dados_df['Valor em Estoque'] = dados_df ['Preço']*dados_df['Quantidade em estoque']

dados_df['Imposto (Ebaaa)'] = dados_df ['Valor em Estoque']*0.03

dados_df['Valor Final'] = dados_df['Valor em Estoque'] - dados_df['Imposto (Ebaaa)']

dados_df['Status'] = 'Disponível'

dados_df.loc[dados_df['Quantidade em estoque'] <= 20, 'Status'] = 'Quase acabando'
dados_df.loc[dados_df['Quantidade em estoque'] == 0, 'Status'] = 'Esgotado'

dados_df['Custo médio por Unidade'] = dados_df['Valor em Estoque']/dados_df['Quantidade em estoque']

dados_df['Frete'] = 0

dados_df.loc[dados_df['Categoria'] == 'Roupas', 'Frete']= 12.90
dados_df.loc[dados_df['Categoria'] == 'Eletrônicos', 'Frete']= 25.0
dados_df.loc[dados_df['Categoria'] == 'Acessórios', 'Frete']= 8.5
dados_df.loc[dados_df['Categoria'] == 'Calçados', 'Frete']= 15.0

dados_df.to_excel('planilha_aula16.xlsx', index=False)