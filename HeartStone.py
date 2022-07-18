# Riane Carla Gomes Alves
# Matrícula: 508771
# Turma 01
print('\n')

print('*'*30)
print('Bem vindo a Arena HearthStone')
print('*'*30,'\n')

print('Entre com os dados da batalha.')

print('--- Primeira Equipe ---')
while True:                                                                 # Mensagem de erro caso coloque um número no nome do heroi.
    heroi_1 = input('Heroi - Nome: ')                                       # Coletando o nome do heroi.
    if(heroi_1.isnumeric()):
        print('Coloque apenas nomes.')
    else:
        break

while True:                                                                 # Mensagem caso a vida do heroi não esteja nas condiões.
    vidaH1 = int(input(f'Heroi {heroi_1} - Pontos de vida: '))              # Coletando pontos de vida.
    if(vidaH1 < 0 or vidaH1 > 30):
        print('Insira um valor para Pontos de Vida válido. Maior que 0 e menor que 30.')
    else:
        break

while True:                                                                 # Mensagem de erro caso coloque um número no nome do lacaio.
    lacaio1H1 = input(f'Primeiro lacaio de {heroi_1} - Nome: ')             # Coletando nome do lacaio.
    if(lacaio1H1.isnumeric()):
        print('Coloque apenas nomes.')
    else:
        break

while True:                                                                 # Mensagem caso os pontos de vida não estejam nas condições.
    vidaL1H1 = int(input(f'Lacaio {lacaio1H1} - Pontos de vida: '))         # Coletando os pontos de vida.
    if(vidaL1H1 < 0 or vidaL1H1 >10):
        print('Insira um valor para Pontos de Vida válido. Maior que 0 menor que 10.')
    else:
        break
while True:                                                                 # Mensagem caso os pontos de ataque não estejam nas condições.
    ataqueL1H1 = int(input(f'Lacaio {lacaio1H1} - Pontos de ataque: '))     # Coletando pontos de ataque.
    if(ataqueL1H1 < 0 or ataqueL1H1 > 10):
        print('Insira um valor para Pontos de ataque válido. Maior que 0 e menor que 10.')
    else:
        break

while True:                                                                 # Mensagem de erro caso coloque um número no nome do lacaio.
    lacaio2H1 = input(f'Segundo lacaio de {heroi_1} - Nome: ')              # Coletando nome do lacaio.
    if(lacaio2H1.isnumeric()):
        print('Coloque apenas nomes.')
    else:
        break

while True:                                                                # Mensagem caso os pontos de vida não estejam nas condições.
    vidaL2H1 = int(input(f'Lacaio {lacaio2H1} - Pontos de Vida: '))        # Coletando pontos de vida.
    if(vidaL2H1 < 0 or vidaL2H1 > 10):
        print('Insira um valor para Pontos de Vida válido. Maior que 0 e menor que 10.')
    else:
        break
while True:                                                                 # Mensagem caso os pontos de ataque não estejam nas condições.
    ataqueL2H1 = int(input(f'Lacaio {lacaio2H1} - Pontos de Ataque: '))     # Coletando pontos de ataque.
    if(ataqueL2H1 < 0 or ataqueL2H1 > 10):
        print('Insira um valor para Pontos de Ataque válido. Maior que 0 e menor que 10.')
    else:
        break
print('\n')

print('--- Segunda Equipe ---')
while True:                                                                 # Mensagem de erro caso coloque um número no nome do heroi.
    heroi_2 = input('Heroi - Nome: ')                                       # Coletando o nome do  heroi.
    if(heroi_2.isnumeric()):
        print('Coloque apenas nomes.')
    else:
        break

while True:                                                                # Mensagem caso a vida do heroi não esteja nas condições.
    vidaH2 = int(input(f'Heroi {heroi_2} - Pontos de Vida: '))             # Coletando vida do heroi.
    if(vidaH2 < 0 or vidaH2 > 30):
        print('Insira um valor para Pontos de Vida válido. Maior que 0 e menor que 30.')
    else:
        break

while True:                                                                # Mensagem de erro caso coloque um número no nome do lacaio.
    lacaio1H2 = input(f'Primeiro lacaio de {heroi_2} - Nome: ')            # Coletando nome do lacaio.
    if(lacaio1H1.isnumeric()):
        print('Coloque apenas nomes.')
    else:
        break

while True:                                                                # Mensagem caso pontos de vida não esteja nas condições.
    vidaL1H2 = int(input(f'Lacaio {lacaio1H2} - Pontos de Vida: '))        # Coletando pontos de vida.
    if(vidaL1H2 < 0 or vidaL1H2 > 10):
        print('Insira um valor para Pontos de Vida válido. Maior que 0 e menor que 10.')
    else:
        break
while True:                                                                 # Mensagem caso pontos de ataque não estejam nas condições.
    ataqueL1H2 = int(input(f'Lacaio {lacaio1H2} - Pontos de Ataque: '))     # Coletando pontos de ataque.
    if(ataqueL1H2 < 0 or ataqueL1H2 > 10):
        print('Insira um valor para Pontos de Ataque válido. Maior que 0 e menor que 10.')
    else:
        break

while True:                                                                 # Mensagem de erro caso coloque um número no nome do lacaio.
    lacaio2H2 = input(f'Segundo lacaio de {heroi_2} - Nome: ')              # Coletando nome do lacaio.
    if(lacaio2H2.isnumeric()):
        print('Coloque apenas nomes.')
    else:
        break

