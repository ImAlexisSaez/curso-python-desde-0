def area_triangulo(b, h):
    return b * h / 2


for b in range(1, 10, 5):
    for h in range(1, 10, 5):
        print(
            f"El área del triángulo de base {b} y altura {h} es {area_triangulo(b, h)}."
        )
