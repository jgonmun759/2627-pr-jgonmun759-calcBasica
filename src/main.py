def sumar(numero1: float, numero2: float) -> float:
    """
    Suma 2 números

    :param numero1: primer número
    :param numero2: segundo número

    :returns: resultado
    """
    return numero1 + numero2


def restar(numero1: float, numero2: float) -> float:
    """
        Suma 2 números
    
        :param numero1: primer número
        :param numero2: segundo número
    
        :returns: resultado
    """
    return numero1 - numero2

def multiplicar(numero1: float, numero2: float) -> float:
    """
        Multiplica 2 números
    
        :param numero1: primer número
        :param numero2: segundo número
    
        :returns: resultado
    """
    return numero1 * numero2

def dividir(numero1: float, numero2: float) -> float | str:
    """
        Divide 2 números

        :numero1: primer número
        :numero2: segundo número
    
        :returns: resultado
    """
    return (numero1 / numero2) if numero2 != 0 else "La operación no puede realizarse"

def main():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    suma = sumar(num1, num2)
    resta = restar(num1, num2)
    mult = multiplicar(num1, num2)
    div = dividir(num1, num2)

    print("\n---- RESULTADO ----")

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {mult}")
    print(f"División: {div}")

if __name__ == "__main__":
    main()