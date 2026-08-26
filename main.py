menu = """
      === menu ===
 ||1. ver candidatos ||
 ||2. votar          ||
 ||3. ver resultados ||
 ||4. salir          ||
"""
continuar = "s"
c1=0
c2=0
c3=0
while (continuar == "s"):

 print (menu)
 print ("---------------------------")
 opcion=int(input("ingrese una opcion: ")) 
 print ("---------------------------")
 match opcion:
  case 1:
   print ("c1")
   print ("c2")
   print ("c3")
   print ("---------------------------")
   continuar = input("¿Desea volver al menú? (s/n): ").lower()
  case 2:
    votacion = int(input("por quien deseas votar?? (1,2,3) "))
    if (votacion == 1):
      print ("---------------------------")
      print ("voto registrado")
      c1 = c1 + 1
    elif (votacion == 2):
     print ("---------------------------")
     print ("voto registrado")
     c2 = c2 + 1 
    elif (votacion == 3):
     print ("---------------------------")
     print ("voto registrado")
     c3 = c3 + 1
    else:
     print ("---------------------------")
     print ("candidato no existe")
     print ("---------------------------")
    continuar = input("¿Desea volver al menú? (s/n): ").lower()
  case 3:
   print (c1)
   print (c2)
   print (c3)
   continuar = input("¿Desea volver al menú? (s/n): ").lower()
  case 4:
   continuar = "n"











#candidatos = array = ("Candidato 1", "Candidato 2", "Candidato 3")
#for candidato in candidatos:
#    print (candidato)
#votacion = int(input("Ingrese el número de votos: "))


# if (opcion == 1):
#  print (candidato)
# elif (opcion == 2):
#  print (candidato)
#votacion = int(input("vote por in candidato: "))
#votos = votos + 1