import os

def menu():
    print("\033[92m=======MENU=======\033[0m")
    print("\033[92m1.\033[0m Ver candidatos")
    print("\033[92m2.\033[0m Votar")
    print("\033[92m3.\033[0m Ver resultados ")
    print("\033[92m4.\033[0m Salir ")
    print("\033[92m==================\033[0m")


def candidatos():
    print("1. Julio Jaramillo")
    print("2. José José")
    print("3. Obama Petro")
    print("\033[92m==================\033[0m")


def resultados():
    total = c1 + c2 + c3
    
    print("=== RESULTADOS ===")
    print(f"Julio Jaramillo: {c1} votos")
    print(f"José José:       {c2} votos")
    print(f"Obama Petro:     {c3} votos")
    print(f"Total de votos:  {total}")
    volverAlMenu()

def volverAlMenu():
    input("\033[92mENTER para volver al menu\033[0m")
c1 = 0
c2 = 0
c3 = 0


while True:
    os.system("cls")
    menu()
    

    try:
        opcion = int(input("\nIngrese una opción: \033[92m"))
        print("==================\033[0m")

        match opcion:

            case 1:
                candidatos()
                volverAlMenu()

            case 2:
                
                edad = int(input("digite su edad: "))
                print("\033[92m==========================\033[0m")
                documento = input("cuenta con cedula?? s/n: ").lower()
                print("\033[92m==========================\033[0m")
                if (edad >= 18 and documento== "s"):
                 candidatos()
                 votacion = int(input("¿Por quién deseas votar?: "))
                 print("\033[92m==========================\033[0m")
                 
                 match votacion:
                    case 1:
                        c1 += 1
                        print("Voto registrado correctamente.")
                        print("==================")

                    case 2:
                        c2 += 1
                        print("Voto registrado correctamente.")
                        print("==================")

                    case 3:
                        c3 += 1
                        print("Voto registrado correctamente.")
                        print("==================")

                    case _:
                        print("Candidato no existe.")
                else: 
                    print("\033[91mNO PUEDES VOTAR!!\033[0m")
                    print("=================")
                    volverAlMenu()
                print("==================")

            case 3:
                resultados()
                print("==================")

            case 4:
                print("Gracias por participar.")
                break
                

            case _:
                print("Opción no válida.")

    except ValueError:
        print("---------------------------")
        print("Debe ingresar un número válido.")
        volverAlMenu()


#    if continuar == "s":
#        continuar = input("¿Desea volver al menú? (s/n): ").lower()
print ("------------------------------------------------")
print("Programa finalizado.")