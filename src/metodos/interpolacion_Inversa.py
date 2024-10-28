import numpy as np
import math
class Interpolacion_Inversa:
    def Interpolacion_Inversa(self):
      x = np.array([1,2,3,4,5])    
      y = np.array([1,0.5,0.3333,0.25,0.2])
      
      valor_dado = 10/3
      Fx = "1/x"
      mi_funcion = eval("lambda x: " + Fx)

      resultado = mi_funcion(valor_dado)
      index = self.valores_proximos(y,resultado)
      x1 = np.array([x[index-1],x[index],x[index+1]])
      y1 = np.array([y[index-1],y[index],y[index+1]])
      print(x1)
      print(y1)
      fx= self.coeficiente_Polinomio_Interpolacion(x1,y1)
      print(fx)
      print(resultado)
      
      chicharronera_P = (-(fx[1]) + np.sqrt(fx[1]**2 - 4 * fx[2] * (fx[0] - resultado))) / (2 * fx[2])
      chicharronera_N = (-(fx[1]) - np.sqrt(fx[1]**2 - 4 * fx[2] * (fx[0] - resultado))) / (2 * fx[2])
      print("-{}+ sqrt {}^2 - 4{} {}-{} / 2{}".format(fx[1],fx[1],fx[2],fx[0],resultado,fx[2]))
      print("X1 = {} x2= {}".format(chicharronera_P, chicharronera_N))

     
      


      return chicharronera_P
    
    def coeficiente_Polinomio_Interpolacion(self,x,y):
    
     zise = len(x)
     matriz_ceros = np.zeros((zise, zise), dtype=float)
     for i in range(zise):
      for j in range(zise):
        matriz_ceros[i,j] = (x[i]**j)

     if np.linalg.det(matriz_ceros) != 0:
     # Calcular la inversa de la matriz
      A_inv = np.linalg.solve(matriz_ceros,y)
     else:
      print("La matriz no es invertible (determinante es 0).")

     return A_inv
    

    
    def valores_proximos(self, y,resultado):
     
      menor =  abs(resultado-y[0])

      for i in range(len(y)):
        if abs(resultado-y[i])< menor :
          menor =  abs(resultado-y[i])
          j = i

      return j