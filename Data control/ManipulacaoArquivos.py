#Funcao OPEN para abrir arquivos

arquivo = open('endereco/nom_arquivo', 'opcoes de abertura')


'''
#opcoes de abertura
r - abrir o arquivo apenas para leitura
a - abrir o arquivo para escrita, adicionando lihas no final do arquivo (append)
w - abrir o arquivo para escrita, porém esse modo sobrescreve o arquivo. Logo é usado para criar um aquivo novo

'''


#Metodo close() fecha o arquivo
arquivo.close()

#Metodo write(string) escreve no arquivo
#\n salta uma linha dentro do arquivo
arquivo.write('TESTE')

#Metodo de leitura readline() que permite ler uma linha por vez e no final retorna um string ''
arquivo.readline()

#Metodo de leitura readlines() que permite ler todo o conteudo do arquivo retornando isso em uma lista
lista = arquivo.readlines()
