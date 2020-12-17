
print('PROGRAMA PARA CALCULAR SU AGUINALDO')

nombre= input('¿Cuál es su nombre? ')
dui=int(input('¿Cuál es su DUI? '))
nit=int(input('¿Cuál es su NIT? '))
sueldo=int(input('¿Cuál es su salario? '))

print('Cuántos años lleva en la empresa')

def tiempo():
	print("1. De 1 a 3 años // Elija opción 1")
	print("2. De 4 a 9 años // Elija opción 2")
	print("3. De 10 años o más // Elija opción 3")
	opcion = input("-->")
	return opcion

op = tiempo()

if op == "1":
	aguinaldo1=(sueldo/30)*15
	print("Estimado", nombre +  "\n DUI:", str(dui) + " \n NIT:",str(nit))
	print( "Su aguinaldo es $",aguinaldo1)
elif op == "2":
	aguinaldo2=(sueldo/30)*19
	print("Estimado", nombre +  "\n DUI:", str(dui) + " \n NIT:",str(nit))
	print('Su aguinaldo es $',aguinaldo2)
elif op == "3":	
	aguinaldo3=(sueldo/30)*21
	print("Estimado", nombre +  "\n DUI:", str(dui) + " \n NIT:",str(nit))
	print('Su aguinaldo es $',aguinaldo3)
else:
	print("No a elegido ninguna de la opciones disponible, favor intente de nuevo")



	







