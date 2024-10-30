from metodos.hacia_adelante import hacia_adelante
from metodos.hacia_atras import hacia_atras
from metodos.diferencias_divididas import diferencias_divididas
from metodos.coeficiente_Polinomio_Interpolacion import coeficiente_Polinomio_Interpolacion
from metodos.regresión import regresión
from metodos.interpolacion_Inversa import Interpolacion_Inversa
from metodos.intepolacion_Herminte import intepolacion_Herminte
from metodos.Interpolacion_Lagrange import Interpolacion_Lagrange
from metodos.FuncionLineal import FuncionLineal
from metodos.Interpolacion_Segmentada import Interpolacion_Segmentada
from metodos.regresion_polinomial import regresion_polinomial
from metodos.regresion_multiple import regresion_multiple
class Menu:
     def menu(self):
          """INSTANCIAS """
          instance_hacia_adelante = hacia_adelante()
          instance_hacia_atras = hacia_atras()
          instance_diferencia = diferencias_divididas()
          instance_coeficiente = coeficiente_Polinomio_Interpolacion()
          instance_regresion = regresión()
          instance_Interpolacion_Lagrange = Interpolacion_Lagrange()
          instance_Interpolacion_Inversa= Interpolacion_Inversa()
          instance_Interpolacion_Segmentada= Interpolacion_Segmentada()
          instance_intepolacion_Herminte = intepolacion_Herminte()
          instance_FuncionLineal =FuncionLineal()
          instance_regresion_polinomial = regresion_polinomial()
          instance_regresion_multuple = regresion_multiple()
          """ respuesta  =input("HACIA ATRAS(1)") """
          respuesta = "12"
          if respuesta == "1":
           instance_hacia_adelante.hacia_adelante()
          if respuesta == "2":
              instance_hacia_atras.hacia_atras()
          if respuesta == "3":
              instance_diferencia.diferencias_divididas()
          if respuesta =="4":
              instance_coeficiente.coeficiente_Polinomio_Interpolacion()
          if respuesta =="5":
              instance_regresion.regresion()
          if respuesta =="6":
              instance_Interpolacion_Inversa.Interpolacion_Inversa()
          if respuesta =="7":
              instance_Interpolacion_Segmentada.Interpolacion_Segmentada()
          if respuesta =="8":
              instance_Interpolacion_Lagrange.Interpolacion_Lagrange()
          if respuesta =="9":
             instance_intepolacion_Herminte.intepolacion_Herminte()
          if respuesta =="10":
              instance_FuncionLineal.FuncionLineal()
          if respuesta == "11":
              instance_regresion_polinomial.regresion_polinomial()
          if respuesta == "12":
              instance_regresion_multuple.regresion_multiple()
                

             
              
          return