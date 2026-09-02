def menu():
    print("===MENU===")
    print("1. Ver candidatos")
    print("2. Votar")
    print("3. Ver resultados ")
    print("4. Salir ")
    print("==================")


def candidatos():
    print("1. Julio Jaramillo")
    print("2. José José")
    print("3. Obama Petro")
    print("==================")

def resultados():
    total = c1 + c2 + c3
    
    print("=== RESULTADOS ===")
    print(f"Julio Jaramillo: {c1} votos")
    print(f"José José:       {c2} votos")
    print(f"Obama Petro:     {c3} votos")
    print(f"Total de votos:  {total}")


c1 = 0
c2 = 0
c3 = 0

continuar = "s"

while continuar == "s":

    menu()
    print("==================")

    try:
        opcion = int(input("Ingrese una opción: "))
        print("==================")

        match opcion:

            case 1:
                candidatos()
              

            case 2:
                candidatos()
                

                votacion = int(input("¿Por quién deseas votar?: "))
                print("==================")

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

                print("==================")

            case 3:
                resultados()
                print("==================")

            case 4:
                print("Gracias por participar.")
                continuar = "n"
                

            case _:
                print("Opción no válida.")

    except ValueError:
        print("---------------------------")
        print("Debe ingresar un número válido.")

    print("---------------------------")

    if continuar == "s":
        continuar = input("¿Desea volver al menú? (s/n): ").lower()
print ("------------------------------------------------")
print("Programa finalizado.")