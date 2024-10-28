import numpy as np
import math
class Interpolacion_Lagrange:
    def Interpolacion_Lagrange(self):
        x = np.array([1,2,5,10])    
        L = np.array([]) 
        y = np.array([1,4,25,100 ])
        v_dado = 7
        #s= np.append(s, 1)
        i=0
        for i in range(len(x)):
         L = np.append(L,self.ecuacion(x,v_dado,i,y))
         
         i+=1
        print(L)
        final = np.sum(L)
        print(final)

        return
    def ecuacion(self,x,v_dado, index,y):
      j ,valor= index, 1
      i=0
      for i in range(len(x)):
       if i != j:
        valor = ((v_dado-x[i])/(x[j]-x[i]))*valor
        print(valor)
       i+=1


      return valor*y[index]