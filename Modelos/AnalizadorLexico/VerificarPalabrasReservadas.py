palabras_reservadas = ["def", "if", "else", "for", "and", "or", "receive", "show", "principal", "return"]


def determinar_palabras_reservadas(reservada):
    if reservada in palabras_reservadas:
        return True
    else:
        return False


def determinar_tipo_palabra_reservada(reservada):
    tipo_reservada = ["kw_def", "kw_if", "kw_else", "kw_for", "kw_and", "kw_or", "kw_receive", "kw_show",
                      "kw_principal", "kw_return"]

    indice = palabras_reservadas.index(reservada)

    return tipo_reservada[indice]
