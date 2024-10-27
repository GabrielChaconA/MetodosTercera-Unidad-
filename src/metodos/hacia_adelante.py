import numpy as np
import math
class hacia_adelante:
    def hacia_adelante(self):
        x = np.array([6,8,10,12])    
        y = np.array([9,25,55,105])

        if self.equidistance(x):
         
         print("f(x)= ESCRIBA VALOR")
         x_Valor = 11 
         equidistance = x[1]-x[0]
         print("Valor ingresado fue {}".format(x_Valor))
         self.ejecutar(self.factorial(x_Valor,x,equidistance),self.ecuation(y))
        else:
           print("No es equidistante")
        



        return
    """ Realiza  """
    def ecuation(self, y):
     contador = 0
     contador2 = 0
     condicion = len(y)-1
     flag = True
     primer_fila = np.array([])
     while(flag):
       print(contador)
       primer_fila = np.append(primer_fila,y[0]) if contador == 0 else primer_fila

       y[contador] = y[contador+1]-y[contador]
       
       contador+=1
       contador2+=1
       condicion = len(y)-1 if contador==condicion else condicion
       contador = contador if contador < condicion else 0
       if len(primer_fila) == len(y):
          
          flag = False
        
     return primer_fila 
    
    def factorial(self,x_Valor,x,equidistancia):
      i, factorial,k = 1 ,1,0
      s = np.array([])
      s= np.append(s, 1)
      k = (x_Valor-x[0])/equidistancia
   
    

      for s1 in x:
         
         anterior = s[i-1]* factorial
         factorial = math.factorial(i) 
         s = np.append(s, (((anterior)*(k-(i-1)))/factorial))
     
         i+=1
        
         if i == len(x):
            break
         
       

      return s
    
    def ejecutar(self,s,f):
       print(s)
       print(f)
       
       resultado = s*f
       print(resultado)
       resultado = sum(resultado)
       
       
       print(resultado)
       return resultado
    
    def equidistance(self, ecuacion):
       equidistance = np.diff(ecuacion)
       for equisitance1  in equidistance:
          i =0
          flag = True
          if equidistance[i] != equidistance[i+1] and i<len(equidistance):
             flag == False
             print("no son equidistantes ")
          i+=1
            
        
             
       
       return flag
    