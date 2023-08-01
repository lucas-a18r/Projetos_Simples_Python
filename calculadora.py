operador = (input('\
\n soma digite +\n \
subtrair digite -\n \
multiplicar digite *\n \
dividir digite /\n \
qual deseja fazer: '))

num1 = float(input('Digite número 1: '))
num2 = float(input('Digite número 2: '))

def resulta(): # usando função para os cálculos
    resultado = 0
    if operador == '+' :
        resultado = num1 + num2
        print('valor: ', resultado)
    elif operador == '-' :
        resultado = num1 - num2
        print('valor: ', resultado)
    elif operador == '*' :
        resultado = num1 * num2
        print('valor: ', resultado)
    elif operador == '/' :
        resultado = num1 / num2
        print('valor: ',resultado)
    else:
        print('Digite o operador corretamente!')
    
resulta()