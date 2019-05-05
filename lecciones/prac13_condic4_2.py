print("Programa de evaluación de becas - Curso 2018/19")

distancia_escuela = int(input("Introduce la distancia a la escuela (en km): "))
print("Distancia a la escuela: " + str(distancia_escuela))

numero_hermanos = int(input("Introduce el número de hermanos en el centro: "))
print("Número de hermanos: " + str(numero_hermanos))

salario_familiar = int(input("Introduce el salario anual bruto: "))
print("Salario anual bruto: " + str(salario_familiar))

if distancia_escuela > 40 or numero_hermanos > 2 or salario_familiar <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")
