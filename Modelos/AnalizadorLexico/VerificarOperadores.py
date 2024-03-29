tokens = ["(", ")", "{", "}", "+", "-", "*",
          "/", "=", "<", ">", "<=", ">=", "==", "!=", "+=", ","]


def determinar_operador(operador):

    if operador in tokens:
        return True
    else:
        return False


def determinar_tipo_operador(operador):
    variables = ["par_left", "par_right", "key_left", "key_right", "ope_plus", "ope_minus",
                 "ope_mult", "ope_div", "ope_equal", "ope_greater", "ope_less",
                 "ope_grater_equal", "ope_less_equal", "ope_compare", "ope_dif", "ope_acum", "comma_sep"]

    indice = tokens.index(operador)

    return variables[indice]
