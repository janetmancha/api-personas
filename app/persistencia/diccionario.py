
personas = {}

def insertarPersona(nombre, edad):
    personas[nombre]={"edad":edad}
    
def listarPersonas():
    #return personas

    # convertir el diccionario de personas en lista 
    listaPersonas = []
    for persona in personas:
        listaPersonas.append({"nombre": persona,"edad":personas[persona]["edad"]})
    return listaPersonas

def buscarPersona(nombre):
    if nombre in personas :
        return { "nombre" : nombre, "edad" : personas[nombre]['edad']}
    return None