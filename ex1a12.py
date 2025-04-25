def fahrenheit_para_celsius():
    temperatura_fahrenheit = input("Digite a temperatura em fahrenheit:")
    temperatura_fahrenheit = float(temperatura_fahrenheit)
    temperatura_celsius =  (5/9) * (temperatura_fahrenheit - 32)
    print("A temperatura em celsius é:",temperatura_celsius)

def celsius_para_fahrenheit():
    temperatura_celsius = input("Digite a temperatura em celsius:")
    temperatura_celsius = float(temperatura_celsius)
    temperatura_fahrenheit =  (9/5) * temperatura_celsius + 32
    print("A temperatura em fahrenheit é:",temperatura_fahrenheit)

def celsius_para_kelvin():
    temperatura_celsius = input("Digite a temperatura em celsius:")
    temperatura_celsius = float(temperatura_celsius)
    temperatura_kelvin =  temperatura_celsius + 273
    print("A temperatura em temperatura kelvin é:",temperatura_kelvin)

def kelvin_para_celsius():
    temperatura_kelvin = input("Digite a temperatura em kelvin: ")
    temperatura_kelvin =float(temperatura_kelvin)
    temperatura_celsius = temperatura_kelvin - 273
    print("A temperatura em celsius sera:",temperatura_celsius)

def celsius_para_rankine():
    temperatura_celsius = input("Digite a temperatura em celsius: ")
    temperatura_celsius =float(temperatura_celsius)
    temperatura_rankine = temperatura_celsius * 9/5 + 491.67
    print("A temperatura em rankine sera:",temperatura_rankine)

def rankine_para_celsius():
    temperatura_rankine = input("Digite a temperatura em rankine: ")
    temperatura_rankine =float(temperatura_rankine)
    temperatura_celsius = (temperatura_rankine - 491.67) * 5/9
    print("A temperatura em celsius será:",temperatura_celsius)

def fahrenheit_para_kelvin():
    temperatura_fahrenheit = input("Digite a temperatura em fahrenheit: ")
    temperatura_fahrenheit =float(temperatura_fahrenheit)
    temperatura_kelvin = (temperatura_fahrenheit - 32) * 5/9 + 273.15
    print("A temperatura em kelvin será:",temperatura_kelvin)

def kelvin_para_fahrenheit():
    temperatura_kelvin = input("Digite a temperatura em kelvin: ")
    temperatura_kelvin =float(temperatura_kelvin)
    temperatura_fahrenheit = (temperatura_kelvin - 273.15) * 9/5 + 32
    print("A temperatura em fahrenheit será:",temperatura_fahrenheit)

def fahrenheit_para_rankine():
    temperatura_fahrenheit = input("Digite a temperatura em fahrenheit: ")
    temperatura_fahrenheit =float(temperatura_fahrenheit)
    temperatura_rankine = (temperatura_fahrenheit + 459.67) * 5/9
    print("A temperatura em rankine será:",temperatura_rankine)

def rankine_para_fahrenheit():
    temperatura_rankine = input("Digite a temperatura em rankine: ")
    temperatura_rankine =float(temperatura_rankine)
    temperatura_fahrenheit = (temperatura_rankine * 9/5) - 459.67
    print("A temperatura em fahrenheit será:",temperatura_fahrenheit)

def kelvin_para_rankine():
    temperatura_kelvin = input("Digite a temperatura em kelvin: ")
    temperatura_kelvin =float(temperatura_kelvin)
    temperatura_rankine = temperatura_kelvin * 9/5
    print("A temperatura em rankine será:",temperatura_rankine)

def rankine_para_kelvin():
    temperatura_rankine = input("Digite a temperatura em rankine: ")
    temperatura_rankine =float(temperatura_rankine)
    temperatura_kelvin = temperatura_rankine * 5/9
    print("A temperatura em kelvin será:",temperatura_kelvin)
def menu():
    print("Escolha uma opção:")
    print("1. Fahrenheit para Celsius")
    print("2. Celsius para Fahrenheit")
    print("3. Celsius para Kelvin")
    print("4. Kelvin para Celsius")
    print("5. Celsius para Rankine")
    print("6. Rankine para Celsius")
    print("7. Fahrenheit para Kelvin")
    print("8. Kelvin para Fahrenheit")
    print("9. Fahrenheit para Rankine")
    print("10. Rankine para Fahrenheit")
    print("11. Kelvin para Rankine")
    print("12. Rankine para Kelvin")
    print("0. Sair")
    opcao = input("Digite sua opção: ")
    return opcao
def main():
    while True:
        opcao = menu()
        if opcao == "1":
            fahrenheit_para_celsius()
        elif opcao == "2":
            celsius_para_fahrenheit()
        elif opcao == "3":
            celsius_para_kelvin()
        elif opcao == "4":
            kelvin_para_celsius()
        elif opcao == "5":
            celsius_para_rankine()
        elif opcao == "6":
            rankine_para_celsius()
        elif opcao == "7":
            fahrenheit_para_kelvin()
        elif opcao == "8":
            kelvin_para_fahrenheit()
        elif opcao == "9":
            fahrenheit_para_rankine()
        elif opcao == "10":
            rankine_para_fahrenheit()
        elif opcao == "11":
            kelvin_para_rankine()
        elif opcao == "12":
            rankine_para_kelvin()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()