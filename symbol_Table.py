class nodoST(object):
    def __init__(self, tipo, identificador, valor):
        self.padre = None
        self.symbolTable = None
        self.tipo = tipo
        self.identificador = identificador
        self.valor = valor

    def getPadre(self):
        return self.padre

    def setPadre(self, st):
        self.padre = st

    def getsymbolTable(self):
        return self.symbolTable

    def setsymbolTable(self, st):
        self.symbolTable = st


class symbolTable(object):
    def __init__(self):
        self.listNodo = []
        self.listParam = []

    def agregar(self, Nodo):
        self.listNodo.append(Nodo)

    def getNodos(self):
        return self.listNodo

    def agregarParam(self, Nodo):
        self.listParam.append(Nodo)

    def getParam(self):
        return self.listParam