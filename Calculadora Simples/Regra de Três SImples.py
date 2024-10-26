def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um número válido.")

def calcular_resultado(p1, p2, p3):
    """Calcula o resultado da proporção."""
    return (p2 * p3) / p1

def main():
    p1 = obter_valor('Digite o primeiro valor: ')
    p2 = obter_valor('Digite o segundo valor: ')
    p3 = obter_valor('Digite o terceiro valor: ')
    print('O quarto valor será o X.')

    resultado = calcular_resultado(p1, p2, p3)
    print(f'\nO valor {p1} está para {p2}, assim como {p3} está para X = {resultado}\n')

if __name__ == "__main__":
    main()