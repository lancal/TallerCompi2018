
from symbol_Table import *

from parser import scope_variables
from parser import scope_function

import re

erroresSemanticos1 = []
erroresSemanticos2 = []

listAsignaciones = []
listFunciones = []

st = symbolTable()

class nodo():
    pass

class programa(nodo):

    def __init__(self, lista_decl_p):

        self.lista_decl_p = lista_decl_p
        self.nombre = 'Programa '
        self.errorColor = True
        self.checkSymbolTable()

    def checkSymbolTable(self):

         for dl in self.lista_decl_p:

             dl.checkSymbolTable(st)

    def accept(self,visitor):

        visitor.visit_programa(self)

class nodoDeclaracionVar(nodo):

    def __init__(self,def_tipo_p,ID_t,thereis_num = False,NUM_t=None):

        self.def_tipo_p = def_tipo_p
        self.ID_t = ID_t
        self.thereis_num = thereis_num
        self.NUM_t = NUM_t
        self.nombre = 'Declaracion Var '
        self.errorColor = None

    def checkSymbolTable(self, stb):

        patron = re.compile(r'vacuo', re.I)
        arreglo = patron.findall(str(self.def_tipo_p))

        if self.def_tipo_p == arreglo:

            self.errorColor = True

            erroresSemanticos1.append("Variable " + self.ID_t + " declarada no puede ser del tipo " + arreglo[0])

        if self.NUM_t is None:

            vardec = nodoST(self.def_tipo_p, self.ID_t, None)
            vardec.setPadre(stb)
            stb.agregar(vardec)

        else:

            vardec = nodoST(self.def_tipo_p, self.ID_t, None)
            vardec.setPadre(stb)
            stb.agregar(vardec)

    def accept(self, visitor):
        visitor.visit_nodoDeclaracionVar(self)

class nodoDeclaracionFun(nodo):

    def __init__(self,def_tipo_p,ID_t,parametros_p,sentencia_comp_p):

        self.def_tipo_p = def_tipo_p
        self.ID_t = ID_t
        self.parametros_p = parametros_p
        self.sentencia_comp_p = sentencia_comp_p
        self.nombre = 'Declaracion Fun '
        self.nombre2 = 'Error Nodo Declaracion Fun '
        self.errorColor = None

    def checkSymbolTable(self,stb):

        fun = nodoST(self.def_tipo_p, self.ID_t, None)
        listFunciones.append(fun)
        fun.setPadre(stb)
        st2 = symbolTable()

        self.patron = re.compile(r'vacuo', re.I)
        self.arreglo = self.patron.findall(str(self.parametros_p))


        if self.arreglo:

            if self.parametros_p == self.arreglo[0]:

                self.errorColor = True

                erroresSemanticos1.append("Parametro " + self.parametros_p + " de la variable "
                                          + self.ID_t + " declarado es invalido")

        else:

            for ps in self.parametros_p:

                ps.checkSymbolTable(st2)

        fun.setsymbolTable(st2)

        stb.agregar(fun)

        self.sentencia_comp_p.checkSymbolTable(st2)

    def accept(self,visitor):

        visitor.visit_nodoDeclaracionFun(self)

class nodoParam(nodo):

    def __init__(self,def_tipo_p,thereis_ID = False,ID_t = None,Lt_Rt = None):

        self.def_tipo_p = def_tipo_p
        self.ID_t = ID_t
        self.thereis_ID = thereis_ID
        self.Lt_Rt = Lt_Rt
        self.nombre = 'Param '
        self.errorColor = None

    def checkSymbolTable(self, stb):

        self.patron = re.compile(r'vacuo', re.I)
        self.arreglo = self.patron.findall(str(self.def_tipo_p))

        if self.arreglo:

            if self.def_tipo_p == self.arreglo[0] :

                if self.def_tipo_p == "VACUO":

                    self.errorColor = True

                    erroresSemanticos1.append("Parametro " + self.def_tipo_p + " declarado es invalido")
                else:

                    for ps in self.def_tipo_p:

                        ps.checkSymbolTable(stb)
            else:

                self.errorColor = True

                erroresSemanticos1.append("Parametro " + self.def_tipo_p[0]
                                          + " de la variable " + self.ID_t +   " declarado es invalido")
        else:

            pass


        if self.Lt_Rt is None:

            param = nodoST(self.def_tipo_p,self.ID_t,None)
            param.setPadre(stb)
            stb.agregar(param)
            stb.agregarParam(param)

        else:

            param = nodoST(self.def_tipo_p, self.ID_t, None)
            param.setPadre(stb)
            stb.agregar(param)
            stb.agregarParam(param)

    def accept(self,visitor):
        visitor.visit_nodoParam(self)

