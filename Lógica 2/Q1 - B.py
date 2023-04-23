#medir o tamanho da string
#dividir ela no meio
#inverter as duas strings
emails = eval(''+ input('Lista de e-mails: ') +'') #interpreta os emails como uma lista com o eval

def corrige_emails(emails):
    metade = []
    corrigido = []
    for i in emails:
        tam = (int(len(i)/2))
        #print(tam)
        #print(i[tam::])
        metade.append(i[0:tam])
        metade.append(i[tam::])
        inteiro = (metade[0][::-1]+metade[1][::-1])
        #print(inteiro)
        orig = inteiro.find('usp.br')
        if orig == -1:
            corrigido.append('ERRO')
        else:
            corrigido.append(inteiro)
        metade.clear()
   
    return corrigido

print(corrige_emails(emails))

