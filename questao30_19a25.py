def area_triangulo():
    while True:
        try:
            base = float(input("Digite o valor da base (cm): "))
            altura = float(input("Digite o valor da altura (cm): "))
            if base <= 0 or altura <= 0:
                print("Base e altura devem ser positivas e maiores que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite números válidos.")
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area} cm².")


def area_quadrado():
    while True:
        try:
            lado = float(input("Digite o lado do quadrado (cm): "))
            if lado <= 0:
                print("O lado deve ser positivo e maior que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    area = lado ** 2
    print(f"A área do quadrado é: {area} cm².")


def area_retangulo():
    while True:
        try:
            m = float(input("Digite o menor lado do retângulo (cm): "))
            M = float(input("Digite o maior lado do retângulo (cm): "))
            if m <= 0 or M <= 0:
                print("Os lados devem ser positivos e maiores que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite números válidos.")
    area = m * M
    print(f"A área do retângulo é: {area} cm².")


def area_losango():
    while True:
        try:
            d = float(input("Digite a diagonal menor (cm): "))
            D = float(input("Digite a diagonal maior (cm): "))
            if d <= 0 or D <= 0:
                print("As diagonais devem ser positivas e maiores que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite números válidos.")
    area = (d * D) / 2
    print(f"A área do losango é: {area} cm².")


def area_trapezio():
    while True:
        try:
            b = float(input("Digite a base menor (cm): "))
            B = float(input("Digite a base maior (cm): "))
            h = float(input("Digite a altura (cm): "))
            if b <= 0 or B <= 0 or h <= 0:
                print("Bases e altura devem ser positivas e maiores que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite números válidos.")
    area = ((b + B) * h) / 2
    print(f"A área do trapézio é: {area} cm².")


def area_poligono():
    while True:
        try:
            Q = int(input("Digite a quantidade de lados do polígono: "))
            B = float(input("Digite o comprimento da base (cm): "))
            A = float(input("Digite a apótema (cm): "))
            if Q < 3:
                print("O polígono deve ter pelo menos 3 lados.")
            elif B <= 0 or A <= 0:
                print("Base e apótema devem ser positivas e maiores que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite números válidos.")
    area = (Q * B * A) / 2
    print(f"A área do polígono regular é: {area} cm².")


def area_circulo():
    while True:
        try:
            raio = float(input("Digite o raio do círculo (cm): "))
            if raio <= 0:
                print("O raio deve ser positivo e maior que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    pi = 3.1415
    area = pi * (raio ** 2)
    print(f"A área do círculo é: {area:.2f} cm².")


def menu():
    print("\n--- Menu de Áreas ---")
    print("1. Triângulo")
    print("2. Quadrado")
    print("3. Retângulo")
    print("4. Losango")
    print("5. Trapézio")
    print("6. Polígono regular")
    print("7. Círculo")
    print("0. Sair")
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        return -1

while True:
    opcao = menu()
    if opcao == 1:
        area_triangulo()
    elif opcao == 2:
        area_quadrado()
    elif opcao == 3:
        area_retangulo()
    elif opcao == 4:
        area_losango()
    elif opcao == 5:
        area_trapezio()
    elif opcao == 6:
        area_poligono()
    elif opcao == 7:
        area_circulo()
    elif opcao == 0:
        print("Saindo... Até a próxima!")
        break
    else:
        print("Opção inválida. Tente novamente.")
