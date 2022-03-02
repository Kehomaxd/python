import random

def generatePassword():
    mayus = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    min = ['w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symb =['$', '/', '-', '*', '#', 'ª', '·', '#', '€', '%', '&'] 

    characters = mayus + min + symb + num

    password = []

    for i in range(24):
        characterRandom = random.choice(characters)
        password.append(characterRandom)
    password = ''.join(password)
    return password

def run():
    password = generatePassword()

    print('Contraseña generada con exito \n'+ password )
if __name__ == '__main__':

    run()