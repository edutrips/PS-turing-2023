
emails = eval(''+ input('Lista de e-mails: ') +'') #interpreta os emails como uma lista com o eval
    
def conta_economia(emails): #função conta_economia
    compara = []
    iguais = []
    maior = []
    for i in emails:   #lendo os emails um por um
        i = i.split('@')  #separando em duas strings, com e sem @
        i = i[0]  #pegando a string sem @
        #print(i)
        compara.extend(i) #separando letra por letra do email
        #print(compara)
        iguais.append(compara[:])  #copiando as letras para a lista iguais
        count = 0
        count2 = 0
        for c in range(0, len(compara)): #for percorrendo os caracteres da string
            if len(iguais) > 1: # a partir do segundo item da lista iguais
                #print(compara[count])
                #print(iguais[count2][count])
                if iguais[count2][count] == compara[count]: #verificando se os caracteres são iguais na mesma posição
                    #print(iguais[count2][count])
                    count += 1
                    #print(count)
                else:
                    break
        maior.append(count) #adicionando o número de caracteres repetidos na lista
        compara.clear()
    print(sum(maior))#somando os caracteres repetidos
conta_economia(emails)#chamando a função 
#print(iguais)
#https://pt.stackoverflow.com/questions/227170/como-aceitar-uma-lista-como-input
