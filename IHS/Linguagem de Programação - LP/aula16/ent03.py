import pandas as pd

dados_df = pd.read_excel(r'C:\Users\Tec. Inf - Eddy\OneDrive\Documentos\GitHub\Estudos\IHS\Linguagem de Programação - LP\aula15\produtos_ficticios.xlsx')

dados_df['Frete'] = 0

dados_df.loc[dados_df['Categoria'] == 'Roupas', 'Frete']= 12.90
dados_df.loc[dados_df['Categoria'] == 'Eletrônicos', 'Frete']= 25.0
dados_df.loc[dados_df['Categoria'] == 'Acessórios', 'Frete']= 8.5
dados_df.loc[dados_df['Categoria'] == 'Calçados', 'Frete']= 15.0

dados_df.to_excel('produtos_ficticios4.xlsx', index=False)