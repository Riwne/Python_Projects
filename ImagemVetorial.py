# Riane Carla Gomes Alves
# Matrícula: 508771
# Turma 1
import turtle

def retangulo():

    # Colher os dados (fomato da caneta, coordenadas x e y, a orientação e cor) e os dados especificos da forma.
    fc = janela.numinput('Seu Desenho','Escolha a forma da sua caneta:\n 1 - Círculo.\n 2 - Triângulo.\n 3 - Seta.\n 4 - Tartaruga.\n 5 - Invisível.\nOBS: Escolha um número de 1 a 5. ')
    if fc == 1:
        fc = "circle"
    if fc == 2:
        fc = "triangle"
    if fc == 3:
        fc = "classic"
    if fc == 4:
        fc = "turtle"
    if fc == 5:
        fc = "blank"
    x = janela.numinput('Seu Desenho',' Escolha a coordenada x da posição onde seu desenho irá iniciar.')
    y = janela.numinput('Seu Desenho',' Escolha a coordenada y da posição onde seu desenho irá iniciar.')
    orientaçao = janela.numinput('Seu Desenho','Escolha a orientação da caneta.\nObs: Os números indicarão os graus.')
    cor = janela.numinput('Seu Desenho','Escolha uma cor para sua forma:\n 1 - Azul.\n 2 - Amarelo.\n 3 - Verde.\n 4 - Vermelho.\n 5 - Roxo.\n 6 - Marrom.\n 7 - Cinza.\n 8 - Preto.\nOBS: Esccolha um número de 1 a 8.')
    if cor == 1:
        cor = 'blue'
    if cor == 2:
        cor = 'yellow'
    if cor == 3:
        cor = 'green'
    if cor == 4:
        cor = 'red'
    if cor == 5:
        cor = 'purple'
    if cor == 6:
        cor = 'brown'
    if cor == 7:
        cor = 'gray'
    if cor == 8:
        cor = 'black'

    largura = janela.numinput('Seu Desenho','Escolha a largura do seu retângulo.')
    altura = janela.numinput('Seu Desenho','Escolha a altura do seu retângulo.')

    # Agora é só usar todas as informações que o usuário inseriu para fazer o desenho.
    caneta = turtle.Turtle()
    caneta.up()
    caneta.shape(fc)                                            # Formato da caneta escolhido pelo usuário
    caneta.goto(x, y)                                           # Vai até as coordenadas
    caneta.setheading(orientaçao)                               # Coloca na orientação(ângulo) desejado
    caneta.down()                                               # Começa a desenhar
    caneta.fillcolor(cor)                                       # Coloca a cor escolhida
    caneta.begin_fill()                                         # Começa o preenchimento
    caneta.forward(largura)
    caneta.left(90)
    caneta.forward(altura)
    caneta.left(90)
    caneta.forward(largura)
    caneta.left(90)
    caneta.forward(altura)
    caneta.end_fill()                                           # Termina o preenchimento

    # Nessa etapa eu retorno todos os dados usados para fazer o desenho para que no final imprima todas essas informações.
    return 'retangulo', fc, x, y, orientaçao, cor, largura, altura

