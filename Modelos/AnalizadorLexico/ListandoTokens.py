def listar_tokens_por_linea(code):
    lista_separada = []

    separando = ""
    simb = ["(", ")", "{", "}", "+", "-", "*", "/", "=", "<", ">", "!", ","]
    combinado = ["<=", ">=", "==", "!=", "+="]
    letters_numbers = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"]
    case1 = 0
    for linea in code:
        for i in range(0, len(linea)):

            if case1 == 1 and i < (len(linea)-1):
                i += 1
                case1 = 0

            if linea[i] in simb:
                if i <= (len(linea) - 2):
                    if linea[i+1] in simb and linea[i+1] not in letters_numbers:
                        if (linea[i] + linea[i+1]) in combinado:
                            case1 = 1
                            separando += " " + linea[i] + linea[i+1] + " "

                if case1 == 0:
                    separando += " " + linea[i] + " "

            else:
                separando += linea[i]

        if separando.strip():  # Verifica si separando no está vacío después de quitar los espacios en blanco
            lista_separada.append(separando.split())

        separando = ""

    return lista_separada
