def media_notas():
    """
    Função que calcula a média de notas de um aluno.
    """
    # Inicializa a variável para armazenar a soma das notas
    soma = 0
    # Inicializa a variável para contar o número de notas
    contador = 0

    while True:
        # Solicita ao usuário que insira uma nota
        nota = input("Digite a nota do aluno (ou 'sair' para encerrar): ")

        # Verifica se o usuário deseja encerrar o loop
        if nota.lower() == 'sair':
            break

        try:
            # Converte a entrada para float e adiciona à soma
            soma += float(nota)
            contador += 1
        except ValueError:
            print("Entrada inválida. Por favor, insira um número ou 'sair'.")

    # Calcula a média se houver notas válidas
    if contador > 0:
        media = soma / contador
        print(f"A média das notas é: {media:.2f}")
    else:
        print("Nenhuma nota válida foi inserida.")
if __name__ == "__main__":
    media_notas()
