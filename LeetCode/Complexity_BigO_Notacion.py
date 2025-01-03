#################################  Big O notation ###############################################
#Page to calc complexity: 
#https://www.bigocalc.com/


  '''
EPP:  Es una función que denota qué tanto cambia la cantidad de operaciones segun una entrada n de items. 
Ejemplo: para una complejidad O(n), siginifica que si le meto un n de datos le va a tomar n operaciones,
si duplico n entonces se duplicará el tiempo que le tome 

n generalmente representa el número de elementos en una lista, cadena, árbol, grafo, o cualquier dato que esté procesando.
O(n) se encarga de medir el peor de los casos, por ejemplo, si quiero buscar un elemento en una lista no ordenada de n elementos 
es posible que en el peor de los casos tenga que hacer n operaciones para encontrar el número 

---------------------- Tabla de complejidad: ---------------------------------------------------------------- 
Por ejemplo, tengo un arreglo de n= 10 elementos, así se demorará el algoritmo en funcionar: 

1. 0(n!) =   10 datos => O(10!): 3628800 operaciones.
2. 0(2^n) =   10 datos => O(2^10): 1024 operaciones.
3. 0(n^2) =   10 datos => O(10^2): 100 operaciones.
4. O(n*Log_2(n)) =   10 datos => O(10*Log_2(10)): 33.21 operaciones. 
5. O(n) =   10 datos => O(10): 10 operaciones. 
6. O(log_2(n)) =   10 datos => O(Log_2(10)):  3.21 operaciones. 
7. O(1) =   10 datos => O(1): 1 operación.  


-------------------------------- Simplificación ----------------------------------------------------------
La complejidad Big O se basa en un estudio asintotico, es decir para entradas muy grandes o muy dominantes, se pueden simplificar ya que solo importa un acercamiento general del credimiento de pasos segun la cantidad de entradas:

1. O(n) + O(1) = O(n) 

2. O(3n) = O(n): no importa la pendiente de la funcion, por cada uno salen 3, ya que solo importa ver si es lineal o no.  

3. O(5n + 1 + n) = O(6n + 1) = O(6n) = O(n): DOMINANTE. 

4. O(n+m) = si n > m = O(n) y viceversa: DOMINANTE, acá el tiempo de ejecución depende de dos entradas independientes: n y m. s

5. O(n^2 + n^3) = O(n^3): DOMINANTE


 ----------------------------------- Coste operacional de acciones básicas de python ----------------------------------------------------------------

''''

# Operaciones de tiempo constante O(1) en Python ------------------------------------------------------------------------------------


# 1. Asignación
a = 1  # O(1), también O(1) en C++.
b = "Hola"  # O(1), también O(1) en C++, aunque las cadenas pueden implicar una copia profunda en algunos casos.
c = [1, 2, 3]  # O(1), en C++ depende de cómo se inicialicen los contenedores.

# 2. Acceso por índice
x = lista[5]  # O(1), en C++ también es O(1) para arreglos y vectores.
y = tupla[2]  # O(1), en C++ sería O(1) para arreglos o std::array.

# 3. Asignación por índice
lista[3] = 10  # O(1), en C++ también es O(1) para arreglos y vectores.

# 4. Acceso por clave en un diccionario
valor = diccionario['clave']  # O(1) promedio, pero puede ser O(n) en el peor caso en Python.
# En C++ (std::unordered_map), promedio O(1), pero peor caso O(n) si hay colisiones.

# 5. Inserción o actualización de una clave en un diccionario
diccionario['nueva_clave'] = 'valor'  # O(1) promedio, pero podría ser O(n) en el peor caso.
# En C++ (std::unordered_map), promedio O(1), pero peor caso O(n).

# 6. Comprobación de clave en un diccionario
existe = 'clave' in diccionario  # O(1) promedio, pero podría ser O(n) en el peor caso.
# En C++ (std::unordered_map), promedio O(1), pero peor caso O(n).

# 7. Obtener el tamaño de una lista, tupla, conjunto o diccionario
tamaño = len(lista)  # O(1), también O(1) en C++ para contenedores estándar como std::vector.
tamaño = len(diccionario)  # O(1), también O(1) en C++ para std::unordered_map o std::map.

# 8. Agregar un elemento al final de una lista
lista.append(10)  # O(1) promedio, aunque puede ser O(n) si hay un redimensionamiento interno.
# En C++, std::vector.push_back() también es O(1) promedio, pero puede ser O(n) si hay un redimensionamiento.

