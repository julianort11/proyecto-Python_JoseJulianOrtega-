import os
import json 
import modulos.msg as mensajes
import modulos.ui as ui
import modulos.funcionCampers as funciones

def guardarArchivo(Diccionario, archivo):
    with open(f"./modulos/{archivo}.json", 'w') as f: 
        json.dump(Diccionario, f, indent=4) 
    return True

def abrirArchivo(archivo): 
    with open(f"./modulos/{archivo}.json","r") as entrada:
        nuevoDiccionario = json.load(entrada)
        return nuevoDiccionario

trainers_Datas = abrirArchivo('base_datos')

def trainer(trainers_Datas: dict):  # Encontramos al usuario en la base de datos
    print(mensajes.msgIngresoTrainers)
    nombreingresado = input('Ingrese su nombre trainer: ').capitalize()
    encontrado = False  
    
    for trainers in trainers_Datas["trainerInf"]: 
        if nombreingresado == trainers["nombreTrainer"]: 
            encontrado = True
            nombreBienve = trainers["nombreTrainer"]
            print(f"""
                  ==============================
                  =====:)Bienvenido {nombreBienve}(:=====
                  ==============================  
                 """)
            # Menú de opciones para el trainer
            while True:  # Bucle que permite regresar al menú de opciones
                print(ui.menuTrainer)
                opcionTrainer = int(input(':)_ '))
                match opcionTrainer:
                    case 1:  # El trainer tiene la opción de agregar las notas
                        salon = input("Ingrese el salón al que desea agregar notas: ")
                        camperNotas = input("Ingrese el número de documento del camper que desea agregarle notas: ")
                        
                        campers = funciones.abrirArchivo('base_datos')

                        if salon in campers["camper"] and any(camper["numeroDocumento"] == int(camperNotas) for camper in campers["camper"]):

                            camperEncontrado = next(camper for camper in campers["camper"] if camper["numeroDocumento"] == int(camperNotas))

                            print('Ingrese las notas del estudiante:', camperEncontrado)
                            teorica = float(input('Ingrese nota teórica: '))
                            practica = float(input('Ingrese nota de la práctica: '))
                            quizes = float(input('Ingrese nota de quizzes: '))

                            camperEncontrado['notas']['teorica'] = teorica
                            camperEncontrado['notas']['practica'] = practica
                            camperEncontrado['notas']['quizes'] = quizes
                            guardarArchivo(camperEncontrado, 'camper')
                            print('Notas actualizadas correctamente:', camperEncontrado["notas"])

                        else:
                            print("Error: salón o grupo no encontrado.")
                            return 

                    case 2:  # Información sobre las clases del trainer
                        print(ui.menuInfoClases)
                        opcionInfo = int(input(':)_ '))
                        match opcionInfo:
                            case 1:  # Ver los módulos del profesor
                                pass  # Agregar lógica aquí si es necesario
                            case 2:  # Ver cursos con estudiantes
                                for trainer in trainers_Datas["trainerInf"]:
                                    if trainer["nombreTrainer"] == nombreingresado:
                                        clases_asignadas = trainer["clasesAsignadas"]
                                        for clase, datos_clase in clases_asignadas.items():
                                            ruta = datos_clase["ruta"]
                                            print(f'Tus módulos son: {ruta}')
                            case 3:  # Ver las notas de los campers
                                camperNotas = input("Ingrese el número de documento del camper que desea ver notas: ")
                                for camper in trainers_Datas["camper"]:
                                    if camperNotas == camper["numeroDocumento"]:
                                        notasCamper = funciones.baseDatos[camper["numeroDocumento"]]['notas']
                                        print('Notas del estudiante:', notasCamper)
                            case 4:  # Volver al menú anterior
                                return  # Sale de la función y regresa al menú anterior

                    case 3:  # Regresar al menú principal
                        return  # Sale de la función y regresa al menú principal

                    case _:
                        print(mensajes.mensajeSinOpc)
                
                os.system("pause")
                break
        else:
            print("""
              =====================================
              === Identificación no encontrada ===
              =====================================
              """)
            os.system("pause")
    
    return nombreingresado
