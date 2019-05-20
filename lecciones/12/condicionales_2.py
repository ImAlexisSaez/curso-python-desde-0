sal_presidente = int(input("Introduce el salario del presidente: "))
print("Salario presidente: " + str(sal_presidente))

sal_director = int(input("Introduce el salario del director: "))
print("Salario director: " + str(sal_director))

sal_jefe_area = int(input("Introduce el salario del jefe de área: "))
print("Salario jefe de área: " + str(sal_jefe_area))

sal_administrativo = int(input("Introduce el salario del administrativo: "))
print("Salario administrativo: " + str(sal_administrativo))

if sal_administrativo < sal_jefe_area < sal_director < sal_presidente:
    print("Todo funciona correctamente.")
else:
    print("Algo falla en esta empresa.")
