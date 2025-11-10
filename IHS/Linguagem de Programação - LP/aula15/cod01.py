#INTALAR -> pip install pandas (no terminal)
#INSTALA -> pip install openpyxl (tbm no terminal)
#BAIXAR -> Arquivo XLSX enciado ao e-mail (caso não seja enviado converse com o porfessor)

#PANDAS É UMA BIBLIOTECA PARA ANÁLISE DE DADOS

#IMPORTAR ('as pd' é utilizado para abreviar a biblioteca, repare que ao in´ves de 'pandas' será escrio 'pd')
import pandas as pd

#DECLARE a variável

#DF = DATA FRAME
dados_df = pd.read_excel(r'C:\Users\Tec. Inf - Eddy\OneDrive\Documentos\GitHub\Estudos\IHS\Linguagem de Programação - LP\aula15\produtos_ficticios.xlsx')

#MOSTRA TODA A TABELA NO TERMINAL
#print(dados_df)

#MOSTRA A QUANTIDADE DAS LINHAS E COLUNAS DA TABELA
#print(dados_df.to_string)

#MOSTRA SÓ O CONTEÚDO DAS COLUNAS
#print(dados_df.columns)

#MOSTRA A QUANTIDADE DE LINHAS E COLUNAS DA TABELA
#print(dados_df.shape)

# AQUI VOCÊ SELECIONA APENAS A COLUNA 'Nome do produto' E GUARDA NA VARIÁVEL 'produto'
#produto = dados_df['Nome do produto']

#print(produto)

#=========================================================================================================
#                           FUNÇÃO LOC
#=========================================================================================================

#=== VOCÊ TAMBÉM CONSEGUE PUXAR OUTRAS COLUNAS ===
#produtos = dados_df[['Peso (em kg)', 'Preço']]
#print(produtos)

#=== MOSTRAR CONTEÚDOS QUE VOCÊ ESCOLHE DE COLUNAS ===
#roupas = dados_df.loc[dados_df['Categoria'] == 'Roupas']

#print(roupas)

#=== MOSTRAR CONTEÚDOS QUE VOCÊ ESCOLHE DE COLUNAS, MOSTRA SOMENTE OS PREÇO DAS ROUPAS ===

#preco_roupas = dados_df.loc[dados_df['Categoria'] == 'Roupas', 'Preço']

#print(preco_roupas)

#=== MOSTRA O CONTEÚDO QUE VOCÊ ESCOLHE, MOSTRA TUDO COLUNA COR QUE SEJA PRETO, MOSTRANDO O NOME E PREÇO===

#cor_roupa_peco = dados_df.loc[dados_df['Cor'] == 'Preto', ['Nome do produto', 'Preço']]

#print(cor_roupa_peco)

#=== MOSTRA O CONTEÚDO QUE VOCÊ ESCOLHE, COMBINA DUAS CONDIÇÕES PARA FILTRAR ITENS EM ESPECIFICO ===

#O '&' é para compara e ver se a condição é verdadeira (E, OU)
#produto_cor_df = dados_df.loc[(dados_df['Categoria'] == 'Roupas') & (dados_df['Cor'] == 'Preto')]

#print(produto_cor_df)