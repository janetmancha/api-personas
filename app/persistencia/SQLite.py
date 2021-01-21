import sqlite3

conexion = None
cursor = None

def crearConexionBD():
    #conexion
    global conexion
    global cursor

    if conexion == None:
        conexion = sqlite3.connect("file::memory:?cache=shared")
        #crear cursor
        cursor = conexion.cursor()
        #crear tabla
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS personas(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre varchar(255),  
            edad int(255)
        );
        """)
        #guardar cambios
        conexion.commit()
 

def insertarPersona(nombre, edad):
    crearConexionBD()
    cursor.execute(f"INSERT INTO personas VALUES (null,'{nombre}', {edad})")
    conexion.commit()
    
def listarPersonas():
    crearConexionBD()

    cursor.execute("SELECT * FROM personas")
    personas = cursor.fetchall()

    return [{"nombre": persona[1],"edad":persona[2]} for persona in personas]

    # listaPersonas = []

    # for persona in personas:
    #     listaPersonas.append({"nombre": persona[1],"edad":persona[2]})
    
    # return listaPersonas

def buscarPersona(nombre):
    crearConexionBD()
    cursor.execute(f"SELECT * FROM personas WHERE nombre='{nombre}' LIMIT 1")
    persona = cursor.fetchone()

    if persona: 
        return {"nombre": persona[1],"edad":persona[2]}
    return None


def borrarPersonas():
    crearConexionBD()
    cursor.execute("DELETE FROM personas")
    conexion.commit()
