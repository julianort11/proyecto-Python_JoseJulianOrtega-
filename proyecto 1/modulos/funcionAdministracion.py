import json
import os 
import modulos.msg as mensajes
import modulos.ui as menus

def guardarArchivo(Diccionario, archivo):
    with open(f"./modulos/{archivo}.json", 'w') as f: 
        json.dump(Diccionario, f, indent=4) 
    return True

def abrirArchivo(archivo): 
    with open(f"./modulos/{archivo}.json","r") as entrada:
        nuevoDiccionario = json.load(entrada)
        return nuevoDiccionario

admin_datos = abrirArchivo('base_datos')
crear_grupos = abrirArchivo('base_datos')
trainers_Datas = abrirArchivo('base_datos')
estadoCamper = abrirArchivo('base_datos')
riesgoEstudiante = abrirArchivo('base_datos')
infoCampers = abrirArchivo('base_datos')

# Función para agregar estudiantes a los grupos
def aggGrupos(crear_grupos: dict): 
    salones = input('Ingrese salón que desea ingresar los estudiantes: ')
    campers = int(input('Ingrese el número de documento del alumno a ingresar: '))

    if salones in crear_grupos and campers in crear_grupos["camper"]:
        campers_data = crear_grupos["camper"][campers]
        campers_data["horario"] = crear_grupos[salones]["horario"]
        campers_data["ruta"] = crear_grupos[salones]["ruta"]
        crear_grupos[salones]["estudiantes"][campers] = campers_data
        print(f"Estudiante {campers} agregado al grupo {salones}:)")

        if len(crear_grupos[salones]["estudiantes"]) < 33:
            if "inscrito" in campers_data["estado"] and campers_data["estado"]["inscrito"]:
                print(f"Estudiante {campers} ya estaba inscrito.")
            else:
                print(f"El camper {campers} no pasó el filtro inicial.")
        else:
            print(f"El salón {salones} ya tiene 33 estudiantes, no puedes agregar más.")
    else:
        print("El estudiante o el grupo no existen.")
    
    guardarArchivo(crear_grupos,"base_datos")
    return

# Función para agregar trainers y toda su información
def aggTrainer(trainers_Datas: dict): 
    nombres = input("Ingresa el nombre del nuevo trainer: ")
    documentos = input("Ingrese el número de documento del nuevo trainer: ")
    clases_asignadas = {}
    
    num_clases = int(input("¿Cuántas clases asignadas tiene el nuevo trainer? "))
    
    for i in range(num_clases):
        clave_clase = input(f"Ingrese el identificador para la clase {i+1} (ejemplo: p1, p2, etc.): ")
        horario = input(f"Ingrese el horario para la clase {clave_clase}: ")
        ruta = input(f"Ingrese la ruta para la clase {clave_clase}: ")
        salon = input(f"Ingrese el salón asignado para la clase {clave_clase}: ")
        
        clases_asignadas[clave_clase] = {
            "horario": horario,
            "ruta": ruta,
            "estudiantes": [], 
            "salon": salon
        }
    
    nuevo_trainer = {
        "nombreTrainer": nombres,
        "numeroDocumento": documentos,
        "clasesAsignadas": clases_asignadas
    }

    trainers_Datas["trainerInf"].append(nuevo_trainer)
    guardarArchivo(trainers_Datas, "base_datos")
    print(f'El trainer fue guardado correctamente, ingresado con su número de documento {documentos}')
    return

# Función para buscar un camper y agregar notas de filtro
def camperBuscarNotas(infoCampers: dict): 
    camperBuscar = int(input("Ingrese el número de identificación del camper: "))
    encontrado = False  
    for camper in infoCampers["camper"]: 
        if camperBuscar == camper["numeroDocumento"]: 
            encontrado = True
            nombreCamper = camper["nombre"]
            print(f"""
             ====================================
              Camper encontrado: {nombreCamper}
             ====================================
                """)
            teorico = int(input("Ingrese la nota de la evaluación teórica por el estudiante: "))
            practico = int(input("Ingrese la nota de la evaluación práctica por el estudiante: "))

            nota_final = (teorico * 0.5) + (practico * 0.5)
            print(f"""
             Las notas del estudiante fueron:
             La nota teórica: {teorico}
             La nota práctica: {practico} 
             La nota total de las evaluaciones: {nota_final:.2f}
             """)
            os.system('pause')
            if nota_final >= 60:
                camper['estado'] = {
                    'En proceso': False,
                    'Inscrito': True,
                    'Aprobado': True,
                    'Denegado': False,
                    'Cursando': False,
                    'Graduado': False,
                    'Expulsado': False,
                    'Retirado': False
                }
            else:
                camper['estado'] = {
                    'En proceso': False,
                    'Inscrito': False,
                    'Aprobado': False,
                    'Denegado': True,
                    'Cursando': False,
                    'Graduado': False,
                    'Expulsado': False,
                    'Retirado': False
                }
                print(mensajes.msgEstuReprobado)
            guardarArchivo(infoCampers, "base_datos")
            break

    if not encontrado:
        print(mensajes.msgSinEncontrar)
        return camperBuscar

