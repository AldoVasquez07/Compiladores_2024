import os


def lectura(direccion_archivo, nombre_archivo):
    variables = []

    ruta_prueba = os.path.join(os.path.expanduser("~"), direccion_archivo, nombre_archivo)

    with open(ruta_prueba, 'r') as archivo:
        for linea in archivo:

            parte1 = ''
            parte2 = ''
            parte3 = ''
            parte4 = ''
            caso_coment = False
            caso_literal = False

            if '#' not in linea: # and "'" not in linea:
                variables.append(linea.strip())
            else:
                cant = 0
                if '#' in linea:
                    caso_coment = dividir_por_comentario(linea, parte1, parte2)

                '''
                if "'" in linea:
                    if caso_coment:
                        cant = determinar_cantidad_comillas(parte1)
                        dividir_por_literal(variables, parte1)
                    else:
                        cant = determinar_cantidad_comillas(linea)
                        dividir_por_literal(variables, linea)
                '''

    return variables


def dividir_por_comentario(linea, parte1, parte2):
    for i in range(len(linea)):
        if linea[i] == '#':
            for j in range(i):
                parte1 += linea[j]

            for j in range(i, len(linea)):
                parte2 += linea[j]

    return True


def determinar_cantidad_comillas(cadena):
    cont = 0

    for i in cadena:
        if i == "'":
            cont += 1

    return cont


def dividir_por_literal(variables, linea):
    acum = ''
    llave = 0
    for i in range(linea):
        if linea[i] == "'":
            if llave == 0:
                variables.append(acum)
                acum = ''
                acum += linea[i]
                llave = 1
            else:
                acum += linea[i]
                variables.append(acum)
                acum = ''
                llave = 0
        else:
            acum += linea[i]

    if acum != '':
        variables.append(acum)
