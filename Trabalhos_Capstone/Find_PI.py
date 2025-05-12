from mpmath import mp

# Define o limite máximo de casas decimais
LIMITE_MAXIMO = 1000

def solicitar_casas_decimais():
    try:
        casas = int(input(f"Digite o número de casas decimais de PI (máx {LIMITE_MAXIMO}): "))
        if casas < 0:
            print("Número inválido. Digite um valor positivo.")
            return None
        elif casas > LIMITE_MAXIMO:
            print(f"O número é muito alto. Limitando a {LIMITE_MAXIMO} casas decimais.")
            return LIMITE_MAXIMO
        return casas
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return None

def calcular_pi(casas_decimais):
    mp.dps = casas_decimais + 2  # Compensa "3." e arredondamento
    return str(mp.pi)[:2 + casas_decimais]

def main():
    casas_decimais = solicitar_casas_decimais()
    if casas_decimais is not None:
        pi_formatado = calcular_pi(casas_decimais)
        print(f"\nPI com {casas_decimais} casas decimais:")
        print(pi_formatado)

if __name__ == "__main__":
    main()
