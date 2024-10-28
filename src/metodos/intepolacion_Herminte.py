
import numpy as np
import math
class intepolacion_Herminte:
    def intepolacion_Herminte(self):
        x = np.array([1.3,1.6,1.9])    
        y = np.array([0.6201,0.4554,0.2818])
        y_= np.array([-0.5220,-0.5699,-0.5812])
        print("f(x)= ESCRIBA VALOR")
        x_Valor = 11 
        print("Valor ingresado fue {}".format(x_Valor))
        x = self.crear_z(x)
        y = self.crear_z(y)
        y_ = self.crear_y_(y_)


        self.ejecutar(self.ecuation(y,x,y_),self.cadena(x,x_Valor))




        return
    

    def crear_y_(self, y_):
       new_y_ = np.array([])
       j=0
       for i in range(2*len(y_)):
          if i % 2== 0:
            new_y_= np.append(new_y_, y_[j] )
            j+=1

       return new_y_
    def crear_z(self, y_):

       j=0
       new_y_ = np.array([])
       new_y_= np.append(new_y_, y_[j] )
       
       
       for i in range(2*(len(y_))-1):
          new_y_= np.append(new_y_, y_[j] )
          if i % 2== 0 :
           j+=1
          i+=1
       print(new_y_)
          
       
       return new_y_
    
    def ecuation(self, y,x,y_):
       contador = len(y)-1
       contador2 = len(y)-1
       condicion,j,i,k = 0,len(y_)-1,0,1
       flag = True
       primer_fila = np.array([])

       while(True):
       # print("contado: {} len(y)-1 {}".format(contador,len(y)-k))
       
        primer_fila = np.append(primer_fila,y[i]) if contador == len(y)-1 else primer_fila
        if contador == len(y)-1:
          # print("Primer Fila {}".format(primer_fila))
          
           i+=1

        if y[contador] == y[contador-1] and j>-1:
           #print("Se agrego valor de y_ {}".format(y_[j]))
           y[contador] = y_[j]
           j-=1
        else:
         #print("{}-{}/{}-{} = {} ".format(y[contador],y[contador-1], x[contador],x[contador-2],(y[contador]-y[contador-1])/(x[contador]-x[contador-2])))
         y[contador] = (y[contador]-y[contador-1])/(x[contador]-x[contador-2])
        # print("y = {}".format(y))
        
       
       
        contador= contador -1
        contador2-=1
       
        contador = contador if contador > condicion else len(y)-1
        if len(primer_fila) == len(y):
           print("primer_fila")
           print(primer_fila)
           break
       
       
        
        
       return primer_fila 
    
    def cadena(self,x,x_valor):
       i =0
       s = np.array([])
       s= np.append(s, 1)
       for j in range (len(x)-1):
         s = np.append(s,s[i]*(x_valor-x[i]))
         i+=1
       print("s")
       print(s)




       return s
       
    
    
    def ejecutar(self,s,f):
       print(s)
       print(f)
       
       resultado = s*f
       print(resultado)
       resultado = sum(resultado)
       
       
       print(resultado)
       return resultado