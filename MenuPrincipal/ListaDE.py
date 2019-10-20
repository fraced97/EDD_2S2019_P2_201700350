import os
class NodoListaDE():
    def __init__(self, valor, valor2):
        self.siguiente = None
        self.anterior = None
        self.valor = valor
        self.valor2 = valor2
class ListaDE():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0
        self.puntuacion = 0

    def estaVacia(self):
        return self.primero is None


    def insertar_final(self,valor,valor2):
        nuevo = NodoListaDE(valor,valor2)
        if self.primero is None:
            self.primero = nuevo
        else:
            temporal = self.primero
            while temporal.siguiente!=None:
                temporal=temporal.siguiente
            self.ultimo = nuevo
            temporal.siguiente = self.ultimo
            self.ultimo.anterior=temporal

        self.tamanio = self.tamanio + 1


    def inserta_pos(self,index,valor,valor2):
        contador = 0
        if index == 0:
            nuevo = NodoListaDE(valor, valor2)
            self.primero.anterior = nuevo
            nuevo.siguiente = self.primero
            self.primero = nuevo

            self.tamanio = self.tamanio + 1


    def sacarUltimo(self):
        temporal = self.primero
        while temporal.siguiente != self.ultimo:
            temporal = temporal.siguiente
        temporal2 = self.ultimo
        self.ultimo.anterior = None
        self.ultimo = temporal
        self.ultimo.siguiente = None
        self.tamanio = self.tamanio - 1
        return (temporal2.valor, temporal2.valor2)

    def listaEsNula(self):
        if self.primero==None:
            return True
        else:
            return False

    def darPrimero(self):
        temp = self.primero
        return (temp.valor , temp.valor2)

    def listaCompleta(self):
        temp = self.primero
        while temp is not None:
            temp = temp.siguiente
            return temp
    def limpiarLista(self):
        self.primero = None
    def contarNodos(self):
        temp = self.primero
        index=0
        while temp is not None:
            temp = temp.siguiente
            index=index+1
        return index
    def retornarUltimoNodo(self):
        temp = self.primero
        while temp.siguiente is not None:
            temp = temp.siguiente
        return temp
    def obtenerValor(self,index):
        aux=self.primero
        contador = 0
        while index != contador:
            contador = contador + 1
            aux= aux.siguiente
        #self.nombre = aux.valor
        return aux.valor

    def graficarSerpiente(self):
        try:
            f = open("Lista.dot", "w")
            f.write("digraph G {\n")
            f.write("rankdir = LR \n node [shape = square];\n")
            temporal = self.primero
            while temporal.siguiente is not None:

                f.write("\"" + str(temporal.valor) + "," + str(temporal.valor2) + "\"->""\"" + str(
                    temporal.siguiente.valor) + "," + str(temporal.siguiente.valor2) + "\";\n")
                f.write("\"" + str(temporal.siguiente.valor) + "," + str(temporal.siguiente.valor2) + "\"->""\"" + str(
                    temporal.valor) + "," + str(temporal.valor2) + "\";\n")

                temporal = temporal.siguiente
            f.write("}")

            f.close()

            os.system("dot -Tjpg Lista.dot -o imagenLista.jpg")
            os.system("imagenLista.jpg")
        except:
            print("NO HAY NADA")