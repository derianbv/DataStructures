########## Hi there ######################s
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead."""
        #Can you come up with an algorithm that runs in O(m + n) time?

        #Uso punteros para ir desde los últimos numeros validos hasta el inicio 
        p1 = m-1 #Puntero desde el largo-1:ultima posicion de nums1
        p2 = n-1 #Puntero desde el largo-1:ultima posicion de nums2
        pf = (n+m)-1 #Puntero desde el largo-1:ultima posicion del largo de nums1+nums2 = len(nums1). 
        
        if p1 < 0: #Si el arrelo nums1 es vacio, entonces voy a copiar dentro de los primeros n spaceholders de nums1 (nums[:n]) Ej: nums1 = [0,0,0,...,n] los n valores de nums2 (Ej: nums2 = [1,3,4,5,...,n]
            nums1[:n] = nums2
            return # para parar el codigo

        
        while p1 >= 0 and p2 >= 0: #Mientras que los punteros
            
            if nums1[p1] >= nums2[p2]: #si el numero del arreglo largo es más grande que el del numero pequeño entonces lo pongo al final y muevo el puntero del numero replazado
                nums1[pf] = nums1[p1]
                p1 -= 1 
                pf -= 1 #También muevo el puntero del final del arreglo para que el otro siguiente valor mayor sea puesto ahí
            else: 
                nums1[pf] = nums2[p2]
                p2-= 1 
                pf -= 1

        if  p1 < 0: #si ya termine con el arreglo grande, me quedan cosas en el nums2 que voy a agregar igualando unos intervalos
            nums1[:pf+1] = nums2[:p2+1]
        
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

sol = Solution()
sol.merge(nums1, m, nums2, n)
print(nums1)  

