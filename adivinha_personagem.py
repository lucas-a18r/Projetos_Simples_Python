print('Adivinha personagem da cultura POP!')
print('Obs: 1º Letra maiscuscula e palavra sem acento')
personagens = ['Ash', 'Bart', 'Barbie', 'Chapolin', 'Chris', 'Donkey Kong', 'Eleanor', 'Ferb', 'Goku', 'Hilbert', 'Ino', 'Jackie Chan'\
'K', 'Lala', 'Munra', 'Naruto','Omar', 'Paul', 'Quentin', 'R', 'Seya', 'T', 'U', 'Velmont', 'Wolverine', 'Xavier', 'Yno', 'Zabusa']  
 
personagem = str(input('Qual Personagem: '))

if personagem in personagens: # maneira simples de fazer
    print('\nACERTOU!')
else:
    print('\nErrouuuuu...')
