def fatores_primos(n):
    fatores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            fatores.append(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                fatores.append(n)
                break
    return fatores

def main():
    try:
        numero = int(input("Digite um número inteiro maior que 1: "))
        if numero <= 1:
            print("Digite um número maior que 1.")
            return
        fatores = fatores_primos(numero)
        print(f"Fatores primos de {numero}: {fatores}")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

if __name__ == "__main__":
    main()
