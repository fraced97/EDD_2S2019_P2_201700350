from MenuPrincipal import LeerArchivo
import csv
import json
import hashlib

class MenuPractica:


    #def __init__(self):
    indiceGlobalLista = 0
    #auxLeerArchivo = LeerArchivo

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
                archivo = input("INGRESA EL NOMBRE DEL ARCHIVO CSV: ")
                auxArchivo = LeerArchivo.generarData(archivo)
                #print(str(auxArchivo)+"QUE PEDOOOOOOO")
                LeerArchivo.crearArbol(auxArchivo)
            elif condicion==2:
                listaUsuario = LeerArchivo.obtenerLista()
                condicion2 = -1
                indiceLista = 0
                while (condicion2 != 0):
                    if (listaUsuario.primero != None):
                        print("<<<" + listaUsuario.obtenerValor(indiceLista) + ">>>")

                        print(""" 
                                                                 [1] Mover hacia la derecha
                                                                 [2] Mover hacia la izquierda
                                                                 [0] Salir

                                                                                """)
                        try:
                            condicion2 = int(input("Escribe alguna opcion del menu: "))
                        except ValueError:
                            print("--------------------------------")
                            print("No has ingresado un numero Entero")
                            print("--------------------------------")

                        if condicion2 == 1:
                            indiceLista = indiceLista + 1
                            print("<<<" + listaUsuario.obtenerValor(indiceLista) + ">>>")
                        elif condicion2 == 2:
                            if (indiceLista > 0):
                                indiceLista = indiceLista - 1
                                print("<<<" + listaUsuario.obtenerValor(indiceLista) + ">>>")

                        elif condicion2 == 0:
                            self.indiceGlobalLista = indiceLista
                            print("Entro en salir")
                        else:
                            print("--------------------------------")
                            print("Escriba un numero entre 1-3")
                            print("--------------------------------")
                    else:
                        print("Aun no hay nada en la Lista")
                        break
            elif condicion ==3:
                condicion2 = -1
                while (condicion2 != 0):

                    print(""" 
                                [1] Reporte BlockChain
                                [2] Reporte Arbol
                                [3] PreOrden
                                [4] Inorden
                                [5] PosOrden
                                [0] SALIR
                                """)
                    try:
                        condicion2 = int(input("Escribe alguna opcion del menu: "))
                    except ValueError:
                        print("--------------------------------")
                        print("No has ingresado un numero Entero")
                        print("--------------------------------")

                    if condicion2 == 1:
                        print("entro en uno")
                    elif condicion2 == 2:
                        auxLista= LeerArchivo.obtenerLista()
                        tempLista=auxLista.obtenerValor(self.indiceGlobalLista)
                        LeerArchivo.crearArbol(tempLista)
                    elif condicion2 == 3:
                        auxLista = LeerArchivo.obtenerLista()
                        tempLista = auxLista.obtenerValor(self.indiceGlobalLista)
                        LeerArchivo.graficarPreOrden(tempLista)
                    elif condicion2 == 4:
                        auxLista = LeerArchivo.obtenerLista()
                        tempLista = auxLista.obtenerValor(self.indiceGlobalLista)
                        LeerArchivo.graficarInorden(tempLista)
                    elif condicion2 == 5:
                        auxLista = LeerArchivo.obtenerLista()
                        tempLista = auxLista.obtenerValor(self.indiceGlobalLista)
                        LeerArchivo.graficarPostOrden(tempLista)
                    elif condicion2 == 0:
                        print("Entro en salir")
                    else:
                        print("--------------------------------")
                        print("Escriba un numero entre 1-3")
                        print("--------------------------------")
            elif condicion==0:
                print("Entro en salir")
            else:
                print("--------------------------------")
                print("Escriba un numero entre 1-3")
                print("--------------------------------")



def encriptarHash(hashCodigo):
    aux = \
        hashlib.sha256(hashCodigo.encode()).hexdigest()
    return aux

listaUsuario = LeerArchivo.obtenerLista()


def pintarVentana(index):
    curses.start_color()
    # window.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    ventanaUsuario.border(0)
    ventanaUsuario.nodelay(True)  # PONE LAS CADENAS QUE PUSE DENTRO DE LA VENTANA
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    ventanaUsuario.addstr(0, 25, 'DATA')
    ventanaUsuario.addstr(9, 22,"<---  " + str(listaUsuario.obtenerValor(index)) + "  --->", curses.color_pair(1))
    ventanaUsuario.refresh()
def MenuUsuario():
    if listaUsuario.primero!=None:
        indiceListaUsuario = 0
        pintarVentana(indiceListaUsuario)
        # key = ventanaUsuario.getch()
        while True:

            key = ventanaUsuario.getch()

            if (key == 54):  # VERIFICAMOS SI EL FLECHA A LA DERECHA
                indiceListaUsuario = indiceListaUsuario + 1
                ventanaUsuario.clear()
                ventanaUsuario.refresh()
                # print(index)
                pintarVentana(indiceListaUsuario)
                # key = ventanaUsuario.getch()
            elif (key == 52):  # VERIFICAMOS SI ES FLECHA A LA IZQUIERDA
                indiceListaUsuario = indiceListaUsuario - 1
                ventanaUsuario.clear()
                ventanaUsuario.refresh()
                # print(index)
                pintarVentana(indiceListaUsuario)
            # key = ventanaUsuario.getch()
            elif (key == 27):  # SI ES LA TECLA DE SCAPE....
                ventanaUsuario.clear()
                ventanaUsuario.refresh()
                ventanaUsuario.addstr(6, 25, 'Regresando al menu Incial....', curses.color_pair(1))
                ventanaUsuario.refresh()
                curses.napms(2000)
                # nombre = listaUsuario.obtenerValor(indiceListaUsuario)
                # indice = indiceListaUsuario
                break
        curses.endwin()
    else:
        ventanaUsuario.clear()
        ventanaUsuario.refresh()
        ventanaUsuario.addstr(9, 25, 'NO HAY NADA EN LA LISTA')
        ventanaUsuario.refresh()
        curses.napms(2000)


MenuPractica().menuPrincipal()
