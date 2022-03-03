def run():

    # squares = []
    # for i in range(1, 101):
    #     e = i ** 2
    #     if e % 3 != 0:
    #         squares.append(e)
    # print(squares)

    squares = [i**2 for i in range(1, 101) if i % 3 !=0]

    # con diccionario comprehensions
    # {key: value for value in iterable if condition}
    # {i: 1**3 for i in range(1,101) if i % 3 != 0}

if __name__ ==  '__main__':
    run()