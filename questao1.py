while True:
    try:
        temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        if temperatura_fahrenheit < -459.67:
            print("A temperatura não pode ser inferior ao zero absoluto (-459.67°F). Tente novamente.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

temperatura_celsius = (5/9) * (temperatura_fahrenheit - 32)
print("A temperatura em Celsius é:", temperatura_celsius)
