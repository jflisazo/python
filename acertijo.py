import random

acertijo = random.randrange(0,100,1)
numero = -1

while acertijo != numero:
    print("Dame un numero entre 0 y 100: ")
    numero = int(input())

    if numero < acertijo:
        print("Muy chico!!!")
    elif numero > acertijo:
        print("Muy grande!!!")
    else:
        print("Acertaste, eres un genio!!!")

