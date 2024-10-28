import numpy as np
class FuncionLineal:
    def FuncionLineal(self):
        x = np.array([1,2,5,10])    
        y = np.array([1,4,25,100 ])
        v_dado = 11
        R = y[0]+ ((y[0]-y[1])/(x[0]-x[1]))*(v_dado-x[0])
        print(R)







        return R