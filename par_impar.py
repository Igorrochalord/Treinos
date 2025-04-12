def calculo ():
    try:
        numero =(int(input("Coloque um numero inteiro: ")))
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
    except TypeError:
        print("Erro de tipo: insira um número inteiro.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        print("Obrigado por usar o programa.")
        return numero
if __name__ == "__main__":
    calculo()