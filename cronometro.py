import time 

ct = input("\nTempo em segundos: ") 

def contagem_Reg(ct): 
    while ct: 
        minutos, segundos = divmod(ct, 60)
        temporizador = '{:02d}:{:02d}'.format(minutos, segundos) 
        print(temporizador, end="\r") 
        time.sleep(1) 
        ct = ct - 1
    print('\nFim de Jogo!')

contagem_Reg(int(ct))