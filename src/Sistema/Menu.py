from metodos.hacia_adelante import hacia_adelante
from metodos.hacia_atras import hacia_atras
from metodos.diferencias_divididas import diferencias_divididas
from metodos.coeficiente_Polinomio_Interpolacion import coeficiente_Polinomio_Interpolacion
class Menu:
     def menu(self):
          """INSTANCIAS """
          instance_hacia_adelante = hacia_adelante()
          instance_hacia_atras = hacia_atras()
          instance_diferencia = diferencias_divididas()
          instance_coeficiente = coeficiente_Polinomio_Interpolacion()
      
          """ respuesta  =input("HACIA ATRAS(1)") """
          respuesta = "4"
          if respuesta == "1":
           instance_hacia_adelante.hacia_adelante()
          if respuesta == "2":
              instance_hacia_atras.hacia_atras()
          if respuesta == "3":
              instance_diferencia.diferencias_divididas()
          if respuesta =="4":
              instance_coeficiente.coeficiente_Polinomio_Interpolacion()
              
          return