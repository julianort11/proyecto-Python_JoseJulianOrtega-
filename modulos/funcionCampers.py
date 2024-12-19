import json
import os
import modulos.ui as menus
import modulos.msg as mensajes

def guardarArchivo(Diccionario, archivo):
    with open(f"./modulos/{archivo}.json", 'w') as f: 
        json.dump(Diccionario, f, indent=4) 
    return True

def abrirArchivo(archivo): 
    with open(f"./modulos/{archivo}.json","r") as entrada:
        nuevoDiccionario = json.load(entrada)
        return nuevoDiccionario
    

camper = abrirArchivo('base_datos')
notas = abrirArchivo('base_datos')
infoClases = abrirArchivo('base_datos')

def registroCamper (baseDatos: dict):  # Aquí encontramos toda la información del camper

    nombres = input("Ingresa tu nombre: ").capitalize()
    apellidos = input("Ingresa tus apellidos: ").capitalize()
    numeroDocumento = int(input("Ingresa su numero de identificación: "))
    direccion = input("Ingresa tu dirección: ").capitalize()
    acudiente = input("Ingresa nombre de tu acudiente: ").capitalize()
    telefonoCel = int(input("Ingresa tu numero celular de contacto: "))
    telefonoFijo = int(input("Ingresa tu numero fijo de contacto (si no aplica coloca 0): "))

    informacion = {
        "nombre" : nombres,
        "apellidos" : apellidos,
        "numeroDocumento" : numeroDocumento,
        "direccion" : direccion,
        "acudiente" : acudiente,
        "telefonos" : {
            "celular" : telefonoCel,
            "fijo" : telefonoFijo,
        },
        "estado" : {
            "En proceso" : True,
            "inscrito" : False,
            "Aprobado" : False,
            "Denegado" : False,
            "Cursando" : False,
            "Graduado" : False,
            "Expulsado" : False,
            "Retirado" : False
        },
        "riesgo" : {
            "En revision" : False,
            "Continua en campus": False,
            "Posible expulcion": False,
            "No continua en campus": False
        },
        "clasesAsignadas": {
            "j1": {
                "horario": "6:00Am - 9:30Am",
                "ruta": {
                    "NoteJS": False,
                    "Java": False,
                    "NetCore": False
                },
                "estudiantes": 0,
                "salon": "apolo"
            },
            "j2": {
                "horario": "10:00Am - 1:30Pm",
                "ruta": {
                    "NoteJS": False,
                    "Java": False,
                    "NetCore": False
                },
                "estudiantes": 0,
                "salon": "apolo"
            }
        },
        "notas" : {
            "teoria" : 0,
            "practicos" : 0,
            "quizes" : 0,
        }
    }

    baseDatos["camper"].append(informacion)
    guardarArchivo(baseDatos,"base_datos")    
    print(f"Su usuario fue guardado exitosamente, tu ingreso es con tu numero de documento {numeroDocumento}") 
    return baseDatos

# ----------------------------------------------------------------------------------------------------------------------------

def mostrarNotas (notas:dict):  # Imprimimos las notas de los campers

    print(mensajes.notasCamper)
    print(f"teoría: {notas.get('teorica', 'No disponible')}")
    print(f"práctico: {notas.get('practicos', 'No disponible')}")
    print(f"quizzes: {notas.get('quizes', 'No disponible')}")

def informacionClases (infoClases:dict):  # Ver información de clases

    print(mensajes.msgHorario)
    print(f"horarios: {infoClases['clasesAsignadas']}")

# ----------------------------------------------------------------------------------------------------------------------------

def ingresarCamper(baseDatos: dict):  # Buscar camper
    while True:  # Añadimos un bucle para poder regresar al menú si el documento no se encuentra
        documentoIngreso = int(input("Ingresa tu número de identificación para ingresar: "))

        encontrado = False  
        for camper in baseDatos.get("camper", []): 
            if documentoIngreso == camper["numeroDocumento"]: 
                encontrado = True
                nombreCamper = camper["nombre"]
                print(f"""
                    ====================================
                      Camper encontrado: {nombreCamper}
                    ====================================
                    """)
                while True:  # Este bucle permitirá al usuario regresar al menú anterior
                    print(menus.menuDentroingreso)
                    opcionDenIngreso = int(input(":)_ "))

                    match opcionDenIngreso:
                        case 1:  # Mostrar notas
                            mostrarNotas(camper["notas"])
                        case 2:  # Ver información de clases
                            informacionClases(camper)
                        case 3:  # Volver al menú anterior
                            return  # Sale de la función y regresa al menú anterior
                    os.system('pause')
                break
        else:
            print("""
                =======================
                Documento no encontrado
                =======================
            """)
            os.system('pause')
            return  # Regresa al menú anterior si el documento no se encuentra
