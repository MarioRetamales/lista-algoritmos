peso = float(input("Digite o peso da pessoa (kg): "))
altura = float(input("Digite a altura da pessoa (m): "))
imc = peso / (altura ** 2)
print(f"O IMC da pessoa é {imc:.2f}.")
