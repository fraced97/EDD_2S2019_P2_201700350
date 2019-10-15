from MenuPrincipal import ListaDE



class MenuPractica:


    #def __init__(self):


    def menuPrincipal(self):

        '''print("")
        print("")
        print("")
        print("")
        print("-------------Practica 2 EDD-----------------")
        print(""" 
                        [1] INSERTAR BLOQUE
                        [2] SELECCIONAR BLOQUE
                        [3] REPORTES
                        [0] SALIR
                        """)
        condicion = -1
        condicion2 = True;
        while(condicion2):
            condicion = int(input("Escribe alguna opcion del menu: "))
            print(""" 
                                   [1] INSERTAR BLOQUE
                                   [2] SELECCIONAR BLOQUE
                                   [3] REPORTES
                                   [0] SALIR
                                   """)
            switcher = {

                1: "ENTRO EN INSERTAR BLOQUE",
                2: " ENTRO EN SELECCIONAR BLOQUE",
                3: "ENTRO EN REPORTES",
                0: self.salir(condicion2)

            }
            p = switcher.get(condicion, "Invalid month")
            print(p)'''

        condicion = -1
        while (condicion != 0):

            print(""" 
                [1] INSERTAR BLOQUE
                [2] SELECCIONAR BLOQUE
                [3] REPORTES
                [0] SALIR
                """)
            try:
                condicion = int(input("Escribe alguna opcion del menu: " ))
            except ValueError:
                print("--------------------------------")
                print("No has ingresado un numero Entero")
                print("--------------------------------")

            if condicion==1:
                print("entro en uno")
            elif condicion==2:
                print("entro en dos")
            elif condicion==0:
                print("Entro en salir")
            else:
                print("--------------------------------")
                print("Escriba un numero entre 1-6")
                print("--------------------------------")


MenuPractica().menuPrincipal()
