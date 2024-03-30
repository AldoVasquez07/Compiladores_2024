def imprimir_error(lista_tokens, lista_descripcion):
    error_bool = True
    for i in range(len(lista_descripcion)):
        if "error" in lista_descripcion[i] or "No existe" == lista_descripcion[i]:
            error_bool = False
            print(f"\nError en la linea: {i+1}")
            print(f"Situacion: {lista_tokens[i]}")
            print(f"Motivo: {lista_descripcion[i]}")

    return error_bool
