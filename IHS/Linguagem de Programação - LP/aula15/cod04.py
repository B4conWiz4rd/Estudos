#Liste a lista de produtos da china a cima de 50 unidades

import pandas as pd

dados_df = pd.read_excel(r'C:\Users\Tec. Inf - Eddy\OneDrive\Documentos\GitHub\Estudos\IHS\Linguagem de Programação - LP\aula15\produtos_ficticios.xlsx')

prod = dados_df.loc[dados_df['Quantidade em estoque'] >= 50, ['Nome do produto', 'Quantidade em estoque']]

print(prod)