class nodoSentenciaComp(nodo):

    def __init__(self,declaraciones_locales_p,lista_sentencias_p,is_vacio=False,vacio_t=None):

        self.declaraciones_locales_p = declaraciones_locales_p
        self.lista_sentencias_p = lista_sentencias_p
        self.is_vacio = is_vacio
        self.vacio_t = vacio_t
        self.nombre = 'Sentencia Comp '
        self.errorColor = False

    def checkSymbolTable(self, stb):

        listSymbol = st.getNodos()

        for local in self.declaraciones_locales_p:

            if local.nombre != "vacio":

                local.checkSymbolTable(stb)

            else:
                pass

        for state in self.lista_sentencias_p:

            if isinstance(self.lista_sentencias_p, list):

                for ls in listSymbol:

                    patron6 = re.compile(r'vacuo', re.I)
                    arreglo6 = patron6.findall(str(ls.tipo))

                    if isinstance(state,nodoVacio) or isinstance(state,nodoExpresion) \
                            or isinstance(state, nodoSentenciaSeleccion) \
                            or isinstance(state, nodoSentenciaIteracion) \
                            or isinstance(state,nodoSentenciaRetorno):

                        pass

                    elif ls.identificador == state.ID_t and ls.getsymbolTable() is not None:

                        if arreglo6:

                            if ls.tipo == arreglo6:

                                self.errorColor = True

                                erroresSemanticos2.append("Error de tipo, expresion del REP tiene que ser de tipo ENT")

                        else:

                            pass

            if state.nombre != "vacio":

                state.checkSymbolTable(stb)

            else:
                pass


    def accept(self,visitor):
        visitor.visit_nodoSentenciaComp(self)

class nodoExpresion(nodo):

    def __init__(self,var_p = None,thereIsVar=False,expresion_p = None, thereisExpresion=False,
                 semicolon_t = None, thereisSemicolon=False,
                 assign=None):
        self.var_p = var_p
        self.thereIsVar = thereIsVar
        self.expresion_p = expresion_p
        self.thereisExpresion = thereisExpresion
        self.semicolon_t = semicolon_t
        self.thereisSemicolon = thereisSemicolon
        self.assign = assign
        self.nombre = 'Expresion '
        self.errorColor = False

    def checkSymbolTable(self, stb):

        listSymbol = st.getNodos()

        listaNodosActual = stb.getNodos()

        if self.thereIsVar == True and self.thereisExpresion ==True:

            if isinstance(self.expresion_p,nodoExpresion):

                listAsignaciones.append(self.expresion_p)

                idvar = self.expresion_p.var_p

                if idvar.expresion_p is None:

                    isDeclared(listSymbol, listaNodosActual, idvar)

                    #print(isDeclared(listSymbol, listaNodosActual, idvar))
                    #print("isDeclared")

                else:

                    temp = nodoVar(None,False,None)
                    temp.ID_t = idvar.ID_t + "<>"

                    isDeclared(listSymbol, listaNodosActual, temp)

                if not isinstance(self.expresion_p.expresion_p,nodoBinarioOP):

                    idvar = self.expresion_p.expresion_p

                    if not isinstance(idvar, nodoNUM) and not isinstance(idvar, nodoInvocacion):

                        if idvar.expresion_p is None:

                            isDeclared(listSymbol, listaNodosActual, idvar)

                            isInitialized(listAsignaciones, idvar)

                        else:

                            temp = nodoVar(None, False, None)
                            temp.ID_t = idvar.ID_t + "<>"
                            isDeclared(listSymbol, listaNodosActual, temp)
                            temp.ID_t = idvar.ID_t + "<" + idvar.expression.NUM_t + ">"

                            isInitialized(listAsignaciones, temp)

            if isinstance(self.expresion_p,nodoVar):

                idvar = self.expresion_p

                isDeclared(listSymbol, listaNodosActual, idvar)

                isInitialized(listAsignaciones, idvar)

                self.var_p.checkSymbolTable(stb)

            else:

                listSymbol = st.getNodos()

                listaNodosActual = stb.getNodos()

                idvar = self.var_p

                isDeclared(listSymbol, listaNodosActual, idvar)

                isInitialized(listAsignaciones, idvar)

                self.expresion_p.checkSymbolTable(stb)

    def accept(self,visitor):
        visitor.visit_nodoExpresion(self)