def circulo():

    fc = janela.numinput('Seu Desenho','Escolha a forma da sua caneta:\n 1 - Círculo.\n 2 - Triângulo.\n 3 - Seta.\n 4 - Tartaruga.\n 5 - Invisível.\nOBS: Escolha um número de 1 a 5. ')
    if fc == 1:
        fc = "circle"
    if fc == 2:
        fc = "triangle"
    if fc == 3:
        fc = "classic"
    if fc == 4:
        fc = "turtle"
    if fc == 5:
        fc = "blank"

    x = janela.numinput('Seu Desenho', ' Escolha a coordenada x da posição onde seu desenho irá iniciar.')
    y = janela.numinput('Seu Desenho', ' Escolha a coordenada y da posição onde seu desenho irá iniciar.')
    orientaçao = janela.numinput('Seu Desenho','Escolha a orientação da caneta.\nObs: Os números indicarão os graus.')
    cor = janela.numinput('Seu Desenho','Escolha uma cor para sua forma:\n 1 - Azul.\n 2 - Amarelo.\n 3 - Verde.\n 4 - Vermelho.\n 5 - Roxo.\n 6 - Marrom.\n 7 - Cinza.\n 8 - Preto.\nOBS: Escolha um número de 1 a 8.')
    if cor == 1:
        cor = 'blue'
    if cor == 2:
        cor = 'yellow'
    if cor == 3:
        cor = 'green'
    if cor == 4:
        cor = 'red'
    if cor == 5:
        cor = 'purple'
    if cor == 6:
        cor = 'brown'
    if cor == 7:
        cor = 'gray'
    if cor == 8:
        cor = 'black'

    raio = janela.numinput('Seu Desenho', 'Escolha o raio do seu circulo.')

    caneta = turtle.Turtle()
    caneta.up()
    caneta.shape(fc)
    caneta.goto(x, y)
    caneta.setheading(orientaçao)
    caneta.down()
    caneta.fillcolor(cor)
    caneta.begin_fill()
    caneta.circle(raio)
    caneta.end_fill()

    return 'circulo', fc, x, y, orientaçao, cor, raio

def trianguloRet():

    fc = janela.numinput('Seu Desenho','Escolha a forma da sua caneta:\n 1 - Círculo.\n 2 - Triângulo.\n 3 - Seta.\n 4 - Tartaruga.\n 5 - Invisível.\nOBS: Escolha um número de 1 a 5. ')
    if fc == 1:
        fc = "circle"
    if fc == 2:
        fc = "triangle"
    if fc == 3:
        fc = "classic"
    if fc == 4:
        fc = "turtle"
    if fc == 5:
        fc = "blank"
    x = janela.numinput('Seu Desenho', ' Escolha a coordenada x da posição onde seu desenho irá iniciar.')
    y = janela.numinput('Seu Desenho', ' Escolha a coordenada y da posição onde seu desenho irá iniciar.')
    orientaçao = janela.numinput('Seu Desenho','Escolha a orientação da caneta.\nObs: Os números indicarão os graus.')
    cor = janela.numinput('Seu Desenho','Escolha uma cor para sua forma:\n 1 - Azul.\n 2 - Amarelo.\n 3 - Verde.\n 4 - Vermelho.\n 5 - Roxo.\n 6 - Marrom.\n 7 - Cinza.\n 8 - Preto.\nOBS: Escolha um número de 1 a 8.')
    if cor == 1:
        cor = 'blue'
    if cor == 2:
        cor = 'yellow'
    if cor == 3:
        cor = 'green'
    if cor == 4:
        cor = 'red'
    if cor == 5:
        cor = 'purple'
    if cor == 6:
        cor = 'brown'
    if cor == 7:
        cor = 'gray'
    if cor == 8:
        cor = 'black'

    cateto1 = janela.numinput('Seu Desenho','Escolha o tamanho do primeiro cateto do seu triângulo.')
    cateto2 = janela.numinput('Seu Desenho','Escolha o tamanho do segundo cateto do seu triângulo')

    # Importando a biblioteca para fazer o calculo da hipotenusa
    import math
    hipotenusa = (int(cateto1 ** 2)) + (int(cateto2 ** 2))
    raiz = math.sqrt(hipotenusa)

    caneta = turtle.Turtle()
    caneta.up()
    caneta.shape(fc)
    caneta.goto(x, y)
    caneta.setheading(orientaçao)
    caneta.down()
    caneta.fillcolor(cor)
    caneta.begin_fill()
    caneta.right(90)
    caneta.forward(cateto1)
    caneta.left(90)
    caneta.forward(cateto2)
    caneta.end_fill()

    return 'triangulo', fc, x, y, orientaçao, cor, cateto1, cateto2

