#EXERCICIO
#MOSTRE O NOME E PREÇOS DOS PRODUTOS A CIMA DE 300

import pandas as pd

dados_df = pd.read_excel(r'C:\Users\Tec. Inf - Eddy\OneDrive\Documentos\GitHub\Estudos\IHS\Linguagem de Programação - LP\aula15\produtos_ficticios.xlsx')
#REPARE QUE A CONDIÇÃO PARA QUE SEJA MOSTRADO UM PRECO (NÚMERO INTEIRO) MAIOR QUE 300
produto = dados_df.loc[dados_df['Preço'] >= 300 , ['Nome do produto', 'Preço']]

print(produto)

#ESPECIFICA O CONTEÚDO DA COLUNA ESCOLHIDA (Código do produto) DA LINHA ESCOLHIDA (5)
print(dados_df.loc[5, 'Código do produto'])