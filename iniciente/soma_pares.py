def soma_pares():
    """
    Função que soma números inteiros pares.
    """
    soma = 0
    while True:
        try:
            num = int(input("Digite um número inteiro (ou -1 para sair): "))
            if num == -1:
                break
            if num % 2 == 0:
                soma += num
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    print(f"A soma dos números pares digitados é: {soma}")
if __name__ == "__main__":
    soma_pares()