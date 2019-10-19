import os
class NodoAVL:
    def __init__(self, carnet,nombre):
     self.valor=carnet
     self.valor2=nombre
     self.factorEquilibrio=0
     #self.hojaIzquierda:NodoAVL
     self.hojaIzquierda=None
     #self.hojaDerecha:NodoAVL
     self.hojaDerecha=None
class ArbolAVLOriginal:
    raiz : NodoAVL
    def __init__(self):
        self.raiz=None
    def buscarNodo(self,dato,raiz2:NodoAVL):
        if(raiz2==None):
            return None
        elif (raiz2.valor<dato):
            return self.buscarNodo(dato, raiz2.hojaDerecha)
        else:
            return self.buscarNodo(dato, raiz2.hojaIzquierda)
    def insertar(self,numero,nombre):
        nuevo = NodoAVL(numero,nombre)
        if(self.raiz == None):
            self.raiz=nuevo
        else:
            self.raiz=self.insertarNodo(nuevo,self.raiz)
    def izquierda(self, dato3:NodoAVL):
        temporal:NodoAVL
        temporal=dato3.hojaIzquierda
        dato3.hojaIzquierda = temporal.hojaDerecha
        temporal.hojaDerecha=dato3
        dato3.factorEquilibrio=max(self.factorDeEquilibrio(dato3.hojaIzquierda),self.factorDeEquilibrio(dato3.hojaDerecha))+1
        temporal.factorEquilibrio=max(self.factorDeEquilibrio(temporal.hojaIzquierda),self.factorDeEquilibrio(temporal.hojaDerecha))+1
        return temporal

    def factorDeEquilibrio(self,dato2:NodoAVL):
        if(dato2==None):
            return -1
        else:
            return dato2.factorEquilibrio

    def izquierda2(self, aux: NodoAVL):
        temp: NodoAVL
        aux.hojaIzquierda = self.derecha(aux.hojaIzquierda)
        temp = self.izquierda(aux)
        return temp

    def derecha(self, dato4:NodoAVL):
        temporal:NodoAVL
        temporal=dato4.hojaDerecha
        dato4.hojaDerecha = temporal.hojaIzquierda
        temporal.hojaIzquierda=dato4
        dato4.factorEquilibrio=max(self.factorDeEquilibrio(dato4.hojaIzquierda),self.factorDeEquilibrio(dato4.hojaDerecha))+1
        temporal.factorEquilibrio=max(self.factorDeEquilibrio(temporal.hojaIzquierda),self.factorDeEquilibrio(temporal.hojaDerecha))+1
        return temporal


    def derecha2(self, aux: NodoAVL):
        temp: NodoAVL
        aux.hojaDerecha = self.izquierda(aux.hojaDerecha)
        temp = self.derecha(aux)
        return temp

    def insertarNodo(self, nuevo:NodoAVL, aux:NodoAVL):
        nuevaHoja:NodoAVL
        nuevaHoja = aux
        if(nuevo.valor<aux.valor):
            if(aux.hojaIzquierda==None):
                aux.hojaIzquierda=nuevo
            else:
                aux.hojaIzquierda = self.insertarNodo(nuevo,aux.hojaIzquierda)
                if ((self.factorDeEquilibrio(aux.hojaIzquierda)) - (self.factorDeEquilibrio(aux.hojaDerecha)))==2:
                    if(nuevo.valor<aux.hojaIzquierda.valor):
                        nuevaHoja=self.izquierda(aux)
                    else:
                        nuevaHoja=self.izquierda2(aux)
        elif(nuevo.valor>aux.valor):
            if(aux.hojaDerecha==None):
                aux.hojaDerecha=nuevo
            else:
                aux.hojaDerecha=self.insertarNodo(nuevo,aux.hojaDerecha)
                if(self.factorDeEquilibrio(aux.hojaDerecha)-self.factorDeEquilibrio(aux.hojaIzquierda)==2):
                    if(nuevo.valor>aux.hojaDerecha.valor):
                        nuevaHoja=self.derecha(aux)
                    else:
                        nuevaHoja=self.derecha2(aux)
        else:
            print("NODO YA EXISTE")
        if((aux.hojaIzquierda==None) and (aux.hojaDerecha!=None)):
            aux.factorEquilibrio=aux.hojaDerecha.factorEquilibrio+1
        elif((aux.hojaDerecha==None)and(aux.hojaIzquierda!=None)):
            aux.factorEquilibrio=aux.hojaIzquierda.factorEquilibrio+1
        else:
            aux.factorEquilibrio=max(self.factorDeEquilibrio(aux.hojaIzquierda),self.factorDeEquilibrio(aux.hojaDerecha))+1
        return nuevaHoja

    def postorden(self, aux: NodoAVL):
        if (aux != None):
            self.postorden(aux.hojaIzquierda)
            self.postorden(aux.hojaDerecha)
            print(aux.valor)


    def inorden(self,aux:NodoAVL):
        if(aux!=None):
            self.inorden(aux.hojaIzquierda)
            print(aux.valor)
            self.inorden(aux.hojaDerecha)

    def preorden(self, aux: NodoAVL):
        if (aux != None):
            print(aux.valor)
            self.preorden(aux.hojaIzquierda)
            self.preorden(aux.hojaDerecha)


    def obtenerValorRaiz(self):
        return self.raiz

    def graficarInorden(self):
        try:
            f = open("Inorden.dot", "w")
            f.write("digraph G {\n")
            f.write("rankdir = LR \n node [shape = square];\n")
            self.inordenG(self.raiz,f)
            f.write("}")

            f.close()
            archivo = open("Inorden.dot")
            aux=archivo.read().rstrip("->}")
            archivo.close()
            original = open("Inorden.dot", "w")
            original.write(aux+"}")
            original.close()


            os.system("dot -Tjpg Inorden.dot -o imagenInorden.jpg")
            os.system("imagenInorden.jpg")
        except:
            print("NO HAY NADA")
    def inordenG(self,raiz6:NodoAVL,f):
        if (raiz6 != None):
            self.inordenG(raiz6.hojaIzquierda, f)
            f.write("\""+str(raiz6.valor)+", "+raiz6.valor2+", "+str(raiz6.factorEquilibrio)+"\"->")
            self.inordenG(raiz6.hojaDerecha,f)

    def graficarPostOrden(self):
        try:
            f = open("PostOrden.dot", "w")
            f.write("digraph G {\n")
            f.write("rankdir = LR \n node [shape = square];\n")
            self.postordenG(self.raiz,f)
            f.write("}")

            f.close()
            archivo = open("PostOrden.dot")
            aux=archivo.read().rstrip("->}")
            archivo.close()
            original = open("PostOrden.dot", "w")
            original.write(aux+"}")
            original.close()


            os.system("dot -Tjpg PostOrden.dot -o imagenPostOrden.jpg")
            os.system("imagenPostOrden.jpg")
        except:
            print("NO HAY NADA")
    def postordenG(self,raiz7:NodoAVL,f):
        if (raiz7 != None):
            self.postordenG(raiz7.hojaIzquierda, f)
            self.postordenG(raiz7.hojaDerecha, f)
            f.write("\"" + str(raiz7.valor) + ", " + raiz7.valor2 + ", " + str(raiz7.factorEquilibrio) + "\"->")
    def graficarPreOrden(self):
        try:
            f = open("PreOrden.dot", "w")
            f.write("digraph G {\n")
            f.write("rankdir = LR \n node [shape = square];\n")
            self.preOrdenG(self.raiz,f)
            f.write("}")

            f.close()
            archivo = open("PreOrden.dot")
            aux=archivo.read().rstrip("->}")
            archivo.close()
            original = open("PreOrden.dot", "w")
            original.write(aux+"}")
            original.close()


            os.system("dot -Tjpg PreOrden.dot -o imagenPreOrden.jpg")
            os.system("imagenPreOrden.jpg")
        except:
            print("NO HAY NADA")
    def preOrdenG(self,raiz7:NodoAVL,f):
        if (raiz7 != None):
            f.write("\"" + str(raiz7.valor) + ", " + raiz7.valor2 + ", " + str(raiz7.factorEquilibrio) + "\"->")
            self.preOrdenG(raiz7.hojaIzquierda, f)
            self.preOrdenG(raiz7.hojaDerecha, f)


p=ArbolAVLOriginal()
p.insertar(10,"hola")
p.insertar(5,"hola")
p.insertar(13,"hola")
p.insertar(1,"hola")
p.insertar(6,"hola")
p.insertar(17,"hola")
p.insertar(16,"hola")
p.preorden(p.obtenerValorRaiz())
p.graficarPreOrden()