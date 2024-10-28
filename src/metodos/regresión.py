import numpy as np
import math
class regresión:
    def regresion(self):
     x = np.array([1,2,3,4,5,6,7])    
     y = np.array([0.5,2.5,2,4,3.5,6,5.5])
     e, y_Final,sum_x_y,sum_x_,sum_y_=0,0,0,0,0
     sum_x = np.sum(x)
     sum_y = np.sum(y)
     xy = x*y
     sum_xy = np.sum(xy)
     x2 = [v**2 for v in x ]
     sum_x2 = np.sum(x2)
     a1 = ((len(x)*sum_xy)-(sum_x*sum_y))/((len(x)*sum_x2)-(sum_x)**2) #47/56
     a0 = ((sum_y/len(x))-((a1)*(sum_x/len(x)))) #1/14
     print("ai={}".format(a1))
     print("a0={}".format(a0))
     for i in range(len(x)):
      e = round((((y[i]-a0-(a1*x[i]))**2)+e),4)
      print("{}-{}-{}{} ={}".format(y[i],a0,a1,x[i],e))

     print("y ={}+ {}x +- {}".format(a0,a1,e))
     valor_y= a0+(a1*len(x))-e

     for i in range(len(x)):
       sum_x_y = ((x[i]-(x[i]/len(x)))*(y[i]-(y[i]/len(x))))+sum_x_y
       sum_x_ = (x[i]-(x[i]/len(x)))**2+ sum_x_
       sum_y_ = (y[i]-(y[i]/len(x)))**2 + sum_y_

     print("R = {}".format((sum_x_y/(np.sqrt(sum_x_)*np.sqrt(sum_y_)))))
       
     #sum = (a0+ a1*valor_dado-y[i])**2




     return