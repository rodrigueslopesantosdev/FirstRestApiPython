

# values = int(input("Enter the value: "))
#
# while (values > 0):
#     print ("Value: " + str(values))
#     values -= 1 #values = values - 1
#
# list = [1,2,3,4]
#
# for i in list :
#     print(i)
#
# #Range delimita o limite real da lista. range(inicio, fim [,salto de posicao])
# for i in range(1, len(list)) :
#     print(i, list[i])

lista2 = [1,2,3]
lista3 = [4,5,6]
matriz = [lista2, lista3]

for rows in range(len(matriz)):
    for columns in range (len(matriz)):
        print("Valores Matriz: [" + str(rows) +"]["+ str(columns) + "] = " + str(matriz[rows][columns]))

#BLOCO TRY EXCEPT

try:
    valores = input("Informe o valor: ")

    print ("Valor: " + valores)

except:
    print("Ocorreu um erro no bloc TRY ao ler um valor do teclado.")