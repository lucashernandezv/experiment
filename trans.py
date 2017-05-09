def transposicion_igualespositivos():
  
  esf1=float(input("Ingrese ESF +: "))
  cil1=float(input("Ingrese CIL +: "))
  eje1=int(input("Ingrese eje: "))
  
  esf2=esf1+cil1
  cil2=cil1
  eje2=eje1+90
  eje3=eje2-180
  print("")
  print("+ "+str(esf1)+" esf () + "+str(cil1)+" cil a "+str(eje1)+" grados.")
  if eje2>180:
    print("Transpuesto queda: + "+str(esf2)+" esf () - "+str(cil2)+" cil a "+str(eje3)+" grados.")
  else:
    print("Transpuesto queda: + "+str(esf2)+" esf () - "+str(cil2)+" cil a "+str(eje2)+" grados.")
  
def transposicion_masmenos():
  
  esf1=float(input("Ingrese ESF +: "))
  cil1=float(input("Ingrese CIL -: "))
  eje1=int(input("Ingrese eje: "))
  
  esf2=esf1-cil1
  cil2=cil1
  eje2=eje1+90
  eje3=eje2-180
  print("")
  print("+ "+str(esf1)+" esf () - "+str(cil1)+" cil a "+str(eje1)+" grados.")
  if esf2==0 and eje2>180:
    print("Transpuesto queda ESF "+str(esf2)+" () + "+str(cil2)+" cil a "+str(eje3)+" grados.")
    print("")
  elif esf2==0:
    print("Transpuesto queda ESF "+str(esf2)+" () + "+str(cil2)+" cil a "+str(eje2)+" grados.")
    print("")
  elif esf1>cil1 and eje2>180:
    print("Transpuesto queda: + "+str(esf2)+" esf () + "+str(cil2)+" cil a "+str(eje3)+" grados.")
    print("")
  elif esf1>cil1:
    print("Transpuesto queda: + "+str(esf2)+" esf () + "+str(cil2)+" cil a "+str(eje2)+" grados.")
    print("")
  elif esf1<cil1 and eje2>180:
    print("Transpuesto queda: + "+str(esf2)+" esf () + "+str(cil2)+" cil a "+str(eje3)+" grados.")
    print("")
  elif esf1<cil1:
    print("Transpuesto queda: + "+str(esf2)+" esf () + "+str(cil2)+" cil a "+str(eje2)+" grados. ")
    print("")
    
def transposicion_menosmas():
  esf1=float(input("Ingrese ESF -: "))
  cil1=float(input("Ingrese CIL +: "))
  eje1=int(input("Ingrese eje: "))
  
  esf2=esf1-cil1
  cil2=cil1
  eje2=eje1+90
  eje3=eje2-180
  
  print("")
  print("- "+str(esf1)+" esf ()+ "+str(cil1)+" cil a "+str(eje1)+" grados.")
  if esf2==0 and eje2>180:
    print("Transpuesto queda ESF "+str(esf2)+" () - "+str(cil2)+" cil a "+str(eje3)+" grados.")
    print("")
  elif esf2==0:
    print("Transpuesto queda ESF "+str(esf2)+" () - "+str(cil2)+" cil a "+str(eje2)+" grados.")
    print("")
  elif esf1>cil1 and eje2>180:
    print("Transpuesto queda + "+str(esf2)+" () - "+str(cil2)+" cil a "+str(eje3)+" grados.")
    print("")
  elif esf1>cil1:
    print("Transpuesto queda + "+str(esf2)+" () - "+str(cil2)+" cil a "+str(eje2)+" grados.")
    print("")
  elif esf1<cil1 and eje2>180:
    print("Traspuesto queda - "+str(esf2)+" () - "+str(cil2)+" cil a "+str(eje3)+" grados.")
  elif esf1<cil1:
    print("Traspuesto queda - "+str(esf2)+" () - "+str(cil2)+" cil a "+str(eje2)+" grados.")
    print("")
    

def displayMenu():
  print("")
  print("Transponer")
  print("1.Esf+ () Cil+ a Esf+ () Cil-")
  print("2.Esf- () Cil+ a Esf- () Cil-")
  print("3.Esf+ () Cil- a Esf+ () Cil+")
  print("4. Salir")
  
menu=True
while menu:
  displayMenu()
  choice=str(input("Elija una opcion: "))
  if choice == "1":
    transposicion_igualespositivos()
  elif choice=="2":
    transposicion_menosmas()
  elif choice=="3":
    transposicion_masmenos()
  elif choice=="4":
    menu=False
  else: 
    print("Ingrese una opción valida.")
