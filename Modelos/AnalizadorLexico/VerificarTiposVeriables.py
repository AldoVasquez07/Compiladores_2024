def tipo_variable(var):
    if "'" in var:
        if verificar_string(var):
            return "String"
        else:
            return "error: String"
    elif "." in var:
        if verificar_double(var):
            return "Double"
        else:
            return "Error: Double"
    elif var == "false" or var == "true":
        return "Boolean"
    else:
        if verificar_int(var):
            return "Int"
        else:
            return "No existe"


def verificar_string(var):
    if var[0] == "'":
        tam = len(var)
        if var[tam - 1] == "'":
            return True
        else:
            return False
    else:
        return False


def verificar_double(double):
    nums = "0123456789"
    cant_dot = 0
    caso_negativo = 0

    tam = len(double)

    if double[0] == "." or double[tam-1] == ".":
        return False

    if tam >= 2:
        if double[0] == "0" and double[1] != ".":
            return False

    if '-' in double:
        if double[0] != "-":
            return False
        else:
            if (double[1] == "0" and double[2] != ".") and tam >= 2:
                return False

        caso_negativo = 1

    # Verifica si cumple con las caracteristicas de un double
    for i in range(tam):
        if caso_negativo == 1 and i == 0:
            i = i + 1

        if cant_dot <= 1:
            if double[i] not in nums:
                if double[i] == ".":
                    cant_dot = cant_dot + 1
                else:
                    return False
        else:
            return False

    # Manegar cuando el double termina en muchos ceros
    if tam > 3 and double[tam-1] == "0":
        for i in range(tam-1, -1, -1):
            if double[i] == "0":
                double = double[:-1]
            else:
                break

    return True


def verificar_int(entero):
    nums = "0123456789"
    tam = len(entero)
    caso_negativo = 0

    if tam > 1:
        if entero[0] == "0":
            return False

        if entero[1] == "-":
            if tam == 1:
                return False

        caso_negativo = 1

    for i in range(caso_negativo, tam):
        if entero[i] not in nums:
            return False

    return True
