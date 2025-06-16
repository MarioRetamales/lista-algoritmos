def perimetro_triangulo():
    while True:
        try:
            a = float(input("Digite o valor do lado A (em cm): "))
            b = float(input("Digite o valor do lado B (em cm): "))
            c = float(input("Digite o valor do lado C (em cm): "))
            if a <= 0 or b <= 0 or c <= 0:
                print("Todos os lados devem ser positivos e maiores que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite números válidos.")
    perimetro = a + b + c
    print(f"O perímetro do triângulo é {perimetro} cm.")


def perimetro_quadrado():
    while True:
        try:
            lado = float(input("Digite o valor do lado (em cm): "))
            if lado <= 0:
                print("O lado deve ser positivo e maior que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    perimetro = 4 * lado
    print(f"O perímetro do quadrado/losango é {perimetro} cm.")


def perimetro_retangulo():
    while True:
        try:
            m = float(input("Digite o valor do menor lado (em cm): "))
            M = float(input("Digite o valor do maior lado (em cm): "))
            if m <= 0 or M <= 0:
                print("Os lados devem ser positivos e maiores que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite números válidos.")
    perimetro = 2 * (m + M)
    print(f"O perímetro do retângulo/paralelogramo é {perimetro} cm.")


def perimetro_trapezio():
    while True:
        try:
            m = float(input("Digite o menor lado paralelo (em cm): "))
            M = float(input("Digite o maior lado paralelo (em cm): "))
            O = float(input("Digite o lado perpendicular (em cm): "))
            if m <= 0 or M <= 0 or O <= 0:
                print("Todos os lados devem ser positivos e maiores que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite números válidos.")
    perimetro = (m + M) + 2 * O
    print(f"O perímetro do trapézio é {perimetro} cm.")


def perimetro_poligono():
    while True:
        try:
            Q = int(input("Digite a quantidade de lados do polígono: "))
            L = float(input("Digite o valor do lado (em cm): "))
            if Q < 3:
                print("Um polígono precisa ter pelo menos 3 lados.")
            elif L <= 0:
                print("O lado deve ser positivo e maior que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite números válidos.")
    perimetro = Q * L
    print(f"O perímetro do polígono regular é {perimetro} cm.")


def perimetro_circulo():
    while True:
        try:
            raio = float(input("Digite o raio do círculo (em cm): "))
            if raio <= 0:
                print("O raio deve ser positivo e maior que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    pi = 3.14
    perimetro = 2 * pi * raio
    print(f"O perímetro do círculo é {perimetro} cm.")


def menu():
    print("\n--- Menu de Perímetros ---")
    print("1. Triângulo")
    print("2. Quadrado/Losango")
    print("3. Retângulo/Paralelogramo")
    print("4. Trapézio")
    print("5. Polígono regular")
    print("6. Círculo")
    print("0. Sair")
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        return -1

while True:
    opcao = menu()
    if opcao == 1:
        perimetro_triangulo()
    elif opcao == 2:
        perimetro_quadrado()
    elif opcao == 3:
        perimetro_retangulo()
    elif opcao == 4:
        perimetro_trapezio()
    elif opcao == 5:
        perimetro_poligono()
    elif opcao == 6:
        perimetro_circulo()
    elif opcao == 0:
        print("Saindo... Até a próxima!")
        break
    else:
        print("Opção inválida. Tente novamente.")
