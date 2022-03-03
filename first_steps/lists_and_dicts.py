def run():
    _list = [1, "Hello", True, 4.5]
    _dict = { "firstname": "Pedro", "lastname": "Perez"}

    super_list = [
        { "firstname": "Pedro", "lastname": "Perez"},
        { "firstname": "Bruce", "lastname": "Blanco"},
        { "firstname": "Sofia", "lastname": "Saldoval"},
        { "firstname": "Tom", "lastname": "Torres"},
        { "firstname": "Ricardo", "lastname": "Rojas"},
    ]

    super_dict = {
        "natural_nums":[1, 2, 3, 4, 5],
        "integer_nums":[-2, -1, 0, 1, 2],
        "floating_nums":[1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for  value in super_list:
        print(value)

if __name__ == '__main__':
    run()