# 9. Eliminación del último elemento de una lista
lista.pop()  # O(1), también O(1) en C++ para std::vector.

# 10. Operaciones con conjuntos
# Agregar un elemento a un conjunto
conjunto.add(5)  # O(1) promedio, pero podría ser O(n) en el peor caso.
# En C++ (std::unordered_set), promedio O(1), pero peor caso O(n).

# Eliminar un elemento de un conjunto (si existe)
conjunto.discard(5)  # O(1) promedio, pero podría ser O(n) en el peor caso.
# En C++ (std::unordered_set), promedio O(1), pero peor caso O(n).

# Verificar si un elemento está en un conjunto
existe = 5 in conjunto  # O(1) promedio, pero podría ser O(n) en el peor caso.
# En C++ (std::unordered_set), promedio O(1), pero peor caso O(n).

# 11. Llamada a una función
resultado = mi_funcion()  # O(1) para la llamada en sí. Complejidad real depende del contenido de la función.
# En C++, también O(1) para la llamada misma.

# 12. Comparación
resultado = a == b  # O(1) para tipos primitivos, pero puede depender del tamaño de las estructuras comparadas.
# En C++, también O(1) para tipos primitivos, pero podría ser O(n) para estructuras más complejas como std::string.

resultado = a < b  # O(1) para tipos primitivos, similar a C++.

# 13. Booleanos
resultado = a and b  # O(1), también O(1) en C++.
resultado = not a    # O(1), también O(1) en C++.

# 14. Operaciones matemáticas simples
c = a + b  # O(1) para números pequeños. En Python, puede ser O(k) donde k es el número de bits en números grandes.
# En C++, es O(1) para enteros de tamaño fijo, pero podría depender del tamaño para números más grandes.

d = a * b  # O(1) para números pequeños. En Python, puede ser O(k) para enteros grandes.
# En C++, también O(1) para enteros de tamaño fijo.







# Operaciones de tiempo lineal O(n) en Python ----------------------------------------------------------------------------------------------------------------


# 1. Recorrido de una lista, tupla, conjunto o diccionario
# Recorrer una lista
for elemento in lista:  # O(n), también O(n) en C++ para std::vector.

# Recorrer una tupla
for elemento in tupla:  # O(n), también O(n) en C++ para std::array.

# Recorrer un conjunto
for elemento in conjunto:  # O(n), también O(n) en C++ para std::unordered_set.

# Recorrer las claves de un diccionario
for clave in diccionario:  # O(n), también O(n) en C++ para std::unordered_map.

# 2. Búsqueda en listas
elemento in lista  # O(n), en C++ (std::vector) también es O(n).
# Nota: En C++, si usas std::set, esto sería O(log n).

# 3. Concatenación de listas
lista_concatenada = lista1 + lista2  # O(n + m), donde n y m son los tamaños de las listas.
# En C++, concatenar dos std::vectors toma O(n + m).

# 4. Clonado o copia de listas, tuplas o conjuntos
lista_copiada = lista[:]  # O(n), también O(n) en C++ al copiar un std::vector.

tupla_copiada = tupla[:]  # O(n), también O(n) en C++ al copiar un std::array.

conjunto_copiado = conjunto.copy()  # O(n), también O(n) en C++ al copiar un std::unordered_set.

# 5. Conversión de estructuras
# Convertir una lista a un conjunto
conjunto = set(lista)  # O(n), también O(n) en C++ para construir un std::unordered_set desde un contenedor.

# Convertir un conjunto a una lista
lista = list(conjunto)  # O(n), también O(n) en C++ al convertir un std::unordered_set a un std::vector.

# Convertir un diccionario a una lista de claves
lista_claves = list(diccionario.keys())  # O(n), también O(n) en C++ al usar std::unordered_map::keys().

# 6. Comparación de listas o cadenas
lista1 == lista2  # O(n), porque compara elemento por elemento.
# En C++, también es O(n) para std::vector y std::string.

cadena1 == cadena2  # O(n), también O(n) en C++ para std::string.

# 7. Eliminación de un elemento por valor en una lista
lista.remove(valor)  # O(n), porque busca el elemento antes de eliminarlo.
# En C++, std::vector::erase() combinado con std::find es también O(n).

# 8. Buscar un valor mínimo o máximo
minimo = min(lista)  # O(n), porque recorre todos los elementos.
# En C++, std::min_element para std::vector es también O(n).

