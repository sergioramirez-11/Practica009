class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

#Funcion para agregar un nodo al final de la lista
def agregar_nodo (cabeza, valor):
    nuevo_nodo = Nodo(valor)

    if cabeza is None: #Si la lista esta vacia
        cabeza = nuevo_nodo
    else:
        actual = cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente #Avanzamos en la lista
        actual.siguiente = nuevo_nodo

    return cabeza

#Funcion para imprimir la lista
def imprimir_lista(cabeza):
    actual = cabeza
    while actual is not None:
        print(actual.dato, end=" ")
        actual = actual.siguiente
    print()

#Funcion para borrar la lista
def borrar_lista(cabeza):
    while cabeza is not None:
        siguiente = cabeza.siguiente
        print(f"Elemento (cabeza.dato) borrado")
        cabeza = siguiente

#Funcion principal
if __name__ == "__main__":
    cabeza = None #Inicializamos la cabeza de la lista como None

    tamano_lista = int(input("Ingrese la cantidad de elementos que desea agregar a la lista: "))

    for i in range(tamano_lista):
        valor = int(input(f"Ingrese dato {i + 1}: "))
        cabeza = agregar_nodo(cabeza, valor)



    print("Imprimiendo lista de numeros: ")
    imprimir_lista(cabeza)

    borrar_lista(cabeza)

    print("Imprimiendo lista de numeros despues de borrar: ")
    imprimir_lista(cabeza)
