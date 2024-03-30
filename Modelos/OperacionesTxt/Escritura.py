import os


def escribir_archivo(nombre_archivo, lista_1, lista_2, ruta, codigo_separado):

    ruta_completa = os.path.join(os.path.expanduser("~"), ruta, nombre_archivo)
    cant = (determinar_cadena_mayor(lista_1) % 7)
    tab = ''
    for i in range(cant):
        tab += '\t'
    lista_tam = []

    for i in range(len(codigo_separado)):
        lista_tam.append(len(codigo_separado[i]))

    with open(ruta_completa, 'w') as archivo:
        idx = 0
        for i in range(len(lista_tam)):
            for j in range(lista_tam[i]):
                archivo.write(lista_1[idx] + "\t" + lista_2[idx] + "\t" + str(i+1) + "\t" + str(j+1) + "\n")
                idx += 1


def determinar_cadena_mayor(lista):
    string_mas_largo = max(lista, key=len)
    tam = len(string_mas_largo)
    return tam
