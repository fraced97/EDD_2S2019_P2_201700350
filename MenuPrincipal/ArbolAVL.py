class NodoAVL:
    def __init__(self, valor):
     self.valor=valor
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
    def insertar(self,numero:int):
        nuevo = NodoAVL(numero)
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

p=ArbolAVLOriginal()
p.insertar(10)
p.insertar(5)
p.insertar(13)
p.insertar(1)
p.insertar(6)
p.insertar(17)
p.insertar(16)
p.preorden(p.obtenerValorRaiz())