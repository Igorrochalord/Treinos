def soma ():
    num1 = int(input("digite um numero inteiro: "))
    num2 = int(input("digite outro numero inteiro: "))
    resultado = num1 + num2
    print(f"A soma de {num1} e {num2} é {resultado}.")
    return resultado
def subtracao ():
    num1 = int(input("digite um numero inteiro: "))
    num2 = int(input("digite outro numero inteiro: "))
    resultado = num1 - num2
    print(f"A subtração de {num1} e {num2} é {resultado}.")
    return resultado
def multiplicacao ():
    num1 = int(input("digite um numero inteiro: "))
    num2 = int(input("digite outro numero inteiro: "))
    resultado = num1 * num2
    print(f"A multiplicação de {num1} e {num2} é {resultado}.")
    return resultado
def divisao ():
    num1 = int(input("digite um numero inteiro: "))
    num2 = int(input("digite outro numero inteiro: "))
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
        return None
    resultado = num1 / num2
    print(f"A divisão de {num1} e {num2} é {resultado}.")
    return resultado
def potencia ():
    num1 = int(input("digite um numero inteiro: "))
    num2 = int(input("digite outro numero inteiro: "))
    resultado = num1 ** num2
    print(f"A potencia de {num1} e {num2} é {resultado}.")
    return resultado
def raiz ():
    num1 = int(input("digite um numero inteiro: "))
    if num1 < 0:
        print("Erro: Raiz quadrada de número negativo não é permitida.")
        return None
    resultado = num1 ** 0.5
    print(f"A raiz quadrada de {num1} é {resultado}.")
    return resultado
def menu():
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz quadrada")
    print("7. Sair")
    
    while True:
        try:
            opcao = int(input("Digite o número da operação desejada: "))
            if opcao in range(1, 8):
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    
    return opcao
def calculadora():
    while True:
        opcao = menu()
        
        if opcao == 1:
            soma()
        elif opcao == 2:
            subtracao()
        elif opcao == 3:
            multiplicacao()
        elif opcao == 4:
            divisao()
        elif opcao == 5:
            potencia()
        elif opcao == 6:
            raiz()
        elif opcao == 7:
            print("Saindo da calculadora. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")
if __name__ == "__main__":
    calculadora()
    