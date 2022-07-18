#Nome: Riane Carla Gomes Alves
#Matrícula: 508771
#Turma: 01

def vazio(lista):
    return lista == []
#Retorna verdadeiro ou falso indicando se a lista está vazia.

def cabeca(lista):
    return lista[0]
#Retorna o primeiro elemento da lista.

def cauda(lista):
    return lista[1:]
#Retorna a lista sem seu primeiro elemento.

def insere(lista, x):
    lista.append(x)
    return lista
#Retorna a lista com o elemento x inserido no final

l1 = []
l2 = []                                                                       #Identando as variáveis que devem ser transformar em listas
l3 = []

def concatenacao(l1, l2):

    if(vazio(l1)):                               #Se a lista 1 estiver vazia retona a lista 2
        return l2
    elif(vazio(l2)):                             #Se a lista 2 estiver vazia retorna o conteúdo da lista 1
        return l1
    else:                                        #Caso as duas listas tenham elementos juntamos a lista 1 com a cabeça da lista 2 em seguida juntamos com a cauda da 2.
        insere(l1, cabeca(l2))
        return concatenacao(l1, cauda(l2))

def comprimento(l1):
    if (vazio(l1)):            #Se a lista estiver vazia seu comprimento será 0
        return 0
    else:
        contador = 1           #Aqui insere-se um contador e somado com a cauda, pois a cauda contém todos os elementos da lista faltando 1
    return contador + comprimento(cauda(l1))

def elemento(l1, posicao):
    if posicao == 0:            #Se a posição digitada pelo usuario for 0, é retornado o primeiro elemento da lista ou seja o elemento 0
        return cabeca(l1)
    else:                       #A posição vai ser dada usando a cauda, nela temos o resto da lista sem o primeiro elemento então bastas fazer a posição menos 1 e retornar esse elemento
        return elemento(cauda(l1), posicao - 1)

def pertence(l1, x):
    if vazio(l1):          #Se a lista for vazia nada vai pertercer a ela então é falso
        return False
    if cabeca(l1) == x:    #Se o elemento escrito pelo usuário for igual a cabeça da lista ele pertence a lista logo é verdadeiro
        return True
    else:                  #E se pertencer a cauda é verdade tabém
        return pertence(cauda(l1), x)

def ultimo(l1):
    if vazio(l1):                    #Se a lista estiver a vazia não existe ultimo elemento
        return 'Vazio'
    elif comprimento(l1) == 1:       #Se a lista tiver um único elemento isso quer dizer que ele também é o último
        return cabeca(l1)
    else:                            #Para uma lista maior basta retornar o último elemento da cauda dessa lista.
        return ultimo(cauda(l1))

def primeiros(l1,n):
    if n == 0:               #Aqui usa-se a quantidade de primeiros escolhidos menos um (para obter a posição desejada)
        return []            #e esse número é aplicado a cauda depois a concatenação une a cabeça e cauda e printa o numero de primeiros escolhido
    return concatenacao(primeiros(cauda(l1), n - 1), [cabeca(l1)])

def inverte(l1):
    if comprimento(l1) == 1:     #Se o comprimento da lista for um, o seu inverso vai ser a mesma coisa, logo é retornada a cabeça
        return [cabeca(l1)]
    else:                        #Aqui apenas inverte-se a cauda e concatena ela a cabeça
        return concatenacao(inverte(cauda(l1)), [cabeca(l1)])

print('Digite "sair" caso não queira adicionar mais itens a lista')

while True:                                                                  #Começa o laço principal
    x = input('Digite os elementos da lista 1: ')                            #Insere os elementos da lista
    if x != 'sair':                                                          #Se sair será direcionado para o outro laço.
        l1.append(x)
        l3.append(x)
    else:
        break

while True:                                                                  #Laço da escolha
    menu = int(input('\n1 - Concatenação \n2 - Comprimento \n3 - Elemento \n4 - Pertence \n5 - Último \n6 - Primeiros \n7 - Inverte \n8 - Sair \nEscolha uma função para executar: '))
    arq = open('Recursividade.txt', 'a')                                     #Abrindo o arquivo
    if menu == 1:                                                            #Se escolher a primeira opção será pedido mais uma lista
        print('\nDigite "sair" para não adicionar itens na lista 2')
        while True:
            y = input('Digite os elementos da lista 2: ')
            if y != 'sair':
                l2.append(y)
            else:
                break
        c = (concatenacao(l1, l2))                                            #Aqui é usada a funçao de cocatenar
        print(c)                                                              #Printado o resultado
        arq.write(f'Concatenacao -> {l3, l2}  ->  {c}\n')                     #E escrito no arquivo o que será salvo da operação

    if menu == 2:                                                             #Se a escolha for a segunda opção
        print(f'\n{comprimento(l1)} Elementos')                               #É usada a função comprimento e printado o resultado
        arq.write(f'Comprimento -> {l1}  ->  {comprimento(l1)}\n')            #E escrito no aquivo o que será salvo da operação

    if menu == 3:                                                             #Se a escolha for a terceira opção
        posicao = int(input('Digite a posição do elemento a ser mostrado: ')) #É pedido a posição de um elemento
        print(elemento(l1, posicao))                                          #É usada a função posição e printado o resultado
        arq.write(f'Elemento -> {l1,posicao}  ->  {elemento(l1,posicao)}\n')  #E escrito no arquivo o que será salvo da operação

    if menu == 4:                                                             #Se a escolha for a quarta opção
        x = input('Digite o elemento que deseja verificar: ')                 #Pede-se o elemento para verificação
        print(pertence(l1, x))                                                #É usada a função pertence e printado o resultado
        arq.write(f'Pertence -> {l1,x}  ->  {pertence(l1,x)}\n')              #E escrito no arquivo o que será salvo da operação

    if menu == 5:                                                             #Se a escolha for a quinta opção
        print('\n', ultimo(l1))                                               #É usada a função ultimo e printado o resultado
        arq.write(f'Ultimo -> {l1}  ->  {ultimo(l1)}\n')                      #E escrito no arquivo o que será salvo da operação

    if menu == 6:                                                             #Se a escolha for a sexta opção
        n = int(input('Quantos itens da lista deseja que sejam impressos: ')) #Pede-se a quantidade de itens a serem impressos
        print(inverte(primeiros(l1,n)))                                       #É usada a função primeiros e printado o resultado
        arq.write(f'Primeiros -> {l1,n}  ->  {inverte(primeiros(l1,n))}\n')            #E escrito no arquivo o que será salvo da operação

    if menu == 7:                                                             #Se a escolha for a setima opção
        print(inverte(l1))                                                    #É usada a função inverte e printado o resultado
        arq.write(f'Inverte -> {l1}  ->  {(inverte(l1))}\n')                  #E escrito no arquivo o que será salvo da operação

    if menu == 8:                                                             #Se a escolha for a oitava opção
        break                                                                 #O programa finaliza


