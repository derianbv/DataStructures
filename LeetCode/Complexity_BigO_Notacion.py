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

# Operaciones de tiempo constante O(1) en Python
# Incluye notas sobre si la complejidad podría cambiar en otros lenguajes como C++.

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


