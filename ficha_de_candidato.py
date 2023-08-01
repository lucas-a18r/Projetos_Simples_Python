print('Ficha de Candidato')
print('\nPrencheer seus dados cadastrais')

nome = str(input('Nome Completo: '))
idade = int(input('Idade: '))
profiss = str(input('Profissão Anterior: '))


print('\n--- Ficha --- \
    \nNome: '+ nome +' \
    \nIdade: ', idade ,' \
    \nCargo Anterior: '+ profiss +'')
 
if idade >= 18:
    print('\nApto para o novo cargo')
else:
    print('\nSem idade suficiente para entrar no cargo')