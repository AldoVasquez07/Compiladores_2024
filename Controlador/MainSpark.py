from Modelos.OperacionesTxt.Lectura import lectura
from Modelos.AnalizadorLexico.ListandoTokens import listar_tokens_por_linea
from Modelos.AnalizadorLexico.VerificarOperadores import determinar_operador, determinar_tipo_operador
from Modelos.AnalizadorLexico.VerificarIdVariables import nombres_funciones_variables
from Modelos.AnalizadorLexico.VerificarTiposVariables import tipo_variable
from Modelos.OperacionesTxt.Escritura import escribir_archivo
from Modelos.AnalizadorLexico.VerificarPalabrasReservadas import (determinar_palabras_reservadas,
                                                                  determinar_tipo_palabra_reservada)
from Modelos.ControlErrores.ControlLexico import imprimir_error
from Modelos.AnalizadorSintactico.Sintaxis import definiendo_sintaxis
from Modelos.AnalizadorLexico.VerificarDeclaracion import verificar_tipo_declaracion, determinar_tipo_declaracion


def main():
    code = lectura("Desktop", "codigo.txt")
    codigo_separado = listar_tokens_por_linea(code)
    cant_tokens_linea = []
    lista_tokens = []
    lista_descripcion = []

    print(codigo_separado)

    for i in codigo_separado:
        cant_tokens_linea.append(len(i))
        for j in i:
            lista_tokens.append(j)
            if j[0] == '#':
                lista_descripcion.append('hash_comment')
            elif determinar_palabras_reservadas(j):
                lista_descripcion.append(determinar_tipo_palabra_reservada(j))
            elif verificar_tipo_declaracion(j):
                lista_descripcion.append(determinar_tipo_declaracion(j))
            elif determinar_operador(j):
                lista_descripcion.append(determinar_tipo_operador(j))
            elif nombres_funciones_variables(j):
                lista_descripcion.append("id")
            else:
                lista_descripcion.append(tipo_variable(j))

    escribir_archivo("resultado.txt", lista_descripcion, lista_tokens, "Desktop", codigo_separado)

    if imprimir_error(lista_tokens, lista_descripcion):
        print("\nEl analisis lexico termino con exito.")
        # print(definiendo_sintaxis(cant_tokens_linea, lista_tokens, lista_descripcion))
    else:
        print("Error lexico")


if __name__ == '__main__':
    main()
