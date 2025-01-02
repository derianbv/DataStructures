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

6. 
''''