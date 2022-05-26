from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#Apertura del Archivo
files = open("data/datos_clubs.txt", "r", encoding="utf8")
#Lectura del archivo
datos_clubes = files.readlines()

#Ingreso de datos 
for i in range(0,len(datos_clubes),1):
        d=datos_clubes[i].split(";")
        p = Club(nombre=d[0], deporte=d[1],fundacion=d[2])
        session.add(p)
#Cierre del archivo
files.close()

#Apertura del Archivo
files1 = open("data/datos_jugadores.txt", "r", encoding="utf8")
datos_clubes = session.query(Club).all()
#Lectura del archivo
datos_jugadores = files1.readlines()
for i in range(0,len(datos_jugadores),1):
        a=datos_jugadores[i].split(";")
        for club in datos_clubes:
                if a[0] == club.nombre:
                        id_club = club.id
        p = Jugador(nombre=a[3], dorsal=a[2], posicion=a[1], club_id = id_club)
        session.add(p)
#Cierre del archivo
files1.close()
# se confirma las transacciones
session.commit()
