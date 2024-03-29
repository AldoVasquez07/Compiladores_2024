def nombres_funciones_variables(nombre):
    if nombre == "false" or nombre == "true":
        return False

    acepta1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    acepta2 = acepta1 + "0123456789"

    longitud = len(nombre)

    for i in range(longitud):
        consulta = 0

        if i > 0:
            if nombre[i] in acepta2:
                consulta = 1
        else:
            if nombre[i] in acepta1:
                consulta = 1

        if consulta == 0:
            return False

    return True
