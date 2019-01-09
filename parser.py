# coding=utf-8
import ply.yacc as yacc

from scanner import tokens

from AST_visitor import *

from nodos import *

from os import listdir

import os.path

es = []

def p_programa(p):
    #Regla 1: programa =>  lista-decl
    """programa : lista_decl """
    #print("programa\n")
    p[0] = programa(p[1])

#-------------------------------------------------------------------

def p_lista_decl(p):
    #Regla 2: lista-decl => lista-decl declaracion | declaracion
    """lista_decl : lista_decl declaracion
                    | declaracion
    """
    #print("lista-decl\n")
    if len(p) == 3:

        if isinstance(p[1], list):
            p[0] = p[1]
            #print(p[0])
        else:
            p[0] = [p[1]]

            #print(p[0])

        if isinstance(p[2], list):
            p[0].extend(p[2])
        else:
            p[0].extend([p[2]])

    else:

        p[0] = p[1]

#-------------------------------------------------------------------

def p_declaracion(p):
    #Regla 3: declaracion => declaracion_var | declaracion_fun
    """declaracion : declaracion_var
                    | declaracion_fun
    """
    #print("declaracion")
    p[0] = [p[1]]

#-------------------------------------------------------------------

def p_declaracion_var(p):
    #Regla 4: declaracion_var => def_tipo ID SEMICOLON | def_tipo ID LTCOMMENT NUM RTCOMMENT SEMICOLON
    """declaracion_var : def_tipo ID SEMICOLON
                        | def_tipo ID LTCOMMENT NUM RTCOMMENT SEMICOLON
    """
    if len(p) == 4:

        p[0] = nodoDeclaracionVar(p[1],p[2])

    else:

        p[0] = nodoDeclaracionVar(p[1], p[2], thereis_num=True, NUM_t=p[4])

#-------------------------------------------------------------------

def p_def_tipo(p):
    #Regla 5 def_tipo => VACUO | ENT
    """def_tipo : VACUO
                 | ENT
    """
    #print("def_tipo")
    p[0] = [p[1]]

#-------------------------------------------------------------------

def p_declaracion_fun(p):
    #Regla 6 declaracion_fun => def_tipo ID LBRACKET parametros RBRACKET sentencia_comp
    """declaracion_fun : def_tipo ID LBRACKET parametros RBRACKET sentencia_comp"""
    #print("declaracion_fun")
    p[0] = nodoDeclaracionFun(p[1],p[2],p[4],p[6])

#-------------------------------------------------------------------

def p_parametros(p):
    #Regla 7 parametros => lista_parametros | VACUO
    """parametros : lista_parametros
                    | VACUO
    """
    if p[1] == "VACUO":

        p[0] = [nodoParam(def_tipo_p=p[1])]

    else:

        p[0] = p[1]

#-------------------------------------------------------------------

def p_lista_parametros(p):
    #Regla 8 lista_parametros => lista_parametros COMMA param | param
    """lista_parametros : lista_parametros COMMA param
                         | param
    """
    #print("lista_parametros")
    if len(p) == 4:

        if isinstance(p[1], list):
            p[0] = p[1]
        else:
            p[0] = [p[1]]

        if isinstance(p[3], list):
            p[0].extend(p[3])
        else:
            p[0].extend([p[3]])
    else:

        p[0] = [p[1]]

#-------------------------------------------------------------------

def p_param(p):
    #Regla 9 param => def_tipo ID | def_tipo ID LTCOMMENT RTCOMMENT
    """param : def_tipo ID
                | def_tipo ID LTCOMMENT RTCOMMENT
    """
    #print("param")
    if len(p) == 3:
        p[0] = nodoParam(p[1],thereis_ID=True, ID_t= p[2])

    else:

        p[0] = nodoParam(p[1], thereis_ID=True, ID_t=p[2], Lt_Rt='<>')

#-------------------------------------------------------------------

def p_sentencia_comp(p):
    #Regla 10 sentencia_comp => LPARENT declaraciones_locales lista_sentencias RPARENT
    """sentencia_comp : LPARENT declaraciones_locales lista_sentencias RPARENT"""

    #print("sentencia_comp")

    p[0] = nodoSentenciaComp(p[2],p[3])

#-------------------------------------------------------------------

def p_declaraciones_locales(p):
    #Regla 11 declaraciones_locales => declaraciones_locales declaracion_var | vacio
    """declaraciones_locales : declaraciones_locales declaracion_var
                                | vacio
    """
    #print("declaraciones_locales")
    if len(p) == 3:
        if isinstance(p[1], list):
            p[0] = p[1]
        else:
            p[0] = [p[1]]

        if isinstance(p[2], list):
            p[0].extend(p[2])
        else:
            p[0].extend([p[2]])
    else:
        p[0] = [p[1]]