def poligonoReg():

    fc = janela.numinput('Seu Desenho',
                         'Escolha a forma da sua caneta:\n 1 - Círculo.\n 2 - Triângulo.\n 3 - Seta.\n 4 - Tartaruga.\n 5 - Invisível.\nOBS: Escolha um número de 1 a 5. ')
    if fc == 1:
        fc = "circle"
    if fc == 2:
        fc = "triangle"
    if fc == 3:
        fc = "classic"
    if fc == 4:
        fc = "turtle"
    if fc == 5:
        fc = "blank"
    x = janela.numinput('Seu Desenho', ' Escolha a coordenada x da posição onde seu desenho irá iniciar.')
    y = janela.numinput('Seu Desenho', ' Escolha a coordenada y da posição onde seu desenho irá iniciar.')
    orientaçao = janela.numinput('Seu Desenho', 'Escolha a orientação da caneta.\nObs: Os números indicarão os graus.')
    cor = janela.numinput('Seu Desenho',
                          'Escolha uma cor para sua forma:\n 1 - Azul.\n 2 - Amarelo.\n 3 - Verde.\n 4 - Vermelho.\n 5 - Roxo.\n 6 - Marrom.\n 7 - Cinza.\n 8 - Preto.\nOBS: Escolha um número de 1 a 8.')
    if cor == 1:
        cor = 'blue'
    if cor == 2:
        cor = 'yellow'
    if cor == 3:
        cor = 'green'
    if cor == 4:
        cor = 'red'
    if cor == 5:
        cor = 'purple'
    if cor == 6:
        cor = 'brown'
    if cor == 7:
        cor = 'gray'
    if cor == 8:
        cor = 'black'

    nlados = janela.numinput('Seu Desenho', 'Escolha a quantidade de lados do seu poligono.')
    tlados = janela.numinput('Seu Desenho', 'Escolha o tamanho dos lados do seu poligono.')

    caneta = turtle.Turtle()
    caneta.up()
    caneta.shape(fc)
    caneta.goto(x, y)
    caneta.setheading(orientaçao)
    caneta.down()
    caneta.fillcolor(cor)
    caneta.begin_fill()
    # Fazendo o poligono com entradas do usuário
    for i in range(int(nlados)):
        caneta.forward(tlados)
        caneta.right(360/nlados)
    caneta.end_fill()

    return 'poligono', fc, x, y, orientaçao, cor, nlados, tlados

dados = []                                            # Nessa parte a defino que dados é uma lista

laço = True                                           # Laço principal, primeira coisa que vai ser executada.
while laço:
    janela = turtle.Screen()                          # Primeiro abrimos a janela do desenho.
    janela.setup(600,600)
                                                      # Escolher entre fazer uma forma ou sair, só pra ficar bonitinho mesmo.
    inicio = janela.numinput('BEM VINDO A DESENHANDO COM TURTLE','\n1 - Escolher uma Forma para desenhar     2- Sair\nEscolha uma das opções: ')
                                                      # Se escolheu fazer uma forma:
    if inicio == 1:
        escolhaForma = True
        while escolhaForma:                           # Escolha da forma.
            forma=janela.numinput('Seu Desenho','\nAgora escolha a forma que ira desenhar.\n1 - Retângulo   2 - Circulo   3 - Triângulo Retângulo   4 - Poligono Regular\nNúmero da sua forma: ')
            if forma == 1:
                dados.append(retangulo())             # Aqui a variável dados(que é uma lista) vai receber tudo que eu retornei,
            if forma == 2:                            # ou seja todas as informações para reproduzir aquelas formas.
                dados.append(circulo())
            if forma == 3:
                dados.append(trianguloRet())
            if forma == 4:
                dados.append(poligonoReg())
            else:
                break                                 # Se não escolher nenhuma forma volta.
                                                      # Se escolheu sair:
    elif inicio == 2:
        break
print(dados)                                          # E no fim a variável dados vai ser printada, ou seja,
                                                      # vamos printar uma lista com todas as informações para reproduzir o mesmo desenho.