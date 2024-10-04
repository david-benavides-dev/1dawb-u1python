def comprobar_entero(entero: str)-> bool:
    if entero.isdigit():
        return True
    else:
        return False

def dame_entero():
    numero = input("Introduce un número entero: ")
    while not comprobar_entero(numero):
        numero = input("Debe ser un número entero: ")
    else:
        return numero


def main():
    numero = dame_entero()
    print (f"Tu número es: {numero}")

if __name__ == "__main__":
    main()