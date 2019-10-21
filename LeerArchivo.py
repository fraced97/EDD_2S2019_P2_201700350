import csv
import datetime
import ListaDE
import hashlib
import json
import ArbolAVL
import Cliente

conexionCliente= Cliente.Client()
class leerArchivo():
#x  listaSimple = ListaDE.ListaDE()

    indiceJson = ListaDE.ListaDE()
    #def activar(self):
     #   d=Cliente.Client()


    def jsonCorrecto(self,cadenaJson):
        try:
            cadenaJson2 = str(cadenaJson).replace("\'", '"').replace("None", "null")
            listaAux = json.loads(str(cadenaJson2))
            hashAnterior = listaAux["PREVIOUSHASH"]
            print(hashAnterior+"   ESTE ES EL HASHANTERIOR")
            hashActual = listaAux["HASH"]
            clase = listaAux["CLASS"]
            indice = listaAux["INDEX"]
            fechaHora = listaAux["TIMESTAMP"]
            data = listaAux["DATA"]
            hashJson = self.encriptarHash(str(indice) + str(fechaHora) + str(clase) + str(data).replace("\'", '"').replace("None", "null").replace(" ","") + str(hashAnterior))
            print(hashJson+"     ESTE ES HASH QUE GENERO CON LOS DATOS DEL JSON")
            print(hashActual+ "   ESTE EL EL HASH")
            if hashJson != hashActual:

                return "false"
            else:
                return "true"
        except Exception as e:
            print(e)
            pass

    def guardarJson(self,cadenaJson):
        cadenaJson2 = json.loads(str(cadenaJson))
        self.indiceJson.insertar_final(cadenaJson, cadenaJson2["HASH"])



    def encriptarHash(self,hashCodigo):
        aux = hashlib.sha256(hashCodigo.encode()).hexdigest()
        return aux

    def generarData(self,rutaArchivo):

        with open(rutaArchivo, 'r') as abrir:
            leer= csv.reader(abrir)
            archivo = list(leer)

        indiceBloque = self.indiceJson.contarNodos()
        clase=archivo[0][1]
        fechaHora = datetime.datetime.now()
        data = archivo[1][1]

        #fechaHora.strftime('%m-%d-%y %H:%M:%S')
        #auxfechaHora="02-10-19-::14:30:25"
        #auxhashAnterior ="fd5f6d5fdfdf232Y232312QW12196255"

        if self.indiceJson.listaEsNula():
            hashAnterior = self.indiceJson.retornarUltimoNodo().valor2
        else:
            hashAnterior = '0000'


        print(data.replace(" ","").replace("\n",""))
        print(hashAnterior+"    Y ESTE ES EL HASH QUE ANTERIOR QUE SE GENERA ANTES")
        objetoJson = json.dumps(str(data).replace(" ","").replace("\n",""))
        auxobj=str(objetoJson).replace("\\","")

        objetoJson2 = json.loads(str(data).replace(" ","").replace("\n",""))
        hashActual=  self.encriptarHash(str(indiceBloque) + str(fechaHora.strftime('%m-%d-%y-::%H:%M:%S')) + str(clase) + str(objetoJson2).replace("None", "null").replace(" ", "").replace("\'", '"') + str(hashAnterior))

        textoJson = "{\n" + '"INDEX": ' + "\""+str(indiceBloque)+"\"" + ",\n" + '"TIMESTAMP": ' + "\""+ str(fechaHora.strftime('%m-%d-%y-::%H:%M:%S'))+"\""+ ",\n"+'"CLASS": '+"\""+ str(clase)+"\""+",\n"+'"DATA": '+ str(data)+ ",\n"+'"PREVIOUSHASH": '+ "\""+ str(hashAnterior)+"\""+",\n"
        textoJson = textoJson + '"HASH": '+ "\""+str(hashActual)+"\"" + "\n}"
        #print(textoJson)
        #print(objetoJson)
        #print(auxobj)
        #print(str(objetoJson2).replace("None", "null").replace(" ", "").replace("\'", '"'))
        #print(str(2) + str(fechaHora) + str(clase) + str(objetoJson2).replace("\'", '"').replace("None", "null").replace(" ", "") + str(hashAnterior))
        conexionCliente.cliente.sendall(textoJson.encode('utf-8'))
        conexionCliente.cadenaJson = textoJson
    #def graficarLista(self):
     #   self.indiceJson.graficarLista(self.indiceJson.primero)

    def encontrarCarnets(self,cadenJson):
        carnets = []
        def encontrarNombre(carnetNombre):
            try:
                carnets.append(carnetNombre['value'])
            except KeyError:
                print("Error")
            return carnetNombre
        json.loads(cadenJson, object_hook=encontrarNombre)
        return carnets

    def crearArbol(self,cadenaJson):
        auxArbol = ArbolAVL.ArbolAVLOriginal()
        jsonCadena = str(cadenaJson)
        temp = self.encontrarCarnets(str(jsonCadena))
        #print(temp)

        for i in temp:
            aux = str(i).split("-")
            auxArbol.insertar(aux[0], aux[1])
        auxArbol.graficarArbol()

    def graficarInorden(self,cadenaJson):
        auxArbol = ArbolAVL.ArbolAVLOriginal()
        jsonCadena = str(cadenaJson)
        temp = self.encontrarCarnets(str(jsonCadena))

        for iteracion in temp:
            aux = str(iteracion).split("-")
            auxArbol.insertar(aux[0], aux[1])
        auxArbol.graficarInorden()
        auxArbol.inorden2()

    def graficarPostOrden(self,cadenaJson):
        auxArbol = ArbolAVL.ArbolAVLOriginal()
        jsonCadena = str(cadenaJson)
        temp = self.encontrarCarnets(str(jsonCadena))

        for iteracion in temp:
            aux = str(iteracion).split("-")
            auxArbol.insertar(aux[0], aux[1])
        auxArbol.graficarPostOrden()
        auxArbol.postorden2()

    def graficarPreOrden(self,cadenaJson):
        auxArbol = ArbolAVL.ArbolAVLOriginal()
        jsonCadena = str(cadenaJson)
        temp = self.encontrarCarnets(str(jsonCadena))

        for iteracion in temp:
            aux = str(iteracion).split("-")
            auxArbol.insertar(aux[0], aux[1])
        auxArbol.graficarPreOrden()
        auxArbol.preorden2()
    def obtenerLista(self):
        return self.indiceJson
