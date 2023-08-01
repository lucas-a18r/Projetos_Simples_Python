print('Bem ao Vindo ao Quiz!')
print('Boa Sorte')
print('Observação: Digite a opção correta')

print('\nDica: 5 / 8 / 10')
print('Quantas copas o brasil ganhou ? ' )
pergunta1 = input('Resposta: ')

print('\nDica: Marte / Jupiter / Plutao')
print('Qual o planeta considerado extinto: ')
pergunta2 = input('Resposta: ')

print('\nDica: Indigo / Pacifico / Atlantico')
print('O maior oceano do mundo: ')
pergunta3 = input('Resposta: ')

print('\nDica: 105 / 88 / 206')
print('Quantos ossos tem o corpo humano: ')
pergunta4 = input('Resposta: ')

print('\nDica: Quiz / Nada demais / Tudo')
print('o que acabou de fazer: ')
pergunta5 = input('Resposta: ')

pontos = 0
if pergunta1 == '5':
    print('\n1º - ACERTOU!')
    pontos = pontos + 200
else :
    print('\n1º - Infelimente Errou...')

if pergunta2 == 'Plutao':
    print('\n2º - ACERTOU!')
    pontos = pontos + 200
else :
    print('\n2º - Infelimente Errou...')

if pergunta3 == 'Pacifico':
    print('\n3º - ACERTOU!')
    pontos = pontos + 200
else :
    print('\n3º - Infelimente Errou...')

if pergunta4 == '206':
    print('\n4º - ACERTOU!')
    pontos = pontos + 200
else :
    print('\n4º - Infelimente Errou...')

if pergunta5 == 'Quiz':
    print('\n5º - ACERTOU!')
    pontos = pontos + 200
else :
    print('\n5º - Infelimente Errou...')

print('\nPontos Totais: ', pontos)