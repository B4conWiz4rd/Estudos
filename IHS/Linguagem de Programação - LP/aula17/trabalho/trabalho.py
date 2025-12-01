#--------------------------------------------------
# 1. Importação da biblioteca e carregamento
#--------------------------------------------------
import pandas as pd

# Carregar o dataset
df = pd.read_csv('titanic.csv')

# Exibir as primeiras 5 linhas
print(df.head())

#--------------------------------------------------
# 2. Explorando o dataset
#--------------------------------------------------
print(df.info())
print(df.describe())

#--------------------------------------------------
# 3. Exercícios (RESPONDA USANDO CÓDIGO EM PYTHON)
#--------------------------------------------------

# 1) Quantas linhas e colunas o dataset possui?
print("1) Linhas e colunas:", df.shape)

# 2) Qual é a idade média dos passageiros?
print("2) Idade média:", df['Age'].mean())

# 3) Trazer apenas as colunas 'Name' e 'Age'
print("3) Colunas Name e Age:")
print(df[['Name', 'Age']])

# 4) Trazer apenas os passageiros do sexo feminino
print("4) Passageiros do sexo feminino:")
print(df[df['Sex'] == 'female'])

# 5) Trazer apenas passageiros do sexo masculino com idade > 30
print("5) Homens com idade > 30:")
print(df[(df['Sex'] == 'male') & (df['Age'] > 30)])

# 6) Mostrar apenas mulheres sobreviventes
print("6) Mulheres sobreviventes:")
print(df[(df['Sex'] == 'female') & (df['Survived'] == 1)])

# 7) Mostrar passageiros da 1ª classe com menos de 18 anos
print("7) Passageiros da 1ª classe com < 18 anos:")
print(df[(df['Pclass'] == 1) & (df['Age'] < 18)])

# 8) Criar uma coluna chamada 'Faixa' com:
#       - CRIANCA para idade < 18
#       - ADULTO para idade >= 18
df['Faixa'] = df['Age'].apply(lambda x: 'CRIANCA' if x < 18 else 'ADULTO')
print("8) Coluna 'Faixa' criada:")
print(df[['Name', 'Age', 'Faixa']].head())

# 9) Agrupar e mostrar taxa de sobrevivência por sexo
sobrevivencia_por_sexo = df.groupby('Sex')['Survived'].mean()
print("9) Taxa de sobrevivência por sexo:")
print(sobrevivencia_por_sexo)

# 10) Mostrar a tarifa média por classe
tarifa_media_por_classe = df.groupby('Pclass')['Fare'].mean()
print("10) Tarifa média por classe:")
print(tarifa_media_por_classe)

# 11) Qual é a idade da pessoa mais velha do Titanic?
print("11) Idade máxima:", df['Age'].max())

# 12) Qual foi a tarifa mais alta paga no Titanic?
print("12) Tarifa mais alta:", df['Fare'].max())

# 13) Qual classe tinha mais passageiros?
print("13) Classe com mais passageiros:")
print(df['Pclass'].value_counts())

#--------------------------------------------------
# 5. Exportação
#--------------------------------------------------

# 14) Exportar apenas os sobreviventes para um arquivo CSV
sobreviventes = df[df['Survived'] == 1]
sobreviventes.to_csv('sobreviventes.csv', index=False)
print("14) Arquivo 'sobreviventes.csv' exportado com sucesso!")