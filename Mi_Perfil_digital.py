#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Joan Sebastian lizarazo Perez"
edad = 14
estatura = 1.72
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("_joan_Izrxk", "J0an07")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "Mil horas", "artista": "Los abuelos de la nada", "duracion": "2:45"},
{"titulo": "NUEVAYol", "artista": "bad Bunny", "duracion": "3:03"},
{"titulo": "Mañana sera otro dia ", "artista": "Canserbero", "duracion": "3:17"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
for cancion in Playlist:
    print(f"{cancion['titulo']} - {cancion['artista']} ({cancion['duracion']}) min")
print ("----------------------------------")