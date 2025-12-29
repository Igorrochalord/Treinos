def temperatura():
    print("Concersao de temperatura")
    print("Escolha uma opção:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    print("4. Kelvin para Celsius")
    print("5. Fahrenheit para Kelvin")
    print("6. Kelvin para Fahrenheit")
    print("7. Sair")
    while True:
        try:
            opcao = int(input("Digite o numero do menu: "))
            if opcao in range(1, 8):
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    if opcao == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C é igual a {fahrenheit}°F")
    elif opcao == 2:    
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F é igual a {celsius}°C")
    elif opcao == 3:
        celsius = float(input("Digite a temperatura em Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius}°C é igual a {kelvin}K")
    elif opcao == 4:   
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        celsius = kelvin - 273.15
        print(f"{kelvin}K é igual a {celsius}°C")
    elif opcao == 5:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        print(f"{fahrenheit}°F é igual a {kelvin}K")
    elif opcao == 6:
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        print(f"{kelvin}K é igual a {fahrenheit}°F")
    elif opcao == 7:
        print("Saindo do programa...")
        return
    else:
        print("Opção inválida! Tente novamente.")
        return
if __name__ == "__main__":
    temperatura()