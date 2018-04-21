import os
os.system("cls")
tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
print(tupla)
#while True:
#	a = int(input("Ingrese un número del 1 al 12: "))
	# if a < 13:
	# 	print(tupla[a-1])
	# 	break
	# else:
	# 	print("Error! Debe ingresar un número menor a 12")
while True:
     try:
         x = int(input("Por favor ingrese un número: "))
         break
     except ValueError:
         print("Oops! No era válido. Intente nuevamente...")
