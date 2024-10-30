
import numpy as np
class regresion_multiple:
    def regresion_multiple(self):# Variables iniciales
        x_tabla = np.array([0, 1, 2, 3, 4, 5])
        y_tabla = np.array([6, 7, 3, 5, 2, 1])
        z_tabla = np.array([-16.5, -1.5, 71.5, 158.5, 303.5, 478.5])
        array = []
        #v_dado = 0
        n = len(x_tabla)
        
        x_sum = np.sum(x_tabla)
        y_sum = np.sum(y_tabla)
        z_sum = np.sum(z_tabla)
        print("x:{} y:{} ".format(x_sum,y_sum))

        # Configuración de la matriz y variables de control
        matriz = [[0] * 3 for _ in range(3)]  # Matriz 3x3 llena de ceros
        c_variable = 2  # Número de variables a utilizar en la matriz
   

        # Crear el primer fila
        f1 = ([[n], [y_tabla], [x_tabla]])
        z_f = [[0] * 1 for _ in range(3)]

        print(f1)
        flag = True


        # Ciclo principal de ajuste de la matriz
        while flag:
            for i in range(c_variable+1):
                z_f[i] = np.sum( self.elevar(z_tabla, f1[i][0], 1))

                print(i)
                for j in range(c_variable+1):
                    if i == 0 and j != 0:
                        matriz[0][j] = np.sum(np.array(f1[j]))
                    elif j == 0 and i != 0:
                        matriz[i][0] = np.sum(np.array(f1[i]))
                    else:
                        # Calcular y asignar en función de la relación entre elementos de la matriz
                        if np.array_equal(matriz[1][j], matriz[i][1]):
                            matriz[i][j] =np.sum( self.elevar(array, f1[j][0], 2))
                        else:
                            matriz[i][j] = np.sum(self.elevar(f1[j][0], f1[i][0], 1))

                # Condición para salir del ciclo
                if i == c_variable:
                    z_f[0] = np.sum(z_tabla)
                    matriz[0][0]= len(x_tabla)
                    for i in range(len(matriz)):
                        for j in range (len(matriz)):
                         print("[{}]".format(matriz[i][j]), end='')
                        print()
                    print(np.array(z_f))
                    x = np.linalg.solve(matriz, np.array(z_f))
                    print("({}) + ({})x +({})".format(x[0],x[1],x[2]))
                    # y = x[0]+(x[1]*v_dado) +x[2]
                    #print(y)
                    
                    flag = False

                # Imprimir matriz para ver la progresión en cada iteración
                

        return matriz
    

    def elevar(self,x,y,n):
        fx, fy = False, False
        x = np.array(x)
        y = np.array(y)
        R = 0
       ## corregir condiciones y queda 
        if   x.size !=0  :
            x_= x**n
            
            R =np.sum(x_)
            
            
            fx = True 
        if   y.size != 0 :
            
            y_ = y**n
          
            R = np.sum(y_)
            
          
            fy = True
        if fx and fy:
            xy = x*y
            
            R = np.sum(xy)
            print("x = {} y ={} xy = {}".format(x,y,R))

       


        return R

