def decorators(parametro):

    def interno():
        print("interno antes del parametro y el inicio")
        parametro()
        print("interno despues del parametrp y el final")

    return interno

@decorators
def suma():
    print(15+30)

@decorators
def resta():
    print(30-10)

suma()
resta()