import random
import json

# Listas para generar valores aleatorios para cada campo
nombres = ["Julian", "Carlos", "Maria", "Ana", "Pedro", "Laura", "Luis", "Camila", "Sofia", "Jorge"]
apellidos = ["Ortega", "Martinez", "Perez", "Gonzalez", "Lopez", "Rodriguez", "Sanchez", "Fernandez", "Diaz", "Ruiz"]
direcciones = ["Oriental", "Central", "Occidental", "Norte", "Sur", "Este", "Oeste"]
acudientes = ["Jose", "Ana", "Pedro", "Carlos", "Maria"]
salones = ["apolo", "zeus", "hera", "athena", "poseidon"]

# Generar un camper con datos aleatorios
def generar_camper(numero):
    camper = {
        "nombre": random.choice(nombres),
        "apellidos": random.choice(apellidos),
        "numeroDocumento": 100000000 + numero,  # Genera un número de documento único
        "direccion": random.choice(direcciones),
        "acudiente": random.choice(acudientes),
        "telefonos": {
            "celular": random.randint(3000000000, 3999999999),  # Genera un número celular aleatorio
            "fijo": random.randint(1000000, 9999999) if random.random() > 0.5 else 0  # Aleatoriamente puede ser 0
        },
        "estado": {
            "En proceso": random.choice([True, False]),
            "Inscrito": random.choice([True, False]),
            "Aprobado": random.choice([True, False]),
            "Denegado": random.choice([True, False]),
            "Cursando": random.choice([True, False]),
            "Graduado": random.choice([True, False]),
            "Expulsado": random.choice([True, False]),
            "Retirado": random.choice([True, False])
        },
        "riesgo": {
            "En revision": random.choice([True, False]),
            "Continua en campus": random.choice([True, False]),
            "Posible expulcion": random.choice([True, False]),
            "No continua en campus": random.choice([True, False])
        },
        "clasesAsignadas": {
            "j1": {
                "horario": "6:00Am - 9:30Am",
                "ruta": {
                    "NoteJS": random.choice([True, False]),
                    "Java": random.choice([True, False]),
                    "NetCore": random.choice([True, False])
                },
                "estudiantes": random.randint(0, 30),  # Número aleatorio de estudiantes
                "salon": random.choice(salones)
            },
            "j2": {
                "horario": "10:00Am - 1:30Pm",
                "ruta": {
                    "NoteJS": random.choice([True, False]),
                    "Java": random.choice([True, False]),
                    "NetCore": random.choice([True, False])
                },
                "estudiantes": random.randint(0, 30),  # Número aleatorio de estudiantes
                "salon": random.choice(salones)
            }
        },
        "notas": {
            "teoria": random.uniform(0, 100),  # Nota aleatoria de teoría entre 0 y 100
            "practicos": random.uniform(0, 100),  # Nota aleatoria de prácticos entre 0 y 100
            "quizes": random.uniform(0, 100)  # Nota aleatoria de quizes entre 0 y 100
        }
    }
    return camper

# Función para generar los 250 campers
def generar_camperes(numero_camperes=250):
    campers = []
    for i in range(numero_camperes):
        camper = generar_camper(i)  # Genera cada camper con un número único
        campers.append(camper)
    return campers

# Función principal para guardar los campers en un archivo JSON
def guardar_camperes():
    campers = generar_camperes(250)  # Genera 250 campers
    datos = {"camper": campers}
    with open("./modulos/base_datos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
    print("Archivo 'base_datos.json' creado exitosamente con 250 campers.")

# Llamada a la función para generar y guardar los campers
guardar_camperes()