class nodoSentenciaSeleccion(nodo):

    def __init__(self,expresion_p,sentencia_p,is_else = False,sentencia_p2=None):
        self.expresion_p = expresion_p
        self.sentencia_p = sentencia_p
        self.is_else = is_else
        self.sentencia_p2 = sentencia_p2
        self.nombre = 'Sentencia Seleccion '
        self.errorColor = False

    def checkSymbolTable(self, stb):

        if self.sentencia_p2 is None:

            listSymbol = st.getNodos()

            if isinstance(self.expresion_p, nodoInvocacion):

                for ls in listSymbol:

                    patron2 = re.compile(r'vacuo', re.I)
                    arreglo2 = patron2.findall(str(ls.tipo))

                    if ls.identificador == self.expresion_p.ID_t and ls.getsymbolTable() is not None:

                        if arreglo2:

                            if ls.tipo == arreglo2:

                                self.errorColor = True

                                erroresSemanticos2.append("Error de tipo, expresion del SI tiene que ser de tipo ENT")

                        else:

                            pass


            self.expresion_p.checkSymbolTable(stb)
            ifn = nodoST('Nodo', "SI", None)
            ifn.setPadre(stb)
            st3 = symbolTable()
            ifn.setsymbolTable(st3)
            stb.agregar(ifn)

            self.sentencia_p.checkSymbolTable(stb)

        else:

            listSymbol = st.getNodos()

            if isinstance(self.expresion_p, nodoInvocacion):
                for ls in listSymbol:

                    patron3 = re.compile(r'vacuo', re.I)
                    arreglo3 = patron3.findall(str(ls.tipo))

                    if ls.identificador == self.expresion_p.ID_t and ls.getsymbolTable() is not None:

                        if arreglo3:

                            if ls.tipo == arreglo3:

                                self.errorColor = True

                                erroresSemanticos2.append("Error de tipo, expresion del SINO tiene que ser de tipo ENT")

                        else:

                            pass


            self.expresion_p.checkSymbolTable(stb)
            ifne = nodoST('Nodo', "SI", None)
            ifne.setPadre(stb)
            st4 = symbolTable()
            ifne.setsymbolTable(st4)
            stb.agregar(ifne)
            self.sentencia_p.checkSymbolTable(stb)

            nelse = nodoST('Nodo', "SINO", None)
            nelse.setPadre(stb)
            st5 = symbolTable()
            nelse.setsymbolTable(st5)
            stb.agregar(nelse)
            self.sentencia_p2.checkSymbolTable(stb)


    def accept(self,visitor):
        visitor.visit_nodoSentenciaSeleccion(self)

