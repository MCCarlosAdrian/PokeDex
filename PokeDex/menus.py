#Modulo para los Menus y verificadores.
def menuprincipal(a):
    print(a)
    print("Ingresa una opcion")#primera peticion
    try:
        x = int(input())
    except ValueError:#en caso de error volvemos a pedir
        print("Opcion no valida!!!")
        x = menuprincipal(a)
    else:
        if x > 5 or x < 1:#en caso de rango equivocado repetimos
             print("Opcion no valida!!!")
             x = menuprincipal(a)
    return x
  
def menupokemon(a):
    print(a)
    print("Ingresa una opcion")
    try:
        x = int(input())
    except ValueError:
        print("Opcion no valida!!!")
        x = menupokemon(a)
    else:
        if x > 3 or x < 1:
            print("Opcion no valida!!!")
            x = menupokemon(a)
    return x
  
def menupoke2(a):
    print(a)
    print("Ingresa una opcion")
    try:
        x = int(input())
    except ValueError:
        print("Opcion no valida!!!")
        x = menupokemon(a)
    else:
        if x > 2 or x < 1:
            print("Opcion no valida!!!")
            x = menupokemon(a)
    return x

def verif_id():
    try:
        print("Ingresa el pokeID (del 1 al 151)")
        x = int(input())
    except ValueError:
        print("Opcion no valida!!!")
        x = verif_id()
    else:
        if x > 151 or x < 1:
            print("Opcion no valida!!!")
            x = verif_id()
    return str(x)

def verif_met(num):
    try:
        print("Ingresa el ID (del 1 al "+str(num)+")")
        x = int(input())
    except ValueError:
        print("Opcion no valida!!!")
        x = verif_met(num)
    else:
        if x > int(num) or x < 1:
            print("Opcion no valida!!!")
            x = verif_met(num)
    return str(x)

def verif_his(a):
    try:
        print(a)
        x = int(input())
    except ValueError:
        print("Opcion no valida!!!")
        x = verif_his(a)
    else:
        if x > 2 or x < 1:
            print("Opcion no valida!!!")
            x = verif_his(a)
    return x