#-------------------------------------------------------------------

def p_lista_sentencias(p):
    #Regla 12
    """lista_sentencias : lista_sentencias sentencia
                            | vacio
    """
    #print("lista_sentencias")
    if len(p) == 3:

        if isinstance(p[1], list):
            p[0] = p[1]
        else:
            p[0] = [p[1]]
            #p[0] = nodos.nodoVacio(is_vacio=True, vacio_t=p[1])
        if isinstance(p[2], list):
            p[0].extend(p[2])
        else:
            p[0].extend([p[2]])

    else:

        p[0] = [p[1]]

#-------------------------------------------------------------------

def p_sentencia(p):
    #Regla 13 sentencia => sentencia_expr | sentencia_comp | sentencia_seleccion | sentencia_iteracion | sentencia_retorno
    """sentencia : sentencia_expr
                    | sentencia_comp
                    | sentencia_seleccion
                    | sentencia_iteracion
                    | sentencia_retorno
    """
    p[0] = p[1]

#-------------------------------------------------------------------

def p_sentencia_expr(p):
    #Regla 14
    """sentencia_expr : expresion SEMICOLON
                        | SEMICOLON
    """
    #p[0] = p[1]

    if len(p) == 3:

        #p[0] = nodoExpresion(expresion_p=p[1],thereisExpresion=True)
        p[0] = p[1]

    else:

        p[0] = nodoExpresion(semicolon_t=p[1],thereisSemicolon=True)

#-------------------------------------------------------------------

def p_sentencia_seleccion(p):
    #Regla 15
    """sentencia_seleccion : SI LBRACKET expresion RBRACKET sentencia
                            | SI LBRACKET expresion RBRACKET sentencia SINO sentencia
    """

    if len(p) == 6:

        p[0] = nodoSentenciaSeleccion(p[3],p[5])

    else:

        p[0] = nodoSentenciaSeleccion(p[3], p[5], is_else=True, sentencia_p2=p[7])

#-------------------------------------------------------------------

def p_sentencia_iteracion(p):
    #Regla 16
    """sentencia_iteracion : MIENTRAS LBRACKET expresion RBRACKET sentencia
                            | REP sentencia_comp
    """

    if len(p) == 6:

        p[0] = nodoSentenciaIteracion(thereis_expresion=True, expresion_p= p[3], thereis_sentencia=True,sentencia_p = p[5])

    else:

        p[0] = nodoSentenciaIteracion(thereis_sentencia_comp=True, sentencia_comp_p=p[2],rep=p[1])

#-------------------------------------------------------------------

def p_sentencia_retorno(p):
    #Regla 17
    """sentencia_retorno : RET SEMICOLON
                            | RET expresion SEMICOLON
    """

    if len(p) == 3:

        p[0] = nodoSentenciaRetorno()

    else:

        p[0] = nodoSentenciaRetorno(thereis_expression=True, expresion_p=p[2])
        #p[0] = p[2]

#-------------------------------------------------------------------

def p_expresion(p):
    #Regla 18
    """expresion : var ASSIGN expresion
                    | expresion_negada
    """

    if len(p) == 4:

        p[0] = nodoExpresion(var_p=p[1],thereIsVar=True,expresion_p=p[3],thereisExpresion=True,assign=p[2])

    else:

        #p[0] = nodoExpresion(expresion_negada_p=p[1],thereisExpresionNegada=True)
        p[0] = p[1]

#-------------------------------------------------------------------

def p_var(p):
    #Regla 19
    """var : ID
            | ID LTCOMMENT expresion RTCOMMENT
    """

    if len(p) == 2:

        p[0] = nodoVar(ID_t=p[1])

    else:

        p[0] = nodoVar(ID_t=p[1], is_vec_access=True, expresion_p=p[3])

#-------------------------------------------------------------------

def p_expresion_negada(p):
    #Regla 20
    """expresion_negada : NOT LBRACKET expresion_logica RBRACKET
                            | expresion_logica
    """
    #p[0] = nodos.nodoExpresionNegada(not_bracket=True,expresion_logica_p=p[3])

    if len(p) == 5:

        #p[0] = nodoExpresionNegada(expresion_logica_p=p[3])
        p[0] = p[3]

    else:

        #p[0] = nodoExpresionNegada(expresion_logica_p=p[1])

        p[0] = p[1]

#-------------------------------------------------------------------

