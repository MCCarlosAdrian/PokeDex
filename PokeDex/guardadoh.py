def Esc_archi_info(a, b, c, d, e):#función para guardado infogralpokemon
    fo = open("Guardado_Historico.txt","a")
    fo.write(f"Consulta{e}""\n")
    fo.write(str(a) + "\n")
    fo.write(str(b) + "mts""\n")
    fo.write(str(c) + "kg""\n")
    fo.write(str(d) + "\n")
    fo.write("\n")
    fo.close()

def Esc_archi_hab(a, b, c):#función guardado habitat
    fo = open("Guardado_Historico.txt", "a")
    fo.write(f"Consulta{c}""\n")
    fo.write(str(a) + "\n")
    fo.write(str(b) + "\n")
    fo.write("\n")
    fo.close()

def Esc_archi_met(a, b, c):#funcion guardado metodos
    fo = open("Guardado_Historico.txt", "a")
    fo.write(f"Consulta{c}""\n")
    fo.write(str(a) + "\n")
    fo.write(str(b) + "\n")
    fo.write("\n")
    fo.close()

def Esc_archi_promp(a, b):#funcion guardado promedio peso
    fo = open("Guardado_Historico.txt", "a")
    fo.write(f"Consulta{b}""\n")
    fo.write("promedio peso: " + str(a) + "\n")
    fo.write("\n")
    fo.close()

def Esc_archi_proma(a, b):#funcion guardado promedio peso
  fo = open("Guardado_Historico.txt", "a")
  fo.write(f"Consulta{b}""\n")
  fo.write("promedio altura: " + str(a) + "\n")
  fo.write("\n")
  fo.close()

def Esc_archi_moda(a, b):#funcion guardado moda
  fo = open("Guardado_Historico.txt", "a")
  fo.write(f"Consulta{b}""\n")
  fo.write("moda: " + str(a) + "\n")
  fo.write("\n")
  fo.close()

def Leerarchivos(a):
    with open(a, "r") as archivo:
        historial = archivo.read()
    return historial
    