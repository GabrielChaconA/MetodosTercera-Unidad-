import numpy as np
class regresion_polinomial:
    def regresion_polinomial(self):
        x_tala = np.array([0,1,2,3,4,5])  
        e = np.array([])  
        y_tabla = np.array([2.1,7.7,13.6,27.2,40.9,61.1])
        n = len(x_tala)
    
        x2 = x_tala**2
        x3 = x_tala**3
        x4 = x_tala**4
        xy = x_tala*y_tabla
        x2y = x2*y_tabla
        x = round(np.sum(x_tala),4)
        y = round(np.sum(y_tabla),4)
        x2 = round(np.sum(x2),4)
        x3 = round(np.sum(x3),4)
        x4 = round(np.sum(x4),4)
        xy = round(np.sum(xy),4)
        x2y = round(np.sum(x2y),4)
        print("x: {} y: {} x^2: {} x^3:{} x^4:{} xy:{} x^2y: {} ".format(x,y,x2,x3,x4,xy,x2y))


        matriz = np.array([[n,x,x2],[x,x2,x3],[x2,x3,x4]])
        independientes = np.array([y,xy,x2y])
        valores = np.linalg.solve(matriz, independientes)
        print("a0 ={} a1 = {} a2 = {}".format(valores[0], valores[1],valores[2]))
        for i in range(n): 
            y =round( valores[0] + valores[1]*x_tala[i] + valores[2]*x_tala[i]**2,4)
            e = np.append(e,(y_tabla[i]-y)**2)
            i+=1
        print("errro",np.sum(e))
        print("{} + {}X +{}X^2 -{}".format(round(valores[0],4),round( valores[1],4),round(valores[2],4),np.sum(e)))
        print("Da un valor: ")
        v_dado = 1
        print("Valor dado fue :{}" .format(v_dado))
        y =round( valores[0] + valores[1]*v_dado + valores[2]*v_dado**2,4)
        print(y)


        
        


        return