while True:                                                                # Mensagem caso pontos de vida não entejam nas condições.
    vidaL2H2 = int(input(f'Lacaio {lacaio2H2} - Pontos de Vida: '))        # Coletando pontos de vida.
    if(vidaL1H2 < 0 or vidaL2H2 > 10):
        print('Insira um valor para os Pontos de Vida válido. Maior que 0 e menor que 10.')
    else:
        break
while True:                                                                # Mensagem caso pontos de ataque não estejam nas condições.
    ataqueL2H2 = int(input(f'Lacaio {lacaio2H2} - Pontos de Ataque: '))    # Coletando pontos de ataque.
    if(ataqueL2H2 < 0 or ataqueL2H2 > 10):
        print('Insira um valor para Pontos de Ataque válido. Maior que 0 e menor que 10.')
    else:
        break
print('\n')

print('*'*20)
print('Começando a Batalha')
print('*'*20,'\n')

print(f'Ataque de {heroi_1}')
while True:                                                                # Mensagem de erro caso não escolha um lacaio da sua equipe.
    escolhaAtq = input('Escolha um lacaio para atacar: ')                  # Colhendo nome do atacante.
    if(escolhaAtq == lacaio1H2 or escolhaAtq == lacaio2H2):
        print('Escolha um de seus lacaios.')
    else:
        break

while True:                                                               # Mensagem de erro caso não escolha um cacaio de sua equipe pra defender.
    escolhaDef = input('Escolha seu alvo: ')                              # Colhendo nome do lacaio ou heroi que vai defender.
    if(escolhaDef == lacaio1H1 or escolhaDef == lacaio2H1 or escolhaDef == heroi_1):
        print('Escolha um lacaio ou o heroi da equipe inimiga.')
    else:
        break

print('\n')
# Nessa etapa vamos identar a vida e ataque dos combatentes de acordo com os dados colhidos anteriormente.
if(lacaio1H1 == escolhaAtq):
    Ataque1 = ataqueL1H1
    Vida1 = vidaL1H1

if(lacaio2H1 == escolhaAtq):
    Ataque1 = ataqueL2H1
    Vida1 = vidaL2H1

if(heroi_2 == escolhaDef):
    Ataque2 = 0
    Vida2 = vidaH2

if(lacaio1H2 == escolhaDef):
    Ataque2 = ataqueL1H2
    Vida2 = vidaL1H2

if(lacaio2H2 == escolhaDef):
    Ataque2 = ataqueL2H2
    Vida2 = vidaL2H2

vidaRD = Vida2 - Ataque1                                                      # Vida restante de quem defendeu
vidaRA = Vida1 - Ataque2                                                      # Vida restante de quem atacou

print('**** Ataque Feito **** ')
                                                                             # Se não houver vida (<0) os jogadores morreram
if(vidaRD <= 0):
    print(f'{escolhaDef} Morreu!')
if(vidaRA <= 0):
    print(f'{escolhaAtq} Morreu!')
if(vidaRD > 0 and vidaRA > 0):
    print('Ninguém morreu.')
print('\n')

print('**** Status do Tabuleiro ****')

print(f'Heroi {heroi_1} (Vida: {vidaH1})')                                    # Nessa parte temos que mostrar o status do jogo

if(vidaRA <= 0 and lacaio1H1 == escolhaAtq):                                  # Se a vida for <=0 ele esta morto, então não precisa aparecer
    pass                                                                      # no status do jogo, então passa
else:                                                                         # Se não, ele foi a escolha de ataque e devemos mostrar seu ataque
    if(escolhaAtq == lacaio1H1):                                              # da nova identação, também podia ser do primeiro valor de ataque.
        print(f'Lacaio {lacaio1H1} (Ataque: {Ataque1} / Vida: {vidaRA})')     # e o resto da sua vida.
    else:                                                                     # Se ele não morreu nem foi escolha de ataque
        print(f'Lacaio {lacaio1H1} (Ataque: {ataqueL1H1} / Vida: {vidaL1H1})')# ele continua com os mesmos pontos de ataque.

if(vidaRA <= 0 and lacaio2H1 == escolhaAtq):
    pass
else:
    if(escolhaAtq == lacaio2H1):
        print(f'Lacaio {lacaio2H1} (Ataque: {Ataque1} / Vida: {vidaRA})')
    else:
        print(f'Lacaio {lacaio2H1} (Ataque: {ataqueL2H1} / Vida: {vidaL2H1})')

print('\n')

if(vidaRD <= 0 and heroi_2 == escolhaDef):                                      # Se a vida for <=0 ele está morto então não precisa aparecer.
    pass
else:                                                                           # Se não ele foi a escolha de defesa, então devemos mostrar a vida
    if(escolhaDef == heroi_2):                                                  # restante.
        print(f'Heroi {heroi_2} (Vida: {vidaRD})')
    else:                                                                       # E se ele não morreu e não foi a escolha de defesa devemos mostrar
        print(f'Heroi {heroi_2} (Vida: {vidaH1})')                              # os pontos de vida e ataque iniciais.

if(vidaRD <= 0 and lacaio1H2 == escolhaDef):
    pass
else:
    if(escolhaDef == lacaio1H2):
        print(f'Lacaio {lacaio1H2} (Ataque: {Ataque2} / Vida: {vidaRD})')
    else:
        print(f'Lacaio {lacaio1H2} (Ataque: {ataqueL1H2} / Vida: {vidaL1H2})')

if(vidaRD <= 0 and lacaio2H2 == escolhaDef):
    pass
else:
    if(escolhaDef == lacaio2H2):
        print(f'Lacaio {lacaio2H2} (Ataque: {Ataque2} / Vida: {vidaRD}')
    else:
        print(f'Lacaio {lacaio2H2} (Ataque: {ataqueL2H2} / Vida: {vidaL2H2}')
