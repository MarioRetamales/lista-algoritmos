def fahrenheit_para_celsius():
    while True:
        try:
            temp = float(input("Digite a temperatura em Fahrenheit: "))
            if temp < -459.67:
                print("A temperatura não pode ser inferior ao zero absoluto (-459,67°F).")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    print("A temperatura em Celsius é:", (5/9) * (temp - 32))


def celsius_para_fahrenheit():
    while True:
        try:
            temp = float(input("Digite a temperatura em Celsius: "))
            if temp < -273.15:
                print("A temperatura não pode ser inferior ao zero absoluto (-273,15°C).")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    print("A temperatura em Fahrenheit é:", (9/5) * temp + 32)


def celsius_para_kelvin():
    while True:
        try:
            temp = float(input("Digite a temperatura em Celsius: "))
            if temp < -273.15:
                print("A temperatura não pode ser inferior ao zero absoluto (-273,15°C).")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    print("A temperatura em Kelvin é:", temp + 273.15)


def kelvin_para_celsius():
    while True:
        try:
            temp = float(input("Digite a temperatura em Kelvin: "))
            if temp < 0:
                print("A temperatura em Kelvin não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    print("A temperatura em Celsius é:", temp - 273.15)


def celsius_para_rankine():
    while True:
        try:
            temp = float(input("Digite a temperatura em Celsius: "))
            if temp < -273.15:
                print("A temperatura não pode ser inferior ao zero absoluto (-273,15°C).")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    print("A temperatura em Rankine é:", temp * 9/5 + 491.67)


def rankine_para_celsius():
    while True:
        try:
            temp = float(input("Digite a temperatura em Rankine: "))
            if temp < 0:
                print("A temperatura em Rankine não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    print("A temperatura em Celsius é:", (temp - 491.67) * 5/9)


def fahrenheit_para_kelvin():
    while True:
        try:
            temp = float(input("Digite a temperatura em Fahrenheit: "))
            if temp < -459.67:
                print("A temperatura não pode ser inferior ao zero absoluto (-459,67°F).")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    print("A temperatura em Kelvin é:", (temp - 32) * 5/9 + 273.15)


def kelvin_para_fahrenheit():
    while True:
        try:
            temp = float(input("Digite a temperatura em Kelvin: "))
            if temp < 0:
                print("A temperatura em Kelvin não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    print("A temperatura em Fahrenheit é:", (temp - 273.15) * 9/5 + 32)


def fahrenheit_para_rankine():
    while True:
        try:
            temp = float(input("Digite a temperatura em Fahrenheit: "))
            if temp < -459.67:
                print("A temperatura não pode ser inferior ao zero absoluto (-459,67°F).")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    print("A temperatura em Rankine é:", temp + 459.67)


def rankine_para_fahrenheit():
    while True:
        try:
            temp = float(input("Digite a temperatura em Rankine: "))
            if temp < 0:
                print("A temperatura em Rankine não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    print("A temperatura em Fahrenheit é:", temp - 459.67)


def kelvin_para_rankine():
    while True:
        try:
            temp = float(input("Digite a temperatura em Kelvin: "))
            if temp < 0:
                print("A temperatura em Kelvin não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    print("A temperatura em Rankine é:", temp * 1.8)


def rankine_para_kelvin():
    while True:
        try:
            temp = float(input("Digite a temperatura em Rankine: "))
            if temp < 0:
                print("A temperatura em Rankine não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    print("A temperatura em Kelvin é:", temp / 1.8)


def menu():
    print("\n--- Conversão de Temperatura ---")
    print("1. Fahrenheit → Celsius")
    print("2. Celsius → Fahrenheit")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Celsius → Rankine")
    print("6. Rankine → Celsius")
    print("7. Fahrenheit → Kelvin")
    print("8. Kelvin → Fahrenheit")
    print("9. Fahrenheit → Rankine")
    print("10. Rankine → Fahrenheit")
    print("11. Kelvin → Rankine")
    print("12. Rankine → Kelvin")
    print("0. Sair")
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        return -1

while True:
    opcao = menu()
    if opcao == 1:
        fahrenheit_para_celsius()
    elif opcao == 2:
        celsius_para_fahrenheit()
    elif opcao == 3:
        celsius_para_kelvin()
    elif opcao == 4:
        kelvin_para_celsius()
    elif opcao == 5:
        celsius_para_rankine()
    elif opcao == 6:
        rankine_para_celsius()
    elif opcao == 7:
        fahrenheit_para_kelvin()
    elif opcao == 8:
        kelvin_para_fahrenheit()
    elif opcao == 9:
        fahrenheit_para_rankine()
    elif opcao == 10:
        rankine_para_fahrenheit()
    elif opcao == 11:
        kelvin_para_rankine()
    elif opcao == 12:
        rankine_para_kelvin()
    elif opcao == 0:
        print("Saindo... Valeu!")
        break
    else:
        print("Opção inválida. Tente novamente.")
