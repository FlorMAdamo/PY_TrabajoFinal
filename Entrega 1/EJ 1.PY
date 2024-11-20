'''
Las plataformas de música online como YouTube y Spotify almacenan la información asociada a las canciones en
estructuras de datos complejas para hacer las búsquedas de manera eficiente. Para esto se deben modelar las
canciones. Implementar el TDA "Cancion" con los siguientes componentes:
Nombre
Artista
Duración
Género musical (6 posibles: Rock, Jazz, Blues, Funk, Reggae y Rap).
Año de edición
Número de likes
Implementar las siguientes operaciones:
Constructor: Debe incluir las validaciones necesarias.
str: Al usar la función print con una variable del tipo canción debe mostrar: 'nombre' - 'artista' ('duracion').
mayorDuracion: Operación que recibe dos canciones por parámetros y retorna la de mayor duración.
agregaLikes: Operación que recibe un número e incrementa la cantidad de likes de la canción en ese número.
masVotada: Operacion que recibe dos canciones y sin son del mismo artista y del mismo género musical, retorna
la que tiene mayor cantidad de likes. En caso contrario debe lanzar una excepción.
'''

class Cancion:
    def __init__(self, nombreCancion="", artista="" , generoMusical="" , duracion=0 , anioEdicion=0 , nroLikes=0): 
        #validacion Genero con un if.
        if generoMusical not in ['Rock','Jazz','Funk', 'Blues','Reggae', 'Rap']:
            raise ValueError("El Genero no es válido.")
        # Validacion de la duracion.
        if duracion <=0:
            raise ValueError("la duracion debe ser un numero positivo")
            
        self.nombreCancion = nombreCancion
        self.artista = artista
        self.generoMusical = generoMusical
        self.duracion = duracion
        self.anioEdicion= anioEdicion
        self.nroLikes=nroLikes
        
    def __str__(self):
        return f' {self.nombreCancion}-  {self.artista} -  ({self.duracion})'
    
    def mayorDuracion(cancion1,cancion2):
        if cancion1.duracion > cancion2.duracion:
            return cancion1
        elif  cancion1.duracion < cancion2.duracion:
            return cancion1
        else:
            return "Es la misma duracion"
    
    def agregaLikes(self,num):
        if num < 0:
            raise ValueError("El numero que se agrega debe ser positivo")
        self.nroLikes +=num
    def masVotadas(cancion1, cancion2):
        if cancion1.artista == cancion2.artista and cancion1.generoMusical == cancion2.generoMusical:
            return cancion1 if cancion1.nroLikes > cancion2.nroLikes else   cancion2 
        else: raise ValueError ("Las canciones no son del mismo artista o genero musical")

cancion1=Cancion("La Doctora","LPDA", "Reggae",2,2004,500)
cancion2=Cancion("Peldaño","LPDA", "Rock",4,2002,100)

#se muestra  nombre de la cancion - artista - duracion
print(cancion1)
print(cancion1.generoMusical, cancion1.anioEdicion,cancion1.nroLikes)
print(cancion2)
print(cancion2.generoMusical, cancion2.anioEdicion,cancion2.nroLikes)



#comparar duracion de  2 canciones

cancionMayorDuracion= Cancion.mayorDuracion(cancion1,cancion2)
print(f'La cancion con mayor duracion es: {cancionMayorDuracion}')


#recibe un nro y agrega likes 

cancion1.agregaLikes(10)
print(f' Likes de {cancion1.nombreCancion} despues de agregar likes : {cancion1.nroLikes}')
cancion2.agregaLikes(525)
print(f' Likes de {cancion2.nombreCancion} despues de agregar likes : {cancion2.nroLikes}')



#masVotada
try: 
    cancion_mas_votada = Cancion.masVotadas (cancion1,cancion2)
    print(f'LA CANCION MAS VOTADA ES: { cancion_mas_votada}')
except ValueError as error:
    print(error)
