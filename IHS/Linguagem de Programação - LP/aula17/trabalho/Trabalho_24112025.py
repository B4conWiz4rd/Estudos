"""
Vamos praticar Pandas usando o dataset Titanic.csv.
Este trabalho vale 15 pontos.

Lembre-se: o semestre está acabando e a prova está chegando.
Aprenda!!
"""

#--------------------------------------------------
# 1. Importação da biblioteca e carregamento
#--------------------------------------------------
import pandas as pd
#importe aqui a planilha

print(dataframe_aqui.head())

#--------------------------------------------------
# 2. Explorando o dataset
#--------------------------------------------------
print(df.info())
print(df.describe())

#--------------------------------------------------
# 3. Exercícios (RESPONDA USANDO CÓDIGO EM PYTHON)
#--------------------------------------------------

# 1) Quantas linhas e colunas o dataset possui?
#    Dica: use df.shape


# 2) Qual é a idade média dos passageiros?
#    Dica: mean()


# 3) Trazer apenas as colunas 'Name' e 'Age'


# 4) Trazer apenas os passageiros do sexo feminino


# 5) Trazer apenas passageiros do sexo masculino com idade > 30


# 6) Mostrar apenas mulheres sobreviventes


# 7) Mostrar passageiros da 1ª classe com menos de 18 anos


# 8) Criar uma coluna chamada 'Faixa' com:
#       - CRIANCA para idade < 18
#       - ADULTO para idade >= 18


# 9) Agrupar e mostrar taxa de sobrevivência por sexo


# 10) Mostrar a tarifa média por classe


# 11) Qual é a idade da pessoa mais velha do Titanic?
#     Dica: df['Age'].max()


# 12) Qual foi a tarifa mais alta paga no Titanic?
#     Dica: df['Fare'].max()


# 13) Qual classe tinha mais passageiros?
#     Dica: use value_counts()


#--------------------------------------------------
# 5. Exportação
#--------------------------------------------------

# 14) Exportar apenas os sobreviventes para um arquivo CSV
#     Nome sugerido: sobreviventes.csv