maximo = max(lista)  # O(n), en C++ std::max_element para std::vector es también O(n).

# 9. Extender una lista con otra lista
lista1.extend(lista2)  # O(n + m), donde n es el tamaño de lista1 y m el tamaño de lista2.
# En C++, std::vector::insert() para extender un vector también toma O(n + m).

# 10. Comprobación de igualdad para diccionarios
diccionario1 == diccionario2  # O(n), porque compara las claves y valores.
# En C++, comparar dos std::unordered_map es también O(n).

# 11. Suma de elementos en una lista o conjunto
suma = sum(lista)  # O(n), porque recorre todos los elementos.
# En C++, usar std::accumulate para sumar elementos en std::vector es también O(n).

suma = sum(conjunto)  # O(n), también O(n) en C++ al sumar elementos de un std::unordered_set.

# 12. Reversión de una lista
lista_reversa = lista[::-1]  # O(n), porque crea una copia en orden inverso.
# En C++, usar std::reverse para un std::vector también toma O(n).

# 13. Creación de una lista por comprensión
lista_nueva = [x * 2 for x in lista]  # O(n), porque recorre todos los elementos.
# En C++, un equivalente sería usar std::transform en un std::vector, que también es O(n).





# Operaciones de tiempo logarítmico O(log n) en Python ------------------------------------------------------------------------------------------


# 1. Operaciones con estructuras de datos ordenadas (bisect)
import bisect

# Inserción en una lista ordenada usando bisect
bisect.insort(lista_ordenada, valor)  # O(log n)
# Es así porque Python implementa búsqueda binaria para encontrar la posición correcta antes de insertar.
# En C++, std::set::insert o std::map::insert también son O(log n) porque usan árboles balanceados.

# Búsqueda de la posición donde se puede insertar un valor en una lista ordenada
pos = bisect.bisect(lista_ordenada, valor)  # O(log n)
# Python usa búsqueda binaria internamente para determinar el índice.
# En C++, std::lower_bound en std::vector o std::set también toma O(log n).

# 2. Operaciones con conjuntos o diccionarios ordenados (sortedcontainers)
from sortedcontainers import SortedSet, SortedDict

conjunto_ordenado = SortedSet([1, 2, 3, 4])
diccionario_ordenado = SortedDict({'a': 1, 'b': 2, 'c': 3})

# Búsqueda de un elemento en un conjunto ordenado
existe = 3 in conjunto_ordenado  # O(log n)
# Es así porque el conjunto ordenado usa árboles balanceados internamente para realizar la búsqueda.
# En C++, std::set::find también toma O(log n).

# Inserción en un conjunto ordenado
conjunto_ordenado.add(5)  # O(log n)
# Python utiliza un árbol balanceado para mantener el orden, lo que hace que la inserción sea logarítmica.
# En C++, std::set::insert también es O(log n).

# Eliminación de un elemento en un conjunto ordenado
conjunto_ordenado.remove(3)  # O(log n)
# Es así porque la operación de eliminación también aprovecha la estructura de árbol balanceado.
# En C++, std::set::erase también toma O(log n).

# Búsqueda de un elemento en un diccionario ordenado
valor = diccionario_ordenado['a']  # O(log n)
# Los diccionarios ordenados implementan árboles balanceados para búsquedas rápidas.
# En C++, std::map::find es O(log n).

# Inserción en un diccionario ordenado
diccionario_ordenado['d'] = 4  # O(log n)
# La inserción en un diccionario ordenado usa árboles balanceados, manteniendo el orden.
# En C++, std::map::insert también es O(log n).

# Eliminación en un diccionario ordenado
del diccionario_ordenado['a']  # O(log n)
# La eliminación aprovecha la estructura de árbol balanceado para operar en tiempo logarítmico.
# En C++, std::map::erase también es O(log n).

# 3. Búsqueda binaria en listas ordenadas
def busqueda_binaria(lista, objetivo):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio  # O(log n)
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1
# Es así porque cada iteración reduce el rango de búsqueda a la mitad.
# En C++, std::binary_search también toma O(log n).

# 4. Operaciones en heap (montículo)
import heapq
heap = [1, 3, 5, 7]
heapq.heapify(heap)  # Convierte una lista en un heap, O(n).

# Inserción en un heap
heapq.heappush(heap, 4)  # O(log n)
# Es así porque Python utiliza un árbol binario implícito para organizar el heap.
# En C++, std::priority_queue::push también es O(log n).

