import pandas as pd

dados_df = pd.read_excel(r'C:\Users\Tec. Inf - Eddy\OneDrive\Documentos\GitHub\Estudos\IHS\Linguagem de Programação - LP\aula15\produtos_ficticios.xlsx')

dados_df['Valor em Estoque'] = dados_df ['Preço']*dados_df['Quantidade em estoque']

dados_df['Status'] = 'Disponível'

dados_df.loc[dados_df['Quantidade em estoque'] <= 20, 'Status'] = 'Quase acabando'
dados_df.loc[dados_df['Quantidade em estoque'] == 0, 'Status'] = 'Esgotado'

dados_df['Custo médio por Unidade'] = dados_df['Valor em Estoque']/dados_df['Quantidade em estoque']

