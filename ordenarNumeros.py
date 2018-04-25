def ordenarNumeros(lista):
    if len(lista)>1:
        mid = len(lista)//2
        lefthalf = lista[:mid]
        righthalf = lista[mid:]
        ordenarNumeros(lefthalf)
        ordenarNumeros(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lista[k] = lefthalf[i]
                i = i + 1
            else:
                lista[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            lista[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            lista[k] = righthalf[j]
            j = j + 1
            k = k + 1
    
def crearLista(nums):
    i = 0
    lista = []
    while i < nums:
        numero = int(input("Ingrese numero: "))
        lista.append(numero)
        i = i + 1
    return lista

def main(nums):
    lista = crearLista(nums)
    ordenarNumeros(lista)
    print(lista)
numeros = int(input("Ingrese cantidad de numeros por ordenar: "))
main(numeros)
