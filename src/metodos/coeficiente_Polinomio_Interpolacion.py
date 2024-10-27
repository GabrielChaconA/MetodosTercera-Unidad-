import numpy as np
import math
class coeficiente_Polinomio_Interpolacion:
  def coeficiente_Polinomio_Interpolacion(self):
    x = np.array([1,2,5,10])    
    y = np.array([1,4,25,100])
    zise = len(x)
    matriz_ceros = np.zeros((zise, zise), dtype=float)
    for i in range(zise):
      for j in range(zise):
        matriz_ceros[i,j] = (x[i]**j)

    if np.linalg.det(matriz_ceros) != 0:
    # Calcular la inversa de la matriz
     A_inv = np.linalg.solve(matriz_ceros,y)
     print("Inversa de la matriz A:")
     print(A_inv)
    else:
     print("La matriz no es invertible (determinante es 0).")

  


    return A_inv