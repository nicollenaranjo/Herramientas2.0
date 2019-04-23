creditos_totales = 0
ponderado_final = 0
baja = 4.0
nombre_materia = ""


def materia():
    global creditos_totales, creditos, nota_materia, ponderado, promedio, ponderado_final, nombre, baja, nombre_materia
    nombre = str(input("Ingrese nombre de la materia: "))
    nota_materia = eval(input("Ingrese la nota de la materia: "))
    if(nota_materia < baja):
        baja = nota_materia
        nombre_materia = nombre
    creditos = int(input("Ingrese número de creditos: "))
    ponderado = nota_materia  * creditos
    ponderado_final = ponderado_final + ponderado
    print("Su ponderado acumulado es de " + str(ponderado_final))
    creditos_totales = creditos_totales + creditos
    print("Sus créditos son " + str(creditos_totales))
    promedio = ponderado / creditos_totales
    
materia()

def materia_mas():
    global creditos_totales, creditos, nota_materia, ponderado, promedio, ponderado_final, nombre2, nota_materia2, baja, nombre_materia
   ### Insertar nombre materia
    nombre2 = str(input("Ingrese nombre de la materia: "))
    ###
    nota_materia2 = eval(input("Ingrese la nota de la materia: "))
    if(nota_materia2 < baja):
        baja = nota_materia2
        nombre_materia = nombre2
    creditos2 = int(input("Ingrese número de creditos: "))
    ponderado = nota_materia2  * creditos2
    ponderado_final = ponderado_final + ponderado
    print("Su ponderado acumulado es de " + str(ponderado_final))
    creditos_totales = creditos_totales + creditos2
    print("Sus créditos son " + str(creditos_totales))
    promedio = ponderado_final / creditos_totales
    final()
    
        

def final():
    global creditos_totales, creditos, nota_materia, ponderado, promedio, baja, nombre_materia, promedio_final
    x = int(input("¿Desea ingresar otra materia? 1)Sí 2)No "))
    if(x == 1):
        materia_mas()
    if(x == 2):
        print("Su materia más baja es " + str(nombre_materia) + " con una nota de " + str(baja))
        if(promedio == 3.25555555555):
            print("Por poco está en prueba. Su promedio final es de " + str(promedio))
        if(promedio >  3.9):
            print("Su promedio es de " + str(promedio))
        if(promedio < 4):
            print("Su promedio final es de " + str(promedio) + ". Está en prueba académica")
            promedio_final = 7 - promedio  
            print("Deberia usted de sacar un promedio de " + str(promedio_final) + " para salir de prueba académica.")