# Función para definir el estado del camper
def defEstadoCamper(estadoCamper: dict):
    camperBuscar = int(input("Ingrese el número de identificación del camper: "))
    encontrado = False  
    for camper in estadoCamper["camper"]: 
        if camperBuscar == camper["numeroDocumento"]: 
            encontrado = True
            nombreCamper = camper["nombre"]
            print(f"""
             ====================================
              Camper encontrado: {nombreCamper}
             ====================================
                """)
            print(mensajes.msgEstadoCamper)
            estado = input("Ingrese cuál es el estado del camper: ").capitalize()
            
            estadosValidos = ['En proceso', 'Inscrito', 'Aprobado', 'Denegado', 'Cursando', 'Graduado', 'Expulsado', 'Retirado']
            if estado not in estadosValidos:
                print(f"El estado ingresado no es válido. Los estados válidos son: {', '.join(estadosValidos)}")
                break  

            camper["estado"] = {estado: False for estado in estadosValidos}
            camper["estado"][estado] = True
            print(mensajes.msgEstadoFinal)
            print(f"El estado del camper '{nombreCamper}' ha sido actualizado a: {estado}.")
            break
    if not encontrado:
        print(mensajes.msgSinEncontrar)
        guardarArchivo(estadoCamper, "base_datos")
        return camperBuscar

# Función para definir el riesgo del camper
def defRiesgoEstudiante(riesgoEstudiante):
    camperBuscar = int(input("Ingrese el número de identificación del camper: "))
    encontrado = False  

    for camper in riesgoEstudiante["camper"]: 
        if camperBuscar == camper["numeroDocumento"]: 
            encontrado = True
            nombreCamper = camper["nombre"]
            print(f"""
             ====================================
              Camper encontrado: {nombreCamper}
             ====================================
                """)
            print(mensajes.msgRiesgoCamper)
            riesgo = input("Ingrese cuál es el estado del camper: ").capitalize()

            riesgosValidos = ["En revisión", "Continúa en campus", "Posible expulsión", "No continúa en campus"]
            if riesgo not in riesgosValidos:
                print(f"Riesgo no válido. Los riesgos válidos son: {', '.join(riesgosValidos)}")
                break  

            if "riesgo" in camper:
                for clave in riesgosValidos:
                    if clave in camper["riesgo"]:
                        camper["riesgo"][clave] = False

                if riesgo in camper["riesgo"]:
                    camper["riesgo"][riesgo] = True
                    print(f"El riesgo del camper '{nombreCamper}' ha sido actualizado a '{riesgo}'.")
            else:
                print(f"El riesgo '{riesgo}' no existe en la estructura de datos.")
                break
        else:
            print(mensajes.msgRiesgoFinal)
            break
    if not encontrado:
        print(mensajes.msgSinEncontrar)
        guardarArchivo(riesgoEstudiante, "base_datos")
        return camperBuscar

#-------------------------------------------------------------------------------------------------------------------------------------
# Función principal de administración
def administrador(admin_datos: dict): 
    print(mensajes.msgIngresoAdmin)
    documentoIngreso = int(input("Ingresa tu número de identificación para ingresar: "))

    encontrado = False  
    for administrador in admin_datos["administracionInf"]: 
        if documentoIngreso == administrador["numeroDocumento"]: 
            encontrado = True
            nombreBienve = administrador["numeroDocumento"]
            print(f"""
                  ==============================
                  =====:)Bienvenido {nombreBienve}(:=====
                  ==============================  
                 """)

            while True:  # Ciclo para volver al menú después de cada acción
                print(menus.menuAdministracion)
                opcionAdministracion = int(input(":)_ "))
                if opcionAdministracion == 1:  # Agregar alumnos a los salones
                    aggGrupos(crear_grupos)
                elif opcionAdministracion == 2:  # Agregar trainers con su información
                    aggTrainer(trainers_Datas)
                elif opcionAdministracion == 3:  # Información de campers
                    print(menus.menuInformacioncampers)
                    opcionInfoCamper = int(input(":)_ "))
                    if opcionInfoCamper == 1:#agrega notas de admision
                        camperBuscarNotas(infoCampers)
                    elif opcionInfoCamper == 2:#agrega el estado del camper
                        defEstadoCamper(estadoCamper)
                    elif opcionInfoCamper == 3:#agrega riesgo del camper
                        defRiesgoEstudiante(riesgoEstudiante)
                    elif opcionInfoCamper == 4:
                        break
                    else:
                        print(mensajes.mensajeSinOpc)
                        os.system("pause")
                elif opcionAdministracion == 4:  # Agregar nuevas rutas de estudio
                    pass  # Implementar cuando sea necesario
                elif opcionAdministracion == 5:  # Salir
                    break
                else:
                    print(mensajes.mensajeSinOpc)
                    os.system("pause")

        if not encontrado:
            print(mensajes.msgSinEncontrar)
            break  # Si no se encuentra el administrador, se termina el ciclo.
