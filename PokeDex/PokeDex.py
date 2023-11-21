try:
    import requests, json, menus, guardadoh, graficos, calculos, excelmodulo
except ModuleNotFoundError as e1:
    print(f'Error: No se pudo importar un módulo necesario. Detalles: {e1}')
    print("Instale los modulos necesarios para el funcionamiento del",
          "programa.")
    exit()
sumapeso = [0, 0]
sumaaltura = [0, 0]
cont = 1
excelmodulo.crearexcel()
if __name__ == "__main__":
    menu = '''Bienvenido, Elige la opción que más te interese:
    1. Pokemon (informacion general, gráficas y promedios)
    2. Habitats (pokemon que habitan esos habitats)
    3. Metodos de Encuentro (informacion general)
    4. Guardado Historico
    5. Salir \n'''
    historico = "Deseas guardar el historial? \n1. Si \n2. No\n"
    consultarhis = "¿Deseas consultar el apartado historico? \n1.Si \n2.No\n"
    while True:
        opc = menus.menuprincipal(menu)#Mostramos el menu
        if opc == 1:#mostramos el menu 1.1
            pokemenu = '''Elige que deseas conocer:
            1. Información general.
            2. Gráficas (altura, peso y tipos)
            3. Calculos (Promedio de altura y peso, moda de tipos) \n'''
            opcpoke = menus.menupokemon(pokemenu)
            if opcpoke == 1:#Info gral
                i = menus.verif_id()
                url = "https://pokeapi.co/api/v2/pokemon/" + str(i) + "/"
                response = requests.get(url)#200
                if response.status_code != 200:#Si consultaremos alguna
                  #que no existe, es mejor terminar
                    print("no se encontró conexión, vuelve a intentar \n")
                    exit()
                pokedex = json.loads(response.text)
                nombrep = pokedex["name"]#guardado en variables de info
                altura = pokedex.get("height") / 10
                peso = pokedex.get("weight") / 10
                tipos = pokedex.get("types")
                print("Pokemon seleccionado:", nombrep, "\n"
                      "La altura en metros es:", altura, "mts",
                      "\n" "El peso en kg es:", peso, "kg")#imprimimos
                print("El tipo o tipos del pokemon son:")
                #impresión de tipos
                nombre_tipos = []
                for elem in tipos:
                    tipo1_y_2 = elem["type"]["name"]
                    nombre_tipos.append(tipo1_y_2)
                    print("-", tipo1_y_2)
                print("\n")
                #guardado historico
                opc_guardadoinfo = menus.verif_his(historico)
                if opc_guardadoinfo == 1:
                    guarpoke = guardadoh.Esc_archi_info(nombrep, altura,
                                                        peso, nombre_tipos,
                                                        cont)
                    cont += 1#aumentamos el contador de consultas
                    if len(tipos) == 2:
                        valores = [nombrep, nombre_tipos[0], nombre_tipos[1], altura, peso]
                    else:
                        valores = [nombrep, nombre_tipos[0], None, altura, peso]
                    excelmodulo.agregarvalores(valores)
                else:
                    print("\n")
                    continue
            elif opcpoke == 2: #Graficas
                mg = ("Graficar: \n 1. Peso (barras) \n 2. Altura (barras) \n 3. Tipos (pay)")
                opcpoke2 = menus.menupokemon(mg)
                barranombres = []
                barravalores = []
                nombretipos = []
                if opcpoke2 == 1:
                    graficos.grafica("weight", barranombres, barravalores)
                elif opcpoke2 == 2:
                    graficos.grafica("height", barranombres, barravalores)
                elif opcpoke2 == 3:
                    graficos.graficapay()
            elif opcpoke == 3:# promedios de altura y peso, moda de tipo
                mg = '''Conseguir:
1. Promedio de peso
2. Promedio de altura
3. Moda de tipos'''
                opcpoke3 = menus.menupokemon(mg)
                if opcpoke3 == 1:
                    peso = calculos.promedio("weight")
                    print("El peso promedio es:",peso,"\n")
                    opc_guardadopp = menus.verif_his(historico)
                    if opc_guardadopp == 1:
                        guarpromp = guardadoh.Esc_archi_promp(peso, cont)#GH
                        cont += 1#aumentamos el contador de consultas
                        excelmodulo.agregarcalculos(7, peso)
                    else:
                        print("\n")
                        continue
                elif opcpoke3 == 2:
                    altura = calculos.promedio("height")
                    print("La altura promedio es:",altura,"\n")
                    opc_guardadopa = menus.verif_his(historico)
                    if opc_guardadopa == 1:
                        guarproma = guardadoh.Esc_archi_proma(altura, cont)#GH
                        cont += 1#aumentamos el contador de consultas
                        excelmodulo.agregarcalculos(9, altura)
                    else:
                        print("\n")
                        continue
                elif opcpoke3 == 3:
                    typemoda = calculos.moda()
                    print("La moda es:",typemoda,"\n")
                    opc_guardadomod = menus.verif_his(historico)
                    if opc_guardadomod == 1:
                        guarmoda = guardadoh.Esc_archi_moda(typemoda, cont)#GH
                        cont += 1#aumentamos el contador de consultas
                        excelmodulo.agregarcalculos(11, typemoda)
                    else:
                        print("\n")
                        continue
        elif opc == 2:
            habdisp = ["cave", "forest", "grassland", "mountain",
                       "rare", "rough-terrain",
                       "sea", "urban", "waters-edge"]
            i = 1
            for elem in habdisp:
                print(i, "-", elem) #mostramos los habitats disponibles
                i += 1
            i = menus.verif_met(9) #inicia la consulta
            url = "https://pokeapi.co/api/v2/pokemon-habitat/" + i + '/'
            response = requests.get(url)#realizamos la solicitud
            if response.status_code != 200:#Si consultaramos alguna que no
                #existe, es mejor terminar
                print("no se encontró conexión, vuelve a intentar")
                exit()
            infohabitat = json.loads(response.text)#guardamos la info
            listahab = []
            habname = infohabitat["name"]#mostramos name de habitat
            print("el nombre del Habitat es:", habname)
            for x in infohabitat:#guardamos los pokemon en una lista
                if "pokemon_species" in x:
                    print("pokemon en el habitat:")
                    for elem in infohabitat["pokemon_species"]:
                        listahab.append(elem["name"])
            print(listahab)
            opc_guardadohab = menus.verif_his(historico)
            if opc_guardadohab == 1:
                guarhab = guardadoh.Esc_archi_hab(habname, listahab, cont)#GH
                cont += 1#aumentamos el contador de consultas
            else:
                print("\n")
                continue
            print("\n")
        elif opc == 3:#Metodos de Encuentro
            metdisp = ["walk", "old-rod", "good-rod", "super-rod", "surf",
                       "rock-smash", "headbutt", "dark-grass", "grass-spots",
                       "cave-spots", "bridge-spots", "super-rod-spots",
                       "surf-spots", "yellow-flowers", "purple-flowers",
                       "red-flowers", "rough-terrain", "gift", "gift-egg",
                       "only-one"]
            i = 1
            for elem in metdisp:
                print(i, "-", elem)#mostramos los metodos disponibles
                i += 1
            i = menus.verif_met(20)
            url = "https://pokeapi.co/api/v2/encounter-method/" + i + '/'
            response = requests.get(url)#solicitud
            if response.status_code != 200:# Si consultaramos alguna que
                #no existe, es mejor terminar
                print("no se encontró conexión, vuelve a intentar")
                exit()
            infometenc = json.loads(response.text)#guardamos datos
            metname = infometenc["name"]
            print("el metodo de encuentro seleccionado es:",
                  metname)
            if i == "18" or i == "19" or i == "20":#casos especiales
                descmet = infometenc["names"][0]["name"]
                print("Descripcion:", descmet)
                opc_guardadomet = menus.verif_his(historico)
                if opc_guardadomet == 1:
                    guarmet = guardadoh.Esc_archi_met(metname, descmet,
                                                      cont)#GH
                    cont += 1#aumentamos el contador de consultas
                else:
                    print("\n")
                    continue
            else:
                descmet = infometenc["names"][1]["name"]#todos los demás metodos
                print("Descripcion:", descmet)
                opc_guardadomet = menus.verif_his(historico)
                if opc_guardadomet == 1:
                    guarmet = guardadoh.Esc_archi_met(metname, descmet,
                                                      cont)#GH
                    cont += 1#aumentamos el contador de consultas
                else:
                    print("\n")
                    continue
            print("\n")
        elif opc == 4:#Guardado historico
            gh = menus.verif_his(consultarhis)
            if gh == 1:
              try:
                  nom_arch = "Guardado_Historico.txt"
                  impgrd = guardadoh.Leerarchivos(nom_arch)
                  print(impgrd)
              except FileNotFoundError as e:
                  print(f'Error: El archivo {nom_arch} no se encontró. Detalles: {e}''\n')
            else:
              print("\n")
              continue
        else:#opc 5 salida del script
            print("Adios")
            exit()