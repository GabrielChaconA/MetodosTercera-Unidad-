import numpy as np
import math
class diferencias_divididas:
    def diferencias_divididas(self):
        x = np.array([6,8,10,12])    
        y = np.array([9,25,55,105])
        print("f(x)= ESCRIBA VALOR")
        x_Valor = 11 
        print("Valor ingresado fue {}".format(x_Valor))
        self.ejecutar(self.ecuation(y,x),self.cadena(x,x_Valor))

       
        



        return
    """ Realiza  """
    def ecuation(self, y,x):
     y = np.array(y, dtype=float)
     x = np.array(x, dtype=float)
     contador , i= 0, 1
     condicion = len(y)-1
     
     primer_fila = np.array([])
     while(True):
       
       primer_fila = np.append(primer_fila,y[0]) if contador == 0 else primer_fila
       

       if len(primer_fila) == len(y):
          break

       y[contador] = (y[contador+1]-y[contador])/(x[contador+i]-x[contador])
      
       contador+=1   
       condicion = len(y)-i if contador!=condicion else condicion

       #contador = contador if contador < condicion else 0
       if contador < condicion:
          contador = contador
       else:
          contador = 0
          i+=1

       
       
       
        
     return primer_fila 
    
    def cadena(self,x,x_valor):
       i =0
       s = np.array([])
       s= np.append(s, 1)
       for j in range (len(x)-1):
         s = np.append(s,s[i]*(x_valor-x[i]))
         i+=1




       return s
       
    
    
    def ejecutar(self,s,f):
       print(s)
       print(f)
       
       resultado = s*f
       print(resultado)
       resultado = sum(resultado)
       
       
       print(resultado)
       return resultado
    
    
            
        
             
       
     
    