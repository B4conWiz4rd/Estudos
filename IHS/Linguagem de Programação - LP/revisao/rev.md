📝 Prova de Revisão – Python Básico
1) Tipos de dados

1.1 Qual é o tipo de dado da variável abaixo?

altura = 1.75

1.2 Qual dos tipos abaixo representa textos?
-> a) int
b) float
c) str
d) bool

1.3 O que significa o tipo bool?

r-são os dados lógicos, true ou false

1.4 Verdadeiro ou falso:
“Toda entrada do input() vem como string.”
r- Verdadeiro! Para que vá como int ou float, você deve delifini-la
1.5 Escreva um exemplo válido de cada tipo:

int = 18

float = 1,75

str = Edmilson

bool = True

2) Variáveis

2.1 Por que usamos variáveis em Python?
a) Para decorar códigos
->b) Para armazenar valores
c) Para pular linhas
d) Para deixar o código colorido

2.2 Qual dos nomes de variável abaixo é inválido?
a) nome_aluno
b) idade2
-> c) 2nota
d) nota_final

2.3 Qual será a saída?

nota1 = 8
nota2 = 6
media = (nota1 + nota2) / 2
print(media)

r - A saida (print) será = 7

3) Input

3.1 O que o comando input() faz?

r -O usuário colocará o tipo de informação/dado, válido

3.2 Como converter um input para inteiro?

r- input(int(print="Digite a sua idade: "))

3.3 Qual é o tipo da variável idade?

idade = input("Digite sua idade: ")

r- A variável será validade como str, já que não foi definida corretamente como inteiro

4) Condições (if / elif / else)

4.1 Complete:
O bloco usado para testar condições é o ______, seguido de ______ e ______.

r- 1 if, 2 elif, 3 else

4.2 Qual operador significa “diferente”?
a) ==
b) !=
c) and
-> d) or

4.3 O que será impresso?

nota = 4
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

A saida será reprovado, já que a condição aprovado é só se for maior ou igaul a 7, recuperação maior ou igual a 5 e por fim recuperação se não conprir as demais condoções

4.4 O operador and significa:
a) ou
b) negar
-> c) e
d) dividir

4.5 O que acontece?

idade = 18
tem_carteira = False

if idade >= 18 and tem_carteira:
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")

r - Não pode dirigir, já que não cumpre um dos requisitos solicitados, (tem_carteira = False)

5) Laços de repetição

5.1 O que será exibido?

for i in range(3):
    print(i)

r- sairá o seguinte: 1, 2, 3

5.2 Para que serve o comando range()?

r- Ele contará passos, por exemplo para contador for verdadeiro, deve fazer 3 passos

5.3 Quantas vezes a mensagem aparece?

contador = 1
while contador <= 5:
    print("Oi")
    contador += 1

r- O print repetirá 5 vezes
5.4 Qual loop é mais apropriado quando não sabemos quantas vezes repetir?
->a) for
b) while

6) Listas

6.1 Qual é o índice inicial de uma lista?
r- o nome ao qual a lista se refere
6.2 Qual comando adiciona um item?
a) add()
b) insert()
-> c) append()
d) push()

6.3 O que faz?

frutas[1] = "abacaxi"

armazena uma lista de frutas, sendo a casa 1, denominada como "abacaxi"

6.4 O que acontece?

frutas = ["maçã", "banana"]
frutas.remove("banana")

r- a casa 1 (já que a ordem das listas começam com zero) é removido.

7) Dicionários

7.1 Dicionários armazenam dados no formato:
a) índice → valor
->b) chave → valor
c) texto → número
d) lista → item

7.2 Como acessar o valor da chave "nome"?

aluno = {"nome": "Pedro", "idade": 17}

r- print = (aluno ["nome"])

7.3 Como alterar a nota?

aluno["nota"] = 8

r- o comando alterará a nota do dicionário do aluno Pedro

7.4 Como adicionar a chave "turma"?

aluno = ["turma"] = "2B"

8) Funções

8.1 Para que servem as funções?

r- para puxar programções ja pré moldadas pelo programador, por exemplo o import

8.2 O que retorna?

def soma(a, b):
    return a + b

print(soma(2, 4))

r- retornará a soma, o resultado é 6

8.3 O que o comando return faz?

r- no caso fará o calculo do primeiro número definido como a, e o sgeundo númnero definido como b

8.4 Complete:
Uma função com parâmetros recebe valores ______ quando é ______.

9) Importação de bibliotecas

9.1 O que significa importar bibliotecas?

9.2 Para que serve o pandas?

9.3 Qual instrução está correta?
a) import math
b) include math
c) upload math
d) using math

9.4 Cite dois motivos para importar bibliotecas.

10) PyAutoGUI

10.1 Qual comando move o mouse?

10.2 Qual comando escreve texto?

10.3 O que faz pyautogui.press("enter")?

10.4 Por que usamos time.sleep() em automações?

11) Pandas

11.1 Para que serve o pandas?

11.2 Como carregar um CSV?

11.3 O que faz df.head()?

11.4 Qual comando mostra estatísticas básicas?