def p_expresion_logica(p):
    #Regla 21
    """expresion_logica : expresion_logica AND expresion_simple
                         | expresion_logica AND NOT LBRACKET expresion_simple RBRACKET
                         | expresion_simple
                         | NOT LBRACKET expresion_simple RBRACKET
    """

    if len(p) == 4:

        p[0] = nodoExpresionLogica(thereis_exp_log=True,expresion_logica_p=p[1],expresion_simple_p=p[3])

    elif len(p) == 7:

        p[0] = nodoExpresionLogica(thereis_exp_log=True, expresion_logica_p=p[1], expresion_simple_p=p[5])

    elif len(p) == 2:

        #p[0] = nodoExpresionLogica(expresion_simple_p=p[1])

        p[0] = p[1]
    else:

        #p[0] = nodoExpresionLogica(expresion_simple_p=p[3])

        p[0] = p[3]


#-------------------------------------------------------------------

def p_expresion_simple(p):
    #Regla 22
    """expresion_simple : expresion_simple relop expresion_aditiva
                            | expresion_aditiva
    """

    if len(p) == 4:

        if p[2] == "LT":
            p[0] = nodoBinarioOP(is_rama=True, ramaIzq_p=p[1], ramaDer_p=p[3], operacion_p=p[2])

        if p[2] == "EQ":
            p[0] = nodoBinarioOP(is_rama=True, ramaIzq_p=p[1], ramaDer_p=p[3], operacion_p=p[2])

    else:

        #p[0] = nodoBinarioOP(ramaDer_p=p[1], nombre2="expresion aditiva")
        p[0] = p[1]

#-------------------------------------------------------------------

def p_relop(p):
    #Regla 23
    """relop : LT
                | EQ
    """
    p[0] = p[1]

#-------------------------------------------------------------------

def p_expresion_aditiva(p):
    #Regla 24
    """expresion_aditiva : expresion_aditiva addop term
                            | term
    """
    if len(p) == 4:

        if p[2] == "+":
            # p[0] = nodos.nodoBinarioOP(p[1],p[3],"+")
            p[0] = nodoBinarioOP(is_rama=True, ramaIzq_p=p[1], ramaDer_p=p[3], operacion_p=p[2])

        if p[2] == "-":
            # p[0] = nodos.nodoBinarioOP(p[1],p[3],"-")
            p[0] = nodoBinarioOP(is_rama=True, ramaIzq_p=p[1], ramaDer_p=p[3], operacion_p=p[2])

    else:

        #p[0] = nodoBinarioOP(ramaDer_p=p[1], nombre2="term")
        p[0] = p[1]

#-------------------------------------------------------------------

def p_addop(p):
    #Regla 25
    """addop : PLUS
                | MINUS
    """
    p[0] = p[1]

#-------------------------------------------------------------------

def p_term(p):
    #Regla 26
    """term : term mulop factor
                | factor
    """
    if len(p) == 4:

        if p[2] == "++":
            # p[0] = nodos.nodoBinarioOP(p[1],p[3],"++")
            p[0] = nodoBinarioOP(is_rama=True, ramaIzq_p=p[1], ramaDer_p=p[3], operacion_p=p[2])

        if p[2] == "--":
            # p[0] = nodos.nodoBinarioOP(p[1],p[3],"--")
            p[0] = nodoBinarioOP(is_rama=True, ramaIzq_p=p[1], ramaDer_p=p[3], operacion_p=p[2])

    else:

        #p[0] = nodos.nodoBinarioOP(ramaDer_p=p[1], nombre2="factor")

        p[0] = p[1]

#-------------------------------------------------------------------

def p_mulop(p):
    #Regla 27
    """mulop : TIMES
                | DIVIDE
    """
    p[0] = p[1]

#-------------------------------------------------------------------

def p_factor(p):
    #Regla 28
    """factor : LBRACKET expresion RBRACKET
                | var
                | invocacion
    """
    #p[0] = nodoExpresion(expresion_p=p[1])
    if len(p) == 4:
        p[0] = p[2]

    else:

        p[0] = p[1]

#-------------------------------------------------------------------

def p_factor_num(p):
    # Regla 28
    """factor : NUM"""
    p[0] = nodoNUM(p[1])

#-------------------------------------------------------------------

def p_invocacion(p):
    #Regla 29
    """invocacion : ID LBRACKET argumentos RBRACKET """
    p[0] = nodoInvocacion(p[1],p[3])

#-------------------------------------------------------------------

def p_argumentos(p):
    #Regla 30
    """argumentos : lista_arg"""
    p[0] = p[1]

def p_argumentos2(p):
    #Regla 30
    """argumentos : vacio"""
    p[0] = [p[1]]

#-------------------------------------------------------------------

