import random

def run(): 
    num = random.randint(1, 100)

    guess = int(input('elige un número del 1 al 100: '))

    while guess != num:
        if guess < num :
            print('No no, mas grande')
        else:
            print('No no es menos')
        guess = int(input('Elige otro numero: '))
    print ('ganaste')

if __name__ == '__main__': 
       run()
