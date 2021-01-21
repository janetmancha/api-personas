
personas = []

def insertarPersona(nombre, edad):
    personas.append({"nombre": nombre,"edad":edad})
    
def listarPersonas():
    return personas

    # convertir la lista de personas a diccionario
    # dicPersonas = {}
    # for persona in personas:
    #     dicPersonas[persona['nombre']]={"edad":persona['edad'] }
    # return dicPersonas

def buscarPersona(nombre):
    for persona in personas:
        if persona['nombre'] == nombre:
            return persona
    return None

def borrarPersonas():
    personas.clear()
