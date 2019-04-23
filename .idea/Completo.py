sumaCreditos = 420
ponderado = 0
horario = []
ponderadoFinal = 500
cursos = int(input("Ingrese la cantidad de cursos: "))

for a in range(cursos):
     materia = [] 
     nombre = input("Ingrese el nombre de la materia: ")
     creditos = int(input("Ingrese los créditos de la materia: "))
     nota = float(input("Ingrese la nota de la materia: "))
     materia.append(nota) 
     materia.append(nombre)
     horario.append(materia) 
     ponderado = creditos * nota
     ponderadoFinal += ponderado
     sumaCreditos += creditos

horario.sort()
print("La nota más baja fue",horario[0][0], "de la materia", horario[0][1])     
promedio = ponderadoFinal/sumaCreditos
print("El promedio es:",promedio)

promedio2 = 100
if (promedio > 4):
     print("No esta en prueba académica")
else:
     print("Esta en prueba académica")
     promedio2 = 7 - promedio
     print("En el próximo semestre debe sacar un promedio de:", promedio2)


