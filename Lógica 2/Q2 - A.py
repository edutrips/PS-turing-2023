from pilha import Stack

s = Stack()
comandos = []
tam = int(input('Tamanho da pilha: '))
#def estacionamento_ok(tam, comandos):
  #  for i in tam:

while True: #adiciono os comandos numa lista
   n = input('Comando: [aperte enter ao finalizar]')
   if n == '':
      break
   else:
      n = int(n)
      comandos.append(n)
def estacionamento_ok(tam, comandos):
    for i in comandos: #leio a lista de comandos um por um
        if i > 0:
            if (s.size() == tam): # se a pilha estiver maior que o tamanho que eu estimei, retorno 'nao'
                return 'nao'
            else:
                s.push(i)  #adiciono na pilha
                #print(f'tamanho da lista {s.size()}')
                #print(f'topo da lista: {s.peek()}')
        elif i < 0: 
            if s.size() == 0: # se a pilha estiver vazia, retorno 'nao'
                return 'nao'
            else:#se não, comparo o topo da pilha com o elemento que quero remover
                if abs(i) == s.peek():#se forem iguais, eu removo
                    s.pop()
                    #print(f'tamanho da lista {s.size()}')
                    #print(f'topo da lista: {s.peek()}')
                else: # se não, retorno 'nao'
                    return 'nao'
    if s.size() == 0:
        return 'sim'              
print(estacionamento_ok(tam, comandos))



      