def p_lista_arg(p):
    #Regla 31
    """lista_arg : lista_arg COMMA expresion
                    | expresion
    """
    if len(p) == 4:

        if isinstance(p[1], list):
            p[0] = p[1]
        else:
            p[0] = [p[1]]

        if isinstance(p[3], list):
            p[0].extend(p[3])
        else:
            p[0].extend([p[3]])

    else:

        p[0] = p[1]

#-------------------------------------------------------------------

def p_vacio(p):
    'vacio : '
    #p[0] = nodos.nodoVacio()
    p[0] = nodoVacio()
    pass

#-------------------------------------------------------------------

# Errores en la sintaxis.
def p_error(p):
    print('Error de sintaxis! ')
    if p is not None:
        print('Error en el ' + str(p.type) + '\n')
    else:
        print('El archivo de entrada esta vacío\n')

def errorSemantico(errores):
    print("Error Semántico,",errores)

# Build the parser
#parser = yacc.yacc()
parser = yacc.yacc(debug=True,start="programa")


def listarArchivoPP():

    for carpeta in listdir("."):
        if carpeta.endswith(".pp"):
            print (carpeta)


def ingresarArchivo(nombreArchivo):

    treeFileDot = open('tree.dot', 'w')

    with open(nombreArchivo, 'r',encoding='utf-8') as arch:
        contents = arch.read()
        result = parser.parse(contents)
        if result is not None:
            visitor_tipos = visitor()
            programa.accept(result, visitor_tipos)
            treeFileDot.write(visitor_tipos.ast)

            st = getTable()

            scope_variables(st)
            scope_function(st)

            es1 = getesp()
            es.extend(es1)

            for e in es:

                errorSemantico(e)

            es2 = getess()
            if es2 is not None:
                for e in es2:
                    print(e)
        else:

            treeFileDot.write('Error al realizar el parse.')


def scope_variables(symbolTable):
    error_variables = True
    if len(symbolTable.getNodos()) != 0:

        nodes = symbolTable.getNodos()
        for node in nodes:
            comparation = 0
            dato = node.identificador
            for nod in nodes:
                if dato == nod.identificador and dato != "SI" and dato != "SINO" and dato != "MIENTRAS":
                    comparation += 1
            if comparation > 1 and node.getsymbolTable() is None:

                es.append("Variable " + dato   + " del tipo " + node.tipo[0] + " repetida")

            if node.getsymbolTable() is not None:
                scope_variables(node.getsymbolTable())

    return error_variables




def scope_function(symbolTable):

    error_function = True
    nodeFunction = []
    nodes = symbolTable.getNodos()
    temp = nodoST(None, None, None)
    position = 0
    comparation = 0
    for node in nodes:
        if node.getsymbolTable() is not None:
            nodeFunction.append(node)

    for i in range(len(nodeFunction)):
        temp = nodeFunction[i]
        position = i
        nodeFunction.pop(i)
        for x in nodeFunction:
            if temp.tipo == x.tipo and temp.identificador == x.identificador:
                comparation += 1
                if comparation == 2:
                    st = temp.getsymbolTable().getParam()
                    st2 = x.getsymbolTable().getParam()
                    comparation = 0
                    cont = 0
                    if len(st) == len(st2):
                        for s in range(len(st)):
                            if st[s].tipo == st2[s].tipo:
                                cont += 1
                        if len(st) == cont:
                            print(x.tipo)
                            print("x.tipo")
                            print(temp.identificador)
                            print("temp.identificador")
                            es.append("Funciones declaradas iguales " + temp.identificador)

                            break
        nodeFunction.insert(i, temp)

    return error_function

def cerrar(cerrar):

    if cerrar == "CERRAR":

        print("\nBye ! :(")

        c = False

        return c
    else:

        c = True

        return c

def main():

    global flag

    flag = True

    while flag != False:

        listarArchivoPP()

        print("\nPara salir Ingresar: CERRAR ")

        archivoNombre = input("\nIngrese el nombre del archivo a leer: ")

        flag = cerrar(archivoNombre)

        if flag == False:

            break

        while os.path.isfile(archivoNombre) == False:

            print("\nArchivo no encontrado :( ")

            # se ingresa nuevamente el nombre del archivo a buscar
            archivoNombre = input("\nIngrese el nombre del archivo a leer: ")

            flag = cerrar(archivoNombre)

            if flag == False:

                break

        if os.path.isfile(archivoNombre) == True:

            print("\nArchivo Encontrado :) \n")

            ingresarArchivo(archivoNombre)

            print("\nArchivo tree.dot Generado :) \n")


if __name__ == "__main__":

    main()








