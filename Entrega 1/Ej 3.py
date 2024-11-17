'''CORRECCION de lineas de Codigos.'''

lista ordenada:[2 , 3 , 5, 6, 7, 8]
Números pares en orden descendente: [8, 6, 2]
Números impares en orden descendente: [7, 5, 3]


def separar_ordenar_pares_impares(lista):
    # ORDENAR LA LISTA EN ORDEN ASCENDENTE
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)

    # SEPARAR NUMEROS PARES E IMPARES
    pares = [num for num in lista_ordenada if num % 2 == 0] 
    impares = [num for num in lista_ordenada if num % 2 != 0]  #Error de Lógico: en el operador aritmérico  era / y debe ser % . #Error de tipeo: falta un espacio en el distinto =!.

    # ORDENAR PARES E IMPARES EN ORDEN DESCENDENTE
    pares_desc = sorted(pares, reverse=True)
    impares_desc = sorted(impares, reverse=True)  #Error de tipeo: Debe ser "impares", y la linea decia inpares.

    print("Números pares en orden descendente:", pares_desc)
    print("Números impares en orden descendente:", impares_desc)

#PRUEBA 
lista = (5, 3, 8 , 6, 7 ,2) #Error tipo de dato: Deberia ser corchetes porque es una lista.
separar_ordenar_pares_impares(lista)


lista ordenada: [2, 3, 5, 6, 7, 8].
Números pares en orden descendente: [8, 6, 2].
Números impares en orden descendente: [7, 5, 3].

