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