class nodoSentenciaIteracion(nodo):

    def __init__(self,thereis_expresion = False,expresion_p=None,thereis_sentencia = False,sentencia_p=None,
                 thereis_sentencia_comp = False,sentencia_comp_p = None,rep=None):

        self.thereis_expresion = thereis_expresion
        self.expresion_p = expresion_p
        self.thereis_sentencia = thereis_sentencia
        self.sentencia_p = sentencia_p
        self.thereis_sentencia_comp = thereis_sentencia_comp
        self.sentencia_comp_p = sentencia_comp_p
        self.rep = rep
        self.nombre = 'Sentencia Iteracion '
        self.y = ""
        self.errorColor = False

    def checkSymbolTable(self,stb):

        if self.thereis_expresion == True and self.thereis_sentencia == True:

            listSymbol = st.getNodos()

            if isinstance(self.expresion_p, nodoInvocacion):
                for ls in listSymbol:

                    patron4 = re.compile(r'vacuo', re.I)
                    arreglo4 = patron4.findall(str(ls.tipo))

                    if ls.identificador == self.expresion_p.ID_t and ls.getsymbolTable() is not None:

                        if arreglo4:

                            if ls.tipo == arreglo4:

                                self.errorColor = True

                                erroresSemanticos2.append("Error de tipo, expresion del MIENTRAS tiene que ser de tipo ENT")

                        else:

                            pass

            self.expresion_p.checkSymbolTable(stb)
            whilen = nodoST('Nodo', "MIENTRAS", None)
            whilen.setPadre(stb)
            st4 = symbolTable()
            whilen.setsymbolTable(st4)
            stb.agregar(whilen)
            self.sentencia_p.checkSymbolTable(stb)

        elif self.thereis_sentencia_comp == True :

            rep = nodoST('Nodo', "REP", None)
            rep.setPadre(stb)
            st5 = symbolTable()
            rep.setsymbolTable(st5)
            stb.agregar(rep)

            self.sentencia_comp_p.checkSymbolTable(stb)

    def accept(self,visitor):
        visitor.visit_nodoSentenciaIteracion(self)

class nodoSentenciaRetorno(nodo):

    def __init__(self,thereis_expression = False, expresion_p = None):

        self.thereis_expression = thereis_expression
        self.expresion_p = expresion_p
        self.nombre = 'Sentencia Retorno '
        self.nombre2 =  'RET ;'
        self.nombre3 = 'RET'
        self.errorColor = False

    def checkSymbolTable(self,st):

        if self.expresion_p is None:

            pass

        else:

            self.expresion_p.checkSymbolTable(st)


    def accept(self,visitor):
        visitor.visit_nodoSentenciaRetorno(self)

class nodoVar(nodo):

    def __init__(self,ID_t=None, is_vec_access=False, expresion_p=None):
        self.ID_t = ID_t
        self.is_vec_access = is_vec_access
        self.expresion_p = expresion_p
        self.nombre = 'Var '
        self.errorColor = None

    def checkSymbolTable(self,stb):

        if self.expresion_p is None:

            pass

        else:

            self.expresion_p.checkSymbolTable(stb)


    def accept(self,visitor):
        visitor.visit_nodoVar(self)

class nodoExpresionLogica(nodo):

    def __init__(self,thereis_exp_log = False, expresion_logica_p = None , expresion_simple_p = None):

        self.thereis_exp_log =thereis_exp_log
        self.expresion_logica_p = expresion_logica_p
        self.expresion_simple_p = expresion_simple_p
        self.nombre = 'Expresion Logica '
        self.errorColor = False

    def checkSymbolTable(self, st):

        if isinstance(self.expresion_logica_p, list):

            aux = self.expresion_logica_p

        else:

            aux = [self.expresion_logica_p]

        for expresionLogica in aux:

            if self.expresion_logica_p is not None:

                expresionLogica.checkSymbolTable(st)
            else:

                pass

        if isinstance(self.expresion_simple_p, list):

            aux2 = self.expresion_simple_p

        else:

            aux2 = [self.expresion_simple_p]

        for expresionSimple in aux2:

            if isinstance(self.expresion_simple_p,nodoSentenciaIteracion):

                expresionSimple.checkSymbolTable(st)

            elif isinstance(self.expresion_simple_p,nodoSentenciaSeleccion):

                expresionSimple.checkSymbolTable(st)

            elif isinstance(self.expresion_simple_p,nodoSentenciaRetorno):

                expresionSimple.checkSymbolTable(st)

            else:

                pass


    def accept(self,visitor):
        visitor.visit_nodoExpresionLogica(self)

