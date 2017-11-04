#funcoes.py

#Usando funções como parametro de tupla
#no exemplo abaixo o parâmetro valores é uma tupla
# #

def nomeFuncao (*valores):
    return valores

#FUNÇÃO map(funcao_definida, lista_elementos)
#
##

def exponencial(base, expo):
    return base**expo

elementos = [1,2,3]
'''
lista = map(exponencial, elementos)

print (lista)

#FUNÇÃO reduce(funcao, sequencia)
#

def soma(val1, val2):
    return val1+val2

#LIST Comprehensions

soma = [x**2 for x in [1,2,3,4]]

print (soma)

soma = [(x,x**2) for x in range(6)]

print (soma)

valores = ((2,3), (6,7), (10,11))

soma = [a*b for (a,b) in valores]

print (soma)

'''
def fatorial(numero):
    if (numero == 1 or numero == 0):
        return 1
    
    return numero*fatorial(numero-1)


fat = fatorial (6)

print ("Fatoria de 6 é: " + str(fat))