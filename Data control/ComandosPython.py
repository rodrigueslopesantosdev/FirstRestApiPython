
#OPERAÇÕES COM PONTOS FLUTUANTES
# 2*9 = 19
# 2*9. = 18.0
# 1/3. = 0.333333333
# 1+2 = 3
# 1+2. = 3.0
##

#imput
nome = input("Digite seu nome")

#Atribuições
a,b = 0, "Deu certo?"

print("O A: " + str(a))
print ("O B: " + str(b))

#exponencial 2^3
x = 2**3

a = 2
b = 3

if (a==b):
    print ("a é igual a b")
else :
    print ("a é diferente de B")


#diferente pode ser espcificado como a!=b ou a<>b
if (a!=b):
    print("A é diferente de B")
else :
    print("A é igual a B")


#função type mostra qual o tipo do objeto

print(type(x))

#
#Tipos de objetos em Python: int, float, string, listas, tuplas, dicionários
#para transformar um valor em outro basta usar as seguintes funções:
#   int(valor1)  : transforma o valor1 em inteiro
#   float(valor2): transforma o valor2 em float
#   str(valor3)  : transforma o valor3 em string
#  #


#==================================STRINGS=================================#
#Os string não são mutáveis, logo não é possível alterar o valor de uma posição do string
palavra = "termocinética"
print(palavra)
#Acesso a posição da string
print("Posição 0 da palavra: " + palavra[0])
#Repetição da posição da string ou da palavra completa
print("2 X A Posição 0 da palavra: " + 2*   palavra[0])
#Acesso um intervalo dentro da string
print ("Palavra estudada: " + palavra)
print ("Intervalo do caracter 5 a 9: " + palavra[5:9])
print ("Intervalo aberto caracter 5 até o fim: " + palavra[5:])
print ("Intervalo aberto caracter do início até a posição 5: " + palavra[:5])
print ("Intervalo da string com incremento de 2 posições: " + palavra[1:9:2])
#Inverso da string
print ("Inverso da string: " + palavra[::-1])
#Tamanho do string
print ("Tamanho do string: " + str(len(palavra)))



#==================================LISTAS=================================#
#As listas são mutáveis, podendo os valores dentro das listas serem alterados
lista1 = [1,2,3,4]
#Acesso a lista normal
print ("Posição 0 da lista1: " + str(lista1[0]))
#Concatenando duas listas
lista1 = lista1 + [5,6]
print("Posição 5 da lista1: " + str(lista1[5]))
print("Posição lista1[2:-2]: " + str(lista1[2:-2]))
lista1[2] = 10
print("Posição lista1[2]: " + str(lista1[2]))
#O Append adiciona o valor no fim da lista append(valor). Se o valor for uma lista ele será adicionado como uma lista inteira
#em uma posição.
lista1.append('Tiago')
print("Append da lista1: " + str(lista1))
#O Extend adiciona uma lista interia no final de outra lista extend([1,2,3])
lista1.extend([10,20,30])
print("Extend da lista1: " + str(lista1))
#O insert adiciona um valor em uma posição especificada. insert(posicao, valor)
lista1.insert(1, "Luciana")
print("Insert na posição 1 da lista1: " + str(lista1))
#O remove retira um valor da lista com o valor especificado. remove('Tiago')
lista1.remove('Tiago')
print("Remove na posição Tiago da lista1: " + str(lista1))
#O Pop remove o valor da lista, mas tem que especificar a posição e não o valor. pop(posicao)
lista1.pop(0)
print("Pop tira da lista1: " + str(lista1))
#O count retorna quantas vezes o valor passado no parâmetro existe dentro da lista. count(valor), ex: count(10) ou count("Luciana")
print("Count 10 da lista1: " + str(lista1.count(10)))
print("Count Luciana da lista1: " + str(lista1.count('Luciana')))
#Assim com os strings podemos inverter as listas
print("Lista1 invertida: " + str(lista1[::-1]))
#==================================MATRIZES=================================#
lista2 = [1,2,3]
lista3 = [4,5,6]
matriz = [lista2, lista3]
print("Matriz na posição 0,2: " + str(matriz [0][2]))

#==================================TUPLAS=================================#
#As tuplas são imutáveis assim como os strings
tupla1 = (1,2,'casa')
print ("Tupla na posição 2 e 0: " + str(tupla1[2]) + " e " + str(tupla1[0]))

#==================================DICIONÁRIOS=================================#
#Dicionários são Mutáveis, ou seja, aceitam valores atribuídos. Sua construção sempre leva um par de valores, chave + valor
#São declarados usando {} e não [].
aurelio = {'casa':'lugar onde vive', 'carro': 'veículo que anda'}
#atribuição em dicionários é representada por [] e não por {}.
aurelio ['esposa'] = 'aquela com quem o home vai casar'

print("Termo CARRO: " + str(aurelio['carro']))
#Mostra chaves de um dicionário keys()
print("Chaves de um dicionário: " + str(aurelio.keys()))
#Testa se uma chave existe: has_key()
# if  (aurelio.has_key("carro")):
#     print("A chave TERRA existe")
# else:
#     print("A chave TERRA não existe")
#Mostra os itens do dicionário, items() retorna uma tupla com o par (chave, valor)
print(aurelio.items())


#==================================SAÍDA FORMATADA=================================#
constante = 3.14124124535489609
print("O valor da constante é: %3.5f " %constante)
nome = "Tiago Rodrigues Lopes dos Santos"


input("Pressione ENTER")