class nodoBinarioOP(nodo):

    def __init__(self,is_rama = False,ramaIzq_p=None, ramaDer_p=None, operacion_p=None,nombre2 = None):

        self.is_rama = is_rama
        self.ramaIzq_p = ramaIzq_p
        self.ramaDer_p = ramaDer_p
        self.operacion_p = operacion_p
        self.nombre = 'Nodo Binario Op '
        self.nombre2 = nombre2
        self.errorColor = False

    def checkSymbolTable(self,stb):

        # ---------------------------------------------------------------VERIFICACION DE TIPOS OPERANDO-----------------------------------------
        listSymbol = st.getNodos()
        if isinstance(self.ramaDer_p, nodoInvocacion):
            for ls in listSymbol:
                if ls.identificador == self.ramaDer_p.ID_t and ls.getsymbolTable() is not None:
                    if ls.tipo == "ent":
                        self.errorColor = True
                        erroresSemanticos2.append(
                            "Error de tipo, la operación no se puede realizar, el tipo de la funcion " + ls.identificador + "[] no es ENT")
        if isinstance(self.ramaIzq_p, nodoInvocacion):
            for ls in listSymbol:
                if ls.identificador == self.ramaIzq_p.ID_t and ls.getsymbolTable() is not None:
                    if ls.tipo == "ent":
                        self.errorColor = True
                        erroresSemanticos2.append(
                            "Error de tipo, la operación no se puede realizar, el tipo de la funcion " + ls.identificador + "[] no es ENT")

            # ----------------------------------------------------------------VERIFICACION VARIABLES INICIALIZADA----------------------------------------
        # BUSCAR SI LA VARIABLE HA SIDO DECLARADA

        listaNodosActual = stb.getNodos()

        # busco si la variable ha sido declarada en la tabla de simbolos donde me encuentro
        if isinstance(self.ramaDer_p, nodoVar):
            if self.ramaDer_p.expresion_p is None:
                isDeclared(listSymbol, listaNodosActual, self.ramaDer_p)
                isInitialized(listAsignaciones, self.ramaDer_p)
            else:
                temp = nodoVar(None, False, None)
                isDeclared(listSymbol, listaNodosActual, temp)
                temp.ident = self.ramaDer_p.ID_t + "< " + self.ramaDer_p.expresion_p.ID_t + " >"
                isInitialized(listAsignaciones, temp)

        if isinstance(self.ramaIzq_p, nodoVar):

            if self.ramaIzq_p.expresion_p is None:
                isDeclared(listSymbol, listaNodosActual, self.ramaIzq_p)
                isInitialized(listAsignaciones, self.ramaIzq_p)
            else:
                temp = nodoVar(None, False, None)
                temp.ident = self.ramaIzq_p.ID_t + "< >"
                isDeclared(listSymbol, listaNodosActual, temp)
                temp.ident = self.ramaIzq_p.ID_t + "< " + self.ramaIzq_p.expresion_p.NUM_t + " >"
                isInitialized(listAsignaciones, temp)

        # ------------------------------------------------------------------------------------------------------------------------------------------

        self.ramaDer_p.checkSymbolTable(st)

    def accept(self,visitor):
        visitor.visit_nodoBinarioOP(self)

class nodoNUM(nodo):

    def __init__(self, NUM_t):
        self.NUM_t = NUM_t
        self.nombre = 'NUM '
        self.errorColor = None

    def checkSymbolTable(self,st):

        pass

    def accept(self, visitor):
        visitor.visit_nodoNUM(self)


