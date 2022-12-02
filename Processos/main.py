import os

print('Sou processo principal (pai). Meu PID é: ', os.getpid())

escolha = input('Escolha 1: ')

if escolha == '1':
    pid = os.fork()
    if pid == 0:
        print('\nSou Gabriel Oliveira Chaves, e meu PID é: ' + str(os.getpid()))
    elif pid > 0:
        print('Sou pai. Meu PID é:' + str(os.getpid()) + 
          ", Gabriel Oliveira Chaves é: " + str(pid))
else:
    exit()