# Eliminación del elemento más pequeño de un heap
minimo = heapq.heappop(heap)  # O(log n)
# Python reorganiza el heap después de eliminar el elemento mínimo, lo que toma tiempo logarítmico.
# En C++, std::priority_queue::pop también es O(log n).

# 5. División recursiva
# Un ejemplo clásico es el cálculo de potencias usando división y conquista
def potencia(base, exponente):
    if exponente == 0:
        return 1
    mitad = potencia(base, exponente // 2)
    return mitad * mitad if exponente % 2 == 0 else mitad * mitad * base
# O(log n)
# Es así porque el algoritmo divide el problema en subproblemas más pequeños, reduciendo el tamaño a la mitad en cada paso.
# En C++, la exponenciación rápida implementada manualmente o con std::pow tiene la misma complejidad O(log n).



# Operaciones de tiempo O(n log n) en Python -------------------------------------------------------------------------------------

# 1. Ordenar una lista
lista = [3, 1, 4, 1, 5, 9]
lista.sort()  # O(n log n)
# Es O(n log n) porque Python usa Timsort, que divide la lista en sublistas (O(log n)) 
# y luego combina las sublistas ordenadas (O(n) por nivel).
# En C++, std::sort también es O(n log n), utilizando introsort.

# 2. Ordenar una copia de una lista
lista_ordenada = sorted(lista)  # O(n log n)
# Igual que lista.sort(), sorted() usa Timsort y toma O(n log n) en promedio.
# En C++, std::sort también es O(n log n) para ordenar una copia de un contenedor.

# 3. Construir un SortedSet
from sortedcontainers import SortedSet
conjunto_ordenado = SortedSet([3, 1, 4, 1, 5, 9])  # O(n log n)
# Es O(n log n) porque cada elemento insertado en el SortedSet toma O(log n),
# y hay n elementos en total.
# En C++, construir un std::set desde un contenedor también toma O(n log n).

# 4. Construir un SortedDict
from sortedcontainers import SortedDict
diccionario_ordenado = SortedDict({'a': 1, 'c': 3, 'b': 2})  # O(n log n)
# Es O(n log n) porque cada clave-valor insertado en el SortedDict toma O(log n).
# En C++, construir un std::map desde un contenedor también toma O(n log n).

# 5. Heapify (construcción de un heap)
import heapq
heap = [3, 1, 4, 1, 5, 9]
heapq.heapify(heap)  # O(n)
# Es O(n) porque el proceso de reorganización de un heap completo está optimizado.
# Sin embargo, las operaciones posteriores (como insertar n elementos en un heap) pueden tomar O(n log n).
# En C++, std::make_heap para construir un heap también toma O(n).

# Insertar n elementos en un heap
for valor in lista:
    heapq.heappush(heap, valor)  # O(n log n)
# Es O(n log n) porque cada inserción toma O(log n), y hay n elementos.
# En C++, insertar elementos en std::priority_queue toma un tiempo similar.

# 6. Mezclar dos listas ordenadas
import heapq
lista1 = [1, 3, 5]
lista2 = [2, 4, 6]
lista_mezclada = list(heapq.merge(lista1, lista2))  # O(n log n), donde n es la suma de los tamaños de las listas.
# Es O(n log n) porque heapq.merge combina listas usando un heap.
# En C++, mezclar contenedores ordenados manualmente puede tomar O(n log n) dependiendo de la implementación.

# 7. Algoritmos de ordenación por comparación
# Implementar un merge sort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    izquierda = merge_sort(lista[:mid])
    derecha = merge_sort(lista[mid:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    while izquierda and derecha:
        if izquierda[0] < derecha[0]:
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))
    resultado.extend(izquierda or derecha)
    return resultado

ordenada = merge_sort([3, 1, 4, 1, 5, 9])  # O(n log n)
# Es O(n log n) porque divide la lista en sublistas (O(log n)) y luego fusiona los resultados (O(n) por nivel).
# En C++, std::stable_sort también toma O(n log n) y garantiza estabilidad.

# 8. Operaciones en estructuras ordenadas con múltiples elementos
# Insertar múltiples elementos en un SortedSet
from sortedcontainers import SortedSet
sorted_set = SortedSet()
for valor in [3, 1, 4, 1, 5, 9]:
    sorted_set.add(valor)  # O(n log n)
# Es O(n log n) porque cada inserción toma O(log n), y hay n elementos.
# En C++, insertar múltiples elementos en std::set también toma O(n log n).