class nodoInvocacion(nodo):

    def __init__(self,ID_t, argumentos_p):

        self.ID_t = ID_t
        self.argumentos_p = argumentos_p
        self.nombre = 'Invocacion '
        self.errorColor = False

    def getID_t(self):

        return self.ID_t

    def checkSymbolTable(self,stb):

        # ----------------------------------------------------------------INVOCACIÓN FUNCIÓN NO DEFINIDA------------------------------------
        # obtengo los simbolos de la función en la que me encuentro
        liststfun = stb.getNodos()
        # obtengo los simbolos del programa

        lista = st.getNodos()

        # lista de parametros de la funcion invocacion
        listParam = []

        cont = 0
        # lista de las funciones que son iguales a la funcion invocacion
        listaFuncionesequal = []

        for func in listFunciones:
            if func.identificador == self.ID_t:
                cont += 1
                listaFuncionesequal.append(func)

        if cont == 0 and self.ID_t != "output" and self.ID_t != "input":
            self.errorColor = True
            erroresSemanticos2.append("Error Semántico, la invocacion de la funcion " + self.ID_t + "[] es incorrecta, funcion no ha sido declarada")

        else:
            if self.ID_t != "output" and self.ID_t != "input":
                # guardar los parametros de la funcion invocacion
                if type(self.argumentos_p) is list:
                    for arg in self.argumentos_p:
                        if arg.nombre is not 'vacio':
                            listParam.append(arg)
                else:
                    listParam.append(self.argumentos_p)
                    # revisar el tipo de parametros de la funcion
                tipo = []
                cant = 0

                for lp in listParam:
                    # busco la variable en la tabla de simbolos de la funcion donde me encuentro
                    for l in liststfun:

                        if l.identificador == lp.ID_t:
                            cant += 1
                            tipo.append(l.tipo)

                    if cant < len(listParam):
                        for n in lista:
                            if lp.ID_t == n.identificador and n.getsymbolTable() is None:
                                cant += 1
                                tipo.append(n.tipo)

                    isInitialized(listAsignaciones, lp)
                if cant < len(listParam):
                    self.errorColor = True
                    erroresSemanticos2.append("Error de tipo, la variable de la funcion " + self.ID_t + "[] no ha sido declarada")
                # verificar que los parametros han sido inicializados

                # verificar que se esta invocando la funcion de manera correcta
                count = 0
                for le in listaFuncionesequal:
                    param = le.getsymbolTable().getParam()
                    listParamEqual = []
                    for p in param:
                        listParamEqual.append(p.tipo)
                    if listParamEqual == tipo and len(tipo) > 0 and len(listParamEqual) > 0:
                        count += 1
                    # si es vacuo y no manda parametros
                    if len(param) == 0 and len(tipo) == 0:
                        count += 1
                if count == 0:
                    self.errorColor = True
                    erroresSemanticos2.append("Error de tipo, la invocacion de la funcion " + self.ID_t + "[] es incorrecta")

        if type(self.argumentos_p) is list:
            for arg in self.argumentos_p:
                if arg.nombre != 'vacio':
                    arg.checkSymbolTable(stb)
        else:

            self.argumentos_p.checkSymbolTable(stb)


    def accept(self,visitor):
        visitor.visit_nodoInvocacion(self)

class nodoVacio():

    def __init__(self):

        self.nombre = 'vacio'
        self.errorColor = None

    def checkSymbolTable(self,st):
        pass

    def accept(self,visitor):
        visitor.visit_nodoVacio(self)

def isDeclared(listSymbol, listaNodosActual, node):
    cont = 0
    for lna in listaNodosActual:
        if lna.identificador == node.ID_t:
            cont += 1
    if cont == 0:
        for ls in listSymbol:
            if ls.identificador == node.ID_t and ls.getsymbolTable() is None:
                cont += 1
                break
    if cont == 0:

        erroresSemanticos2.append("Error Semántico, Variable "+node.ID_t+" no declarada")

def isInitialized(listaasignaciones, node):

    if len(listaasignaciones) > 0:
        cont = 0
        for la in listaasignaciones:
            if la.var_p.expresion_p is not None:
                temp = nodoVar(None,False, None)
                temp.ID_t = la.var_p.ID_t + "< "+la.var_p.expresion_p.NUM_t+" >"

                if temp.ID_t == node.ID_t:
                    cont += 1
            else:
                if la.var_p.ID_t == node.ID_t:
                    cont += 1
        if cont == 0:
            erroresSemanticos2.append("Error de tipo, Variable "+node.ID_t+" no inicializada")
    #else:
        #erroresSemanticos2.append("Error de tipo, Variable "+node.ID_t+" no inicializada")

def getesp():
    return erroresSemanticos1

def getess():
    return erroresSemanticos2

def getTable():
    return st