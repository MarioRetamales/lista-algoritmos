A = float(input("Digite o coeficiente A: "))
B = float(input("Digite o coeficiente B: "))

if A != 0:
    X = -B / A
    print(f"A raiz da equação é X = {X:.2f}")
else:
    print("A equação não é do 1º grau (A não pode ser zero).")
