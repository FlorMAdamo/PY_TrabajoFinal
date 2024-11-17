'''
Un número narcisista (o número de Armstrong) es un número que es igual a la suma de sus propios dígitos
elevados a la potencia del número de dígitos. Escribe un algoritmo que averigue si un numero dado es narcisista o
no. Por ejemplo: 153 es un número narcisista porque 1^3 + 5^3 + 3^3 = 153
'''


def num_narcisista(num):
    #Convierte el numero a cadena sobre cada digito.
    num_str = str(num)
    #Obtiene la longitud del núimero para usarlo como exponente.
    num_digitos = len(num_str)
    
    suma=0
    
    for digito in num_str:
        suma += int(digito) ** num_digitos
#El resultado es True (booleano) si la suma es igual al numero original, False escenario contrario.
    return suma == n

n=153
if num_narcisista (n):
    print(f"{n} es un numero es_narcisista")
    
else:
    print(f"{n} NO  es un numero es_narcisista")