# 1.  Escreva um código que lê a lista abaixo e faça a leitura do tamanho da lista, do maior e menor valor e da soma dos valores da lista.

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

# Tamanho da lista
tam = len(lista)

# Maior e menor número
maior = max(lista)
menor = min(lista)

# Soma dos elementos da lista
soma = sum(lista)

print(f"A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores  presentes nela é igual a {soma}.")

# 2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária.

numero = int(input('Digite um número de 1 a 10:'))

def tabuada(numero):
    print(f'Tabuada do {numero}')
    for i in range(11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')

tabuada(numero)

# 3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3: 

# Lista gerada
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

# declarando a lista de multiplos de 3 
mult_3 = []
# função para gerar uma lista dos múltiplos de 3 a partir de uma lista
def multiplo_3(lista: list) -> list:
  for i in range(len(lista)):
    # condição para um número ser múltiplo de 3
    if lista[i] % 3 == 0:
      mult_3.append(lista[i])
  return mult_3

# retornando a lista gerada para a variável mult_3
mult_3 = multiplo_3(lista)
print(mult_3)


# 4. Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = lambda x: x**2
resultado = list(map(quadrado,lista))
print(resultado)


'''
# 5. Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.
Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:
"Nota da manobra: [media]"
'''
notas = []
for i in range(1,6):
    nota = float(input(f'Digite a {i}ª nota:'))
    notas.append(nota)

def media(lista):
    lista.remove(max(lista))
    lista.remove(min(lista))
    return sum(lista)/len(lista)

media = media(notas)
print(f"Nota da manobra: {round(media, 1)}")

'''
# 6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:

maior nota
menor nota
média
situação (Aprovado(a) ou Reprovado(a))
'''

notas =[]

for i in range(1,5):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

def aluno(lista):
    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)
    if media >=6:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'

    return (media, maior, menor, situacao)
 
media, maior, menor, situacao = aluno(notas)

print(f"O(a) estudante obteve uma media de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}")


'''
# 7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome.
'''
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

for n in nome_completo:
    print(f'Nome completo: {n}')

'''
# 8. Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.
'''

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

def calcula_pontos(gols_marcados, gols_sofridos):
  pontos = 0
  for i in range(len(gols_marcados)):
    if gols_marcados[i] > gols_sofridos[i]:
      pontos += 3
    elif gols_marcados[i] == gols_sofridos[i]:
      pontos += 1
  aproveitamento = 100 * pontos / (len(gols_marcados) * 3)
  return (pontos, aproveitamento)

pontos, aproveitamento = calcula_pontos(gols_marcados, gols_sofridos)
print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {round(aproveitamento)}%")

'''
# 9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.
O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.
Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).
Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.
'''
dias = int(input("Quantas diárias? "))
cidade = input("Qual a cidade? [Salvador, Fortaleza, Natal ou Aracaju]: ")
distancias = [850, 800, 300, 550]
passeio = [200, 400, 250, 300]
km_l = 14
gasolina = 5

def gasto_hotel(dias):
    return 150 * dias

def gasto_gasolina(cidade):
    if cidade == "Salvador":
        return (2 * distancias[0] * gasolina) / km_l 
    elif cidade == "Fortaleza":
        return (2 * distancias[1] * gasolina) / km_l 
    elif cidade == "Natal":
        return (2 * distancias[2] * gasolina) / km_l 
    elif cidade == "Aracaju":
        return (2 * distancias[3] * gasolina) / km_l 

def gasto_passeio(cidade, dias):
    if cidade=="Salvador":
        return passeio[0] * dias
    elif cidade=="Fortaleza":
        return passeio[1] * dias
    elif cidade=="Natal":
        return passeio[2] * dias 
    elif cidade=="Aracaju":
        return passeio[3] * dias 

gastos = gasto_hotel(dias) + gasto_gasolina(cidade) + gasto_passeio(cidade, dias)
print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {round(gastos, 2)} reais")


'''
# 10. Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.
'''

frase = input("Digite uma frase: ")
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

tamanho = list(filter(lambda x: len(x) >= 5, frase))
print(tamanho)
