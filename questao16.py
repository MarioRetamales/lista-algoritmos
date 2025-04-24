m = float(input("Digite o valor do menor lado paralelo (em centimetros): "))
M = float(input("Digite o valor do maior lado paralelo (em centimetros): "))
O = float(input("Digite o valor do lado perpendicular (em centimetros): "))
perimetro = (m + M) + 2 * O
print(f"O perímetro do trapezio é:", perimetro, "cm")