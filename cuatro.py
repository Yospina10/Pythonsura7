#Crear menú empanadas
contador=0
empanada=
print("1. Agregar empanadas")
print("2. Mostrar empanadas")
print("3. Salir")
while(contador!=3):
    contador=int(input("Digite la opción: "))
    if (contador==1):
        print("Agregando empanadas")

    elif (contador==2):
        print("Mostrar empanadas")
    elif(contador==3):
        print("Salir")
        break
    else:
        print("Opción Inválida")
