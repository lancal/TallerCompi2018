# coding=utf-8

#from symbol_Table import *

from nodos import *

class visitor(object):

    def __init__(self):
        self.ast = ''
        self.id_program = 0
        self.id_declaracion_var= 0
        self.id_declaracion_fun = 0
        self.id_sentencia_comp = 0
        self.id_nodo = 0
        self.id_nodoListaParametros = 0
        self.id_nodoSentenciaSeleccion = 0
        self.id_nodoExpresion = 0
        self.id_nodoVar = 0
        self.id_nodoSentenciaRetorno = 0
        self.id_nodoExpresionNegada = 0
        self.id_nodoExpresionLogica = 0
        self.id_nodoBinarioOP = 0
        self.id_nodoNum = 0
        self.id_nodoInvocacion = 0
        self.id_nodoSentenciaIteracion = 0
        self.id_nodoVacio = 0
        self.id_nodoParam = 0

    def manyTimes(self,p1,p2,p3,p4):

        if p1 is not None:

            if isinstance(p1, list):

                aux = p1

            else:

                aux = [p1]

            for x in aux:

                if isinstance(x, str):

                    if p4.errorColor  == True:

                        self.id_nodo += 1
                        id_nodo = self.id_nodo

                        if isinstance(p4,nodoDeclaracionVar):

                            #print("entro instancia nodoDeclaracion Var")

                            self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="red"] \n'

                            self.ast += '\t' + str(id_nodo) + ' [color="red"]\n'

                            self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                            self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                        if isinstance(p4, nodoDeclaracionFun) :

                            #print("entro isinstance nodoDeclaracionFun")

                            self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="red"] \n'

                            self.ast += '\t' + str(id_nodo) + ' [color="red"]\n'

                            self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                            self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                        if isinstance(p4, nodoParam) :

                            #print("entro instancia nodoParam")

                            self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="red"] \n'

                            self.ast += '\t' + str(id_nodo) + ' [color="red"]\n'

                            self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                            self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                        if isinstance(p4, nodoSentenciaComp) :

                            #print("entro instancia nodoSentenciaComp")

                            self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="red"] \n'

                            self.ast += '\t' + str(id_nodo) + ' [color="red"]\n'

                            self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                            self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                        if isinstance(p4, nodoExpresion) :

                            #print("entro instancia nodoExpresion")

                            self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="red"] \n'

                            self.ast += '\t' + str(id_nodo) + ' [color="red"]\n'

                            self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                            self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                        if isinstance(p4, nodoSentenciaSeleccion) :

                            #print("entro instancia nodoSentenciaSeleccion")

                            self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="red"] \n'

                            self.ast += '\t' + str(id_nodo) + ' [color="red"]\n'

                            self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                            self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'


                        if isinstance(p4, nodoSentenciaIteracion) :

                            #print("entro instancia nodoSentenciaIteracion")

                            self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="red"] \n'

                            self.ast += '\t' + str(id_nodo) + ' [color="red"]\n'

                            self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                            self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                        if isinstance(p4, nodoSentenciaRetorno) :

                            #print("entro instancia nodoSentenciaRetorno")

                            self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="red"] \n'

                            self.ast += '\t' + str(id_nodo) + ' [color="red"]\n'

                            self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                            self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'


                        if isinstance(p4, nodoBinarioOP) :

                            #print("entro instancia nodoBinarioOP")

                            self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="red"] \n'

                            self.ast += '\t' + str(id_nodo) + ' [color="red"]\n'

                            self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                            self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                        if isinstance(p4, nodoInvocacion) :

                           #print("entro instancia nodoInvocacion")

                            self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="red"] \n'

                            self.ast += '\t' + str(id_nodo) + ' [color="red"]\n'

                            self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                            self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                    else:

                        if isinstance(p4,nodoDeclaracionVar) or \
                            isinstance(p4, nodoDeclaracionFun) or \
                            isinstance(p4, nodoParam) or \
                            isinstance(p4, nodoSentenciaComp) or \
                            isinstance(p4, nodoExpresion) or \
                            isinstance(p4, nodoSentenciaSeleccion) or \
                            isinstance(p4, nodoSentenciaIteracion) or \
                            isinstance(p4, nodoSentenciaRetorno) or \
                            isinstance(p4, nodoBinarioOP) or \
                            isinstance(p4, nodoInvocacion) or \
                            isinstance(p4, nodoNUM) or \
                            isinstance(p4, nodoVar):

                            self.id_nodo += 1
                            id_nodo = self.id_nodo

                            self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="green"] \n'

                            self.ast += '\t' + str(id_nodo) + ' [color="green"]\n'

                            self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                            self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'

                        else:

                            self.id_nodo += 1
                            id_nodo = self.id_nodo

                            self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="yellow"] \n'

                            self.ast += '\t' + str(id_nodo) + ' [color="yellow"]\n'

                            self.ast += '\t' + str(id_nodo) + ' [label="' + x + '"]\n'

                            self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'


                else:

                    if x.nombre == "vacio":

                        #self.id_nodo += 1
                        #id_nodo = self.id_nodo

                        self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="green"] \n'

                        #self.id_nodo += 1
                        #id_nodo = self.id_nodo

                        #self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="yellow"] \n'
                        #self.ast += '\t' + str(id_nodo) + ' [color="yellow"]\n'

                        #self.ast += '\t' + str(id_nodo) + ' [label="' + x.nombre + '"]\n'
                        #self.ast += '\t"' + p3 + str(p2) + '" ' + '-> ' + str(id_nodo) + '\n'
                        pass

                    else:

                        #self.ast += '\t"' + p3 + str(p2) + '" ' + ' [color="green"] \n'
                        self.ast += '\t"' + p3 + str(p2) + '" ' + '-> '
                        x.accept(self)


    def visit_programa(self, programa):

        self.id_program += 1
        id_program = self.id_program

        self.ast += 'digraph G { ratio = fill; node [style=filled]; \n'

        self.ast += '\t"Programa ' + str(id_program) + '" [color="blue"] \n'

        self.manyTimes(programa.lista_decl_p,id_program,programa.nombre,programa)

        self.ast += '}'


    def visit_nodoDeclaracionVar(self,declaracion_var_p):


        self.id_declaracion_var+= 1
        id_declaracion_var = self.id_declaracion_var

        self.ast += '"Declaracion Var ' + str(id_declaracion_var) + '"' + '\n'

        if declaracion_var_p.thereis_num == False:

            self.manyTimes(declaracion_var_p.def_tipo_p, id_declaracion_var, declaracion_var_p.nombre,declaracion_var_p)
            self.manyTimes(declaracion_var_p.ID_t, id_declaracion_var, declaracion_var_p.nombre,declaracion_var_p)

        else:

            self.manyTimes(declaracion_var_p.def_tipo_p, id_declaracion_var, declaracion_var_p.nombre,declaracion_var_p)
            self.manyTimes(declaracion_var_p.ID_t, id_declaracion_var, declaracion_var_p.nombre,declaracion_var_p)
            self.manyTimes(declaracion_var_p.NUM_t, id_declaracion_var,declaracion_var_p.nombre,declaracion_var_p)



    def visit_nodoDeclaracionFun(self,declaracion_fun_p):

        # completar
        self.id_declaracion_fun +=1
        id_declaracion_fun = self.id_declaracion_fun

        self.ast += '"Declaracion Fun ' + str(id_declaracion_fun) + '"' + '\n'

        self.manyTimes(declaracion_fun_p.def_tipo_p,id_declaracion_fun,declaracion_fun_p.nombre,declaracion_fun_p)
        self.manyTimes(declaracion_fun_p.ID_t,id_declaracion_fun,declaracion_fun_p.nombre,declaracion_fun_p)
        self.manyTimes(declaracion_fun_p.parametros_p,id_declaracion_fun,declaracion_fun_p.nombre,declaracion_fun_p)
        self.manyTimes(declaracion_fun_p.sentencia_comp_p,id_declaracion_fun,declaracion_fun_p.nombre,declaracion_fun_p)


    def visit_nodoParam(self,param_p):


        self.id_nodoParam += 1
        id_nodoParam = self.id_nodoParam

        self.ast += '"Param ' + str(id_nodoParam) + '"' + '\n'

        if param_p.thereis_ID == False:

            self.manyTimes(param_p.def_tipo_p,id_nodoParam,param_p.nombre,param_p)

        else:

            self.manyTimes(param_p.def_tipo_p, id_nodoParam, param_p.nombre,param_p)
            self.manyTimes(param_p.ID_t, id_nodoParam, param_p.nombre,param_p)


    def visit_nodoVacio(self,vacio_t):

        self.id_nodoVacio += 1
        id_nodoVacio = self.id_nodoVacio

        self.ast += '"Nodo Vacio ' + str(id_nodoVacio) + '"' + '\n'

        self.manyTimes(vacio_t.vacio_t,id_nodoVacio,vacio_t.nombre,vacio_t)

    def visit_nodoSentenciaComp(self,sentencia_comp_p):


        self.id_sentencia_comp +=1

        id_sentencia_comp = self.id_sentencia_comp

        self.ast += '"Sentencia Comp ' + str(id_sentencia_comp) + '"' + '\n'


        self.manyTimes(sentencia_comp_p.declaraciones_locales_p,id_sentencia_comp,sentencia_comp_p.nombre,sentencia_comp_p)
        self.manyTimes(sentencia_comp_p.lista_sentencias_p, id_sentencia_comp, sentencia_comp_p.nombre,sentencia_comp_p)

    def visit_nodoSentenciaSeleccion(self,sentencia_seleccion_p):


        self.id_nodoSentenciaSeleccion += 1
        id_nodoSentenciaSeleccion = self.id_nodoSentenciaSeleccion

        self.ast += '"Sentencia Seleccion ' + str(id_nodoSentenciaSeleccion) + '"' + '\n'


        if sentencia_seleccion_p.is_else == False:

            self.manyTimes(sentencia_seleccion_p.expresion_p, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre,sentencia_seleccion_p)
            self.manyTimes(sentencia_seleccion_p.sentencia_p, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre,sentencia_seleccion_p)

        else:

            self.manyTimes(sentencia_seleccion_p.expresion_p, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre,sentencia_seleccion_p)
            self.manyTimes(sentencia_seleccion_p.sentencia_p, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre,sentencia_seleccion_p)
            self.manyTimes(sentencia_seleccion_p.sentencia_p2, id_nodoSentenciaSeleccion, sentencia_seleccion_p.nombre,sentencia_seleccion_p)


    def visit_nodoSentenciaIteracion(self,sentencia_iteracion_p):

        self.id_nodoSentenciaIteracion += 1
        id_nodoSentenciaIteracion = self.id_nodoSentenciaIteracion

        self.ast += '"Sentencia Iteracion ' + str(id_nodoSentenciaIteracion) + '"' + '\n'

        if sentencia_iteracion_p.thereis_expresion == True and sentencia_iteracion_p.thereis_sentencia == True:

            self.manyTimes(sentencia_iteracion_p.expresion_p, id_nodoSentenciaIteracion, sentencia_iteracion_p.nombre,sentencia_iteracion_p)
            self.manyTimes(sentencia_iteracion_p.sentencia_p, id_nodoSentenciaIteracion, sentencia_iteracion_p.nombre,sentencia_iteracion_p)

        if sentencia_iteracion_p.thereis_sentencia_comp == True:


            self.manyTimes(sentencia_iteracion_p.rep, id_nodoSentenciaIteracion, sentencia_iteracion_p.nombre,sentencia_iteracion_p)
            self.manyTimes(sentencia_iteracion_p.sentencia_comp_p, id_nodoSentenciaIteracion, sentencia_iteracion_p.nombre,sentencia_iteracion_p)


    def visit_nodoSentenciaRetorno(self,sentencia_retorno_p):

        self.id_nodoSentenciaRetorno += 1
        id_nodoSentenciaRetorno = self.id_nodoSentenciaRetorno

        self.ast += '"Sentencia Retorno ' + str(id_nodoSentenciaRetorno) + '"' + '\n'

        if sentencia_retorno_p.thereis_expression == True:

            self.manyTimes(sentencia_retorno_p.nombre3, id_nodoSentenciaRetorno, sentencia_retorno_p.nombre,sentencia_retorno_p)

            self.manyTimes(sentencia_retorno_p.expresion_p,id_nodoSentenciaRetorno,sentencia_retorno_p.nombre,sentencia_retorno_p)

        else:

            self.manyTimes(sentencia_retorno_p.nombre2, id_nodoSentenciaRetorno, sentencia_retorno_p.nombre,sentencia_retorno_p)


    def visit_nodoExpresion(self,expresion_p):

        self.id_nodoExpresion += 1
        id_nodoExpresion = self.id_nodoExpresion

        self.ast += '"Expresion ' + str(id_nodoExpresion) + '"' + '\n'


        if expresion_p.var_p is not None and expresion_p.expresion_p is not None:

            self.manyTimes(expresion_p.var_p, id_nodoExpresion, expresion_p.nombre,expresion_p)
            self.manyTimes(expresion_p.assign, id_nodoExpresion, expresion_p.nombre,expresion_p)
            self.manyTimes(expresion_p.expresion_p, id_nodoExpresion, expresion_p.nombre,expresion_p)

        else:

            if expresion_p.expresion_p:

                self.manyTimes(expresion_p.expresion_p,id_nodoExpresion,expresion_p.nombre,expresion_p)

            else:

                self.manyTimes(expresion_p.semicolon_t, id_nodoExpresion, expresion_p.nombre,expresion_p)


    def visit_nodoVar(self,var_p):

        self.id_nodoVar += 1
        id_nodoVar = self.id_nodoVar

        self.ast += '"Var ' + str(id_nodoVar) + '"' + '\n'

        if var_p.is_vec_access == False and var_p.expresion_p == None:

            self.manyTimes(var_p.ID_t, id_nodoVar, var_p.nombre,var_p)

        else:

            self.manyTimes(var_p.ID_t, id_nodoVar, var_p.nombre,var_p)
            self.manyTimes(var_p.expresion_p, id_nodoVar, var_p.nombre,var_p)

    def visit_nodoExpresionLogica(self,expresion_logica_p):


        self.id_nodoExpresionLogica += 1
        id_nodoExpresionLogica = self.id_nodoExpresionLogica

        self.ast += '"Expresion Logica ' + str(id_nodoExpresionLogica) + '"' + '\n'

        if expresion_logica_p.thereis_exp_log == True:

            self.manyTimes(expresion_logica_p.expresion_logica_p, id_nodoExpresionLogica, expresion_logica_p.nombre,expresion_logica_p)
            self.manyTimes(expresion_logica_p.expresion_simple_p, id_nodoExpresionLogica, expresion_logica_p.nombre,expresion_logica_p)

        else:

            self.manyTimes(expresion_logica_p.expresion_simple_p, id_nodoExpresionLogica, expresion_logica_p.nombre,expresion_logica_p)

    def visit_nodoBinarioOP(self,nodoBinarioOP_p):


        self.id_nodoBinarioOP += 1
        id_nodoBinarioOP = self.id_nodoBinarioOP

        self.ast += '"Nodo Binario Op ' + str(id_nodoBinarioOP) + '"' + '\n'

        if nodoBinarioOP_p.is_rama == False:

            self.manyTimes(nodoBinarioOP_p.ramaDer_p, id_nodoBinarioOP, nodoBinarioOP_p.nombre,nodoBinarioOP_p)

        else:

            self.manyTimes(nodoBinarioOP_p.ramaIzq_p, id_nodoBinarioOP, nodoBinarioOP_p.nombre,nodoBinarioOP_p)
            self.manyTimes(nodoBinarioOP_p.operacion_p, id_nodoBinarioOP, nodoBinarioOP_p.nombre,nodoBinarioOP_p)
            self.manyTimes(nodoBinarioOP_p.ramaDer_p, id_nodoBinarioOP, nodoBinarioOP_p.nombre,nodoBinarioOP_p)


    def visit_nodoNUM(self,nodoNum_p):


        self.id_nodoNum += 1
        id_nodoNum = self.id_nodoNum

        self.ast += '"NUM ' + str(id_nodoNum) + '"' + '\n'

        self.manyTimes(nodoNum_p.NUM_t, id_nodoNum, nodoNum_p.nombre,nodoNum_p)


    def visit_nodoInvocacion(self,invocacion_p):

        self.id_nodoInvocacion += 1
        id_nodoInvocacion = self.id_nodoInvocacion

        self.ast += '"Invocacion ' + str(id_nodoInvocacion) + '"' + '\n'

        self.manyTimes(invocacion_p.ID_t, id_nodoInvocacion, invocacion_p.nombre,invocacion_p)
        self.manyTimes(invocacion_p.argumentos_p, id_nodoInvocacion, invocacion_p.nombre,invocacion_p)
