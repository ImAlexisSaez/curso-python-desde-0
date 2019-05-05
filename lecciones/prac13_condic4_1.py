print("Programa de evaluación de becas - Curso 2018/19")

dist_escuela = int(input("Introduce la distancia a la escuela (en km): "))
print("Distancia a la escuela: " + str(dist_escuela))

num_hermanos = int(input("Introduce el número de hermanos en el centro: "))
print("Número de hermanos: " + str(num_hermanos))

sal_familiar = int(input("Introduce el salario anual bruto: "))
print("Salario anual bruto: " + str(sal_familiar))

if dist_escuela > 40 and num_hermanos > 2 and sal_familiar <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")
