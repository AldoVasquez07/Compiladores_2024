tipo_dec = ["string", "int", "double", "bool"]
token_dec = ["string_dec", "int_dec", "double_dec", "bool_dec"]


def verificar_tipo_declaracion(token):
    if token in tipo_dec:
        return True
    else:
        return False


def determinar_tipo_declaracion(token):
    if token == tipo_dec[0]:
        return token_dec[0]
    elif token == tipo_dec[1]:
        return token_dec[1]
    elif token == tipo_dec[2]:
        return token_dec[2]
    else:
        return token_dec[3]
