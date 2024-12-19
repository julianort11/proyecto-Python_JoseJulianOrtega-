import os
import modulos.msg as mensajes
import modulos.ui as menus
import modulos.funcionCampers as funcionCampers
import modulos.funcionTrainers as funcionTrainers
import modulos.funcionAdministracion as funAdmin

# Función principal
if __name__ == "__main__":
    while True:
        os.system("cls")
        # os.system("clear")
        print(mensajes.mensajePrincipal)
        print(menus.menuPricipal)  # Muestra las opciones del menú principal
        OpcionPrincipal = int(input(":)_  "))

        # Menú principal
        match OpcionPrincipal:
            case 1:
                # Registro de campers
                while True:  # Este bucle hace que regrese al menú anterior si elige la opción 2
                    os.system("cls")
                    print(mensajes.mensajeRegistroCamp)
                    print(menus.menuRegistrarse)  # Muestra las opciones de registro
                    OpcionRegistro = int(input(":)_  "))

                    match OpcionRegistro:
                        case 1:
                            funcionCampers.registroCamper(funcionCampers.camper)
                            os.system('pause')
                        case 2:  # Regresar al menú principal
                            break  # Esto sale del bucle y vuelve al menú principal
                        case _:
                            print(mensajes.mensajeSinOpc)
                            os.system('pause')
            case 2:
                # Roles: campers, trainers y administrativos
                while True:  # Este bucle hace que regrese al menú anterior si elige la opción 4
                    os.system("cls")
                    print(mensajes.mensajeRol)
                    print(menus.menuIngresar)  # Muestra las opciones para los roles
                    opcionRol = int(input(":)_ "))

                    match opcionRol:
                        case 1:  # Los campers ingresan
                            funcionCampers.ingresarCamper(funcionCampers.camper)
                            os.system('pause')
                        case 2:  # Los trainers ingresan
                            funcionTrainers.trainer(funcionTrainers.trainers_Datas)
                        case 3:  # Los administrativos ingresan
                            funAdmin.administrador(funAdmin.admin_datos)
                        case 4:  # Regresar al menú principal
                            break  # Esto sale del bucle y vuelve al menú principal
                        case _:
                            print(mensajes.mensajeSinOpc)
                            os.system('pause')
            case 3:
                # Salir del programa
                break
            case _:
                print(mensajes.mensajeSinOpc)
                os.system('pause')