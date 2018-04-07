import ply.lex as lex
import ply.yacc as yacc
import sys

aprobado = True

dir_func = {}

pOper = []
pType = []
pilaO = []
quad = []
pJumps = []
cont = 0
contQuads = 0
contParam = 0
funcToCall = ''


actual_scope = 'global'

dir_func[actual_scope] = { 'type' : 'void', 'scope' : {}, 'numParams' : 0, 'quadStart' : -1}




def add_pilaO(id):
    pilaO.append(id)

def add_pOper(oper):
    pOper.append(oper)

def add_pType(type):
    pType.append(type)

def add_pJumps(quad):
	pJumps.append(quad)

def pop_pilaO():
    if (len(pilaO) > 0):
        return pilaO.pop()

def pop_pOper():
    if (len(pOper) > 0):
        return pOper.pop()

def pop_pType():
    if (len(pType) > 0):
        return pType.pop()

def pop_pJumps():
	if (len(pJumps) > 0):
		return pJumps.pop()


def top_pOper():
    if (len(pOper) > 0):
        temp = pop_pOper()
        add_pOper(temp)
        return temp
    else:
        return -1


def add_quad(operator,leftOperand,rightOperand,result):
	quad.append({'operator':operator,'leftOperand':leftOperand,'rightOperand':rightOperand,'result':result})
	global contQuads
	contQuads = contQuads + 1

add_quad('GOTO', '','','')

def updateQuad(i, llave, val):
	(quad[i])[llave] = val




def semantic_check(lOP_type,rOP_type,oper):
    if lOP_type in sem_cube:
        if rOP_type in sem_cube[lOP_type]:
            if oper in sem_cube[lOP_type][rOP_type]:
                return sem_cube[lOP_type][rOP_type][oper]
    return 'error'

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

sem_cube = {'NUM' : 	{ 'NUM' : { '+': 'NUM',
                                    '-': 'NUM',
                                    '/': 'FLOT',
                                    '*': 'NUM',
                                    '%': 'NUM',
                                    '<': 'BOOL',
                                    '>': 'BOOL',
                                    '<=': 'BOOL',
                                    '>=': 'BOOL',
                                    '!=': 'BOOL',
                                    '==': 'BOOL',
                                    '=': 'NUM'},
                          'FLOT': {'+': 'FLOT',
                                    '-': 'FLOT',
                                    '/': 'FLOT',
                                    '*': 'FLOT',
                                    '%': 'FLOT',
                                    '<': 'BOOL',
                                    '>': 'BOOL',
                                    '<=': 'BOOL',
                                    '>=': 'BOOL',
                                    '!=': 'BOOL',
                                    '==': 'BOOL',
                                    '=': 'NUM'}},
                 'FLOT' : {'NUM' : {'+': 'FLOT',
                                    '-': 'FLOT',
                                    '/': 'FLOT',
                                    '*': 'FLOT',
                                    '%': 'FLOT',
                                    '<': 'BOOL',
                                    '>': 'BOOL',
                                    '<=': 'BOOL',
                                    '>=': 'BOOL',
                                    '!=': 'BOOL',
                                    '==': 'BOOL',
                                     '=': 'FLOT'},
                          'FLOT': {'+': 'FLOT',
                                    '-': 'FLOT',
                                    '/': 'FLOT',
                                    '*': 'FLOT',
                                    '%': 'FLOT',
                                    '<': 'BOOL',
                                    '>': 'BOOL',
                                    '<=': 'BOOL',
                                    '>=': 'BOOL',
                                    '!=': 'BOOL',
                                    '==': 'BOOL',
                                    '=': 'FLOT'}},
                 'BOOL' : {'BOOL' : {'AND' : 'BOOL',
                                     'OR' : 'BOOL',
                                     '=' : 'BOOL'}}}





reserved = {
	  'PROG' : 'PR_program',
	  'VAR' : 'PR_var',
	  'FUNC' : 'PR_function',
	  'RET' : 'PR_return',
	  'MAIN' : 'PR_main',
	  'KAMEF' : 'PR_kameForw',
	  'KAMEB' : 'PR_kameBack',
	  'KAMER' : 'PR_kameRot',
	  'DRAW' : 'PR_draw',
	  'CIRCLE' : 'PR_circle', 
	  'SQUARE' : 'PR_square',
	  'IF' : 'PR_if' ,
	  'ELSE' : 'PR_else',
	  'LOOP' : 'PR_loop',
	  'TRUE' : 'PR_true',
	  'FALSE' : 'PR_false',
	  'HOME' : 'PR_home' ,
	  'END' : 'PR_end',
	  'COLOR' : 'PR_color',
	  'SIZE' : 'PR_size',
	  'NOT' : 'PR_negacion',
	  'AND' : 'PR_interseccion',
	  'OR' : 'PR_union',
	  'NUM' : 'PR_num',
	  'FLOT' : 'PR_flot',
	  'BOOL' : 'PR_bool',
	  'VOID' : 'PR_void',
	  'RET' : 'PR_return',
	  'RED' : 'PR_red',
	  'GREEN' : 'PR_green',
	  'BLUE' : 'PR_blue',
	  'VIOLET' : 'PR_violet',
	  'ORANGE' : 'PR_orange',
	  'YELLOW' : 'PR_yellow',
	  'WHITE' : 'PR_white',
	  'BLACK' : 'PR_black',

}

tokens = [
	'OP_MAS', 'OP_MENOS', 'OP_MULT','OP_DIV', 'OP_RESID',
	'OP_DOBLEIGUAL','OP_IGUAL', 'OP_DIFDE', 'OP_MENORQUE', 'OP_MENOROIGUAL',
	'OP_MAYORQUE', 'OP_MAYOROIGUAL',
	'TO_PARABRE', 'TO_PARCIERRA', 'TO_LLAABRE', 'TO_LLACIERRA', 
	'TO_CORABRE', 'TO_CORCIERRA',
	'TO_DIGIT', 'TO_NUM', 'TO_FLOT', 'ID', 'TO_COMA', 'TO_UWU','TO_DOSPTOS'

]
#tokens
t_OP_MAS = r'\+'
t_OP_MENOS = r'\-'
t_OP_MULT = r'\*'
t_OP_DIV = r'\/'
t_OP_RESID = r'\%'
t_OP_DOBLEIGUAL = r'\=\='
t_OP_IGUAL = r'\='
t_OP_DIFDE = r'\!\='
t_OP_MENORQUE = r'\<'
t_OP_MENOROIGUAL = r'\<\='
t_OP_MAYORQUE = r'\>'
t_OP_MAYOROIGUAL = r'\>\='
t_TO_PARABRE = r'\('
t_TO_PARCIERRA = r'\)'
t_TO_LLAABRE = r'\{'
t_TO_LLACIERRA = r'\}'
t_TO_CORABRE = r'\['
t_TO_CORCIERRA = r'\]'
t_TO_DIGIT = r'[0-9]'
t_TO_NUM = r'[0-9]+'
t_TO_FLOT = r'[0-9]+\.[0-9]+'
t_TO_COMA = r'\,'
t_TO_UWU = r'\#\u\w\u'
t_TO_DOSPTOS = r'\:'



tokens = tokens + list(reserved.values())

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

# Caracteres ignorados
t_ignore = ' \t\n'

def t_error(t):
	

    global aprobado
    aprobado = False
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


# Construye el lexer
lex.lex()

def p_prog(p):
	'prog : PR_program TO_LLAABRE declare mainBlock TO_LLACIERRA'
	print(dir_func)
	for q in quad: print q
	#print(dir_func.get('move'))
	
def p_val(p):
	'''val : TO_NUM
			| TO_FLOT
			| PR_true
			| PR_false
			| ID'''
	
	if p[1] == 'TRUE' or p[1] == 'FALSE':
		add_pType('BOOL')
		add_pilaO(p[1])
	elif not is_number(p[1]):
		try:
			varscope = dir_func[actual_scope]['scope'][p[1]]
		except KeyError:
			varscope = dir_func['global']['scope'][p[1]]
			add_pilaO(p[1])
			add_pType(varscope.get('type'))
		else:
			add_pilaO(p[1])
			add_pType(varscope.get('type'))

	elif float(p[1]) % 1 != 0:
		add_pType('FLOT')
		add_pilaO(float(p[1]))
	else:
		add_pType('NUM')
		add_pilaO(int(p[1]))


def p_declare(p):
	'declare : decVar decFunc'
	


def p_decVar(p):
	''' decVar : var decVar 
				| empty'''
			

def p_decFunc(p):
	''' decFunc : func decFunc 
				| empty'''


def p_var(p):
	'var : PR_var tipo ID arrayCreate'
	if not p[3] in dir_func[actual_scope]['scope']:
		dir_func[actual_scope]['scope'][p[3]] = {'type' : p[2]}
	else:
		print('Variable ' + p[3] + ' ya declarada')
		sys.exit()


	#print(dir_func.get(actual_scope))
	


def p_arrayCreate(p):
	'''arrayCreate : TO_CORABRE TO_NUM TO_CORCIERRA 
				   | TO_CORABRE TO_NUM TO_CORCIERRA TO_CORABRE TO_NUM TO_CORCIERRA 
				   | empty'''

def p_arrayIndex(p):
	'''arrayIndex : TO_CORABRE exp TO_CORCIERRA 
				  | TO_CORABRE exp TO_CORCIERRA TO_CORABRE exp TO_CORCIERRA 
				  | empty'''
def p_tipo(p):
	'''tipo : PR_num 
			| PR_flot
			| PR_bool '''
	p[0] = p[1]

def p_assign(p):
	'assign : assignTo OP_IGUAL megaExp'
	varia = p[1]
	rightOperand = pop_pilaO()
	rOP_type = pop_pType()

	if varia == 'KAMER' or varia == 'KAMEF' or varia == 'KAMEB':
		print('palabra reservada, FALTA HACERLO')
	else:
		try:
			varscope = dir_func[actual_scope]['scope'][varia]
		except KeyError:
			varscope = dir_func['global']['scope'][varia]
			result_check = semantic_check(varscope.get('type'),rOP_type,'=')
			if result_check != 'error':
				add_quad('=','',rightOperand,varia)
			else:
				print("Error de tipos al asignar")
				sys.exit()
		else:
			result_check = semantic_check(varscope.get('type'),rOP_type,'=')
			if result_check != 'error':
				add_quad('=','',rightOperand,varia)
			else:
				print("Error de tipos al asignar")
				sys.exit()

		
		

def p_assignTo(p):
	'''assignTo : ID arrayIndex
				| PR_kameForw
				| PR_kameBack
				| PR_kameRot'''

	p[0] = p[1]


def p_func(p):
	'func : func1 func2'


def p_func1(p):
	'func1 : func11 func12'


def p_func11(p):
	'func11 : PR_function decideType ID TO_PARABRE'

	if not p[3] in dir_func:
		global actual_scope
		actual_scope = p[3]
		dir_func[p[3]] = { 'type' : p[2], 'scope' : {}, 'numParams' : 0, 'quadStart' : contQuads }
	else:
		print("Funcion " + p[3] +" ya declarada")
		sys.exit()

def p_func12(p):
	'func12 : params TO_PARCIERRA TO_LLAABRE'

def p_func2(p):
	'func2 : decVar bloque TO_LLACIERRA'
	add_quad('ENDPROC','','','')

def p_decideType(p):
	'''decideType : tipo 
				  | PR_void'''
	p[0] = p[1]


def p_params(p):
	'''params : tipo ID moreParams
			  | empty'''
	if len (p) > 2:
		dir_func[actual_scope]['scope'][p[2]] = {'type' : p[1]}
		dir_func[actual_scope]['numParams'] = dir_func[actual_scope]['numParams'] + 1

def p_moreParams(p):
	'''moreParams : TO_COMA tipo ID moreParams 
			  | empty'''
	if len(p) > 2:
		dir_func[actual_scope]['scope'][p[3]] = {'type' : p[2]}
		dir_func[actual_scope]['numParams'] = dir_func[actual_scope]['numParams'] + 1
def p_mainBlock(p):
	'mainBlock : mainBlock1 bloque TO_LLACIERRA'

def p_mainBlock1(p):
	'mainBlock1 : PR_main TO_LLAABRE'
	actual_scope = 'main'
	dir_func[p[1]] = {'type' : 'void', 'scope' : {}}
	updateQuad(0,'result', contQuads)
	#print(dir_func.get('move'))

def p_opLogico(p):
	'''opLogico : PR_interseccion 
				| PR_union'''
	if len(p) > 1:
		add_pOper(p[1])
		#print(pOper)
		


def p_loop(p):
	'loop : loop1 loop2 loop3'
	fin = pop_pJumps()
	inicio = pop_pJumps()
	add_quad('+','iterator','1','iterator')
	add_quad('GOTO', '','',inicio)
	global contQuads
	updateQuad(fin,'result',contQuads)

def p_loop1(p):
	'loop1 : PR_loop'
	add_pJumps(contQuads)

def p_loop2(p):
	'loop2 : TO_PARABRE exp TO_PARCIERRA'
	exp_type = pop_pType()
	if exp_type == 'NUM':
		resultado = pop_pilaO()
		global cont
		cont = cont + 1
		add_quad('<=','iterator',resultado,cont)
		add_quad('GOTOF',cont,'','')
		global contQuads
		add_pJumps(contQuads - 1)
	else:
		print('Error de tipo en LOOP')
		sys.exit()

def p_loop3(p):
	'loop3 : TO_LLAABRE bloque TO_LLACIERRA'

def p_opRelacional(p):
		'''opRelacional : OP_DOBLEIGUAL 
						| OP_DIFDE 
						| OP_MENORQUE 
						| OP_MENOROIGUAL 
						| OP_MAYORQUE 
						| OP_MAYOROIGUAL'''

		if len(p) > 1:
			add_pOper(p[1])
			

def p_bloque(p):
	'''bloque : estructura bloque 
			  | TO_UWU'''

def p_estructura(p):
	'''estructura : assign 
				  | loop 
				  | comparacion
				  | return 
				  | funcCall 
				  | decVar'''


def p_funcCall(p):
	'''funcCall : funcCall1 funcCall2
				| PR_draw TO_PARABRE megaExp TO_PARCIERRA 
				| PR_circle TO_PARABRE exp TO_PARCIERRA 
				| PR_square TO_PARABRE exp TO_PARCIERRA 
				| PR_size TO_PARABRE exp TO_PARCIERRA 
				| PR_color TO_PARABRE colorChoice TO_PARCIERRA '''
def p_funcCall1(p):
	'funcCall1 : ID TO_PARABRE'
	if p[1] in dir_func:
		print('si existo')
		add_quad('ERA',p[1],'','')
		global funcToCall
		funcToCall = p[1]
	else:
		print('Error la funcion ' + p[1] + ' no existe')
		sys.exit()	

def p_funcCall2(p):
	'funcCall2 : paramVals TO_PARCIERRA'
	if contParam == dir_func[funcToCall].get('numParams'):
		add_quad('GOSUB',funcToCall,'','')
	else:
		print('Error en el numero de parametros de ' + funcToCall)
		sys.exit()

def p_bool(p):
	'''bool : PR_true 
			| PR_false'''

def p_colorChoice(p):
	'''colorChoice : PR_red 
				   | PR_green
				   | PR_blue 
				   | PR_violet 
				   | PR_orange 
				   | PR_yellow 
				   | PR_white 
				   | PR_black'''

def p_paramVals(p):
	'''paramVals : unParam moreParamVals 
				 | empty'''

def p_moreParamVals(p):
	'''moreParamVals : TO_COMA unParam moreParamVals 
				 	 | empty'''

def p_unParam(p):
	'unParam : ID TO_DOSPTOS  megaExp'
	global funcToCall
	val = pop_pilaO()
	valType = pop_pType()
	funcTable = dir_func[funcToCall]
	try:
		result = semantic_check(funcTable['scope'][p[1]].get('type'),valType, '=')
	except KeyError:
		print('Error parametro ' + p[1] + ' no existe para la funcion ' + funcToCall )
		sys.exit()
	if result != 'error':
		global contParam
		contParam = contParam + 1
		print('Aqui es memoria')
		add_quad('PARAM', val, '',funcToCall + ':' + p[1])

	else:
		print('Error de tipo al enviar parametro ' + p[1])
		sys.exit()


def p_return(p):
	'return : PR_return megaExp'

def p_comparacion(p):
	'comparacion : compara1 compara2'


def p_compara1(p):
	'compara1 : PR_if TO_PARABRE megaExp TO_PARCIERRA TO_LLAABRE'
	exp_type = pop_pType()
	if exp_type == 'BOOL':
		global contQuads
		resultado = pop_pilaO()
		add_quad('GOTOF', resultado, '', '')
		add_pJumps(contQuads - 1)
	else:
		print('Error de tipo en IF')
		sys.exit()

def p_compara2(p):
	'compara2 : bloque TO_LLACIERRA maybeElse'
	fin = pop_pJumps()
	global contQuads
	updateQuad(fin,'result',contQuads)


def p_maybeElse(p):
	'''maybeElse : checkElse doElse 
				 | empty'''
	

def p_checkElse(p):
	'checkElse : PR_else TO_LLAABRE'
	add_quad('GOTO','','','')
	falso = pop_pJumps()
	global contQuads
	add_pJumps(contQuads - 1)
	updateQuad(falso,'result',contQuads)


def p_doElse(p):
	'doElse : bloque TO_LLACIERRA'

def p_megaExp(p):
	'megaExp : maybeNot superExp anotherMega'
	top = top_pOper()
	if top == 'OR' or top == 'AND' or top == 'NOT':
		rightOperand = pop_pilaO()
		rOP_type = pop_pType()
		operator = pop_pOper()
		global cont
		cont = cont + 1
		if operator == 'NOT':
			if rOP_type == 'BOOL':
				add_quad(operator,'',rightOperand,cont)
				add_pilaO(cont)
				add_pType('BOOL')
			else:
				print('Error de tipo en negacion')
				sys.exit()
		else:
			leftOperand = pop_pilaO()
			lOP_type = pop_pType()
			result_type = semantic_check(lOP_type, rOP_type, operator)
			if result_type != 'error':
				add_quad(operator,leftOperand,rightOperand,cont)
				add_pilaO(cont)
				add_pType(result_type)
				#for q in quad: print q
				#print(pType)
			else:
				print('Error de tipo en una comparacion')
				sys.exit()


def p_maybeNot(p):
	'''maybeNot : PR_negacion 
				| empty'''
	if p[1] == 'NOT':
		add_pOper(p[1])
		#print(pOper)	

def p_anotherMega(p):
	'''anotherMega : opLogico megaExp 
				   | empty'''

def p_superExp(p):
	'superExp : exp maybeRel'


def p_maybeRel(p):
	'''maybeRel : opRelacional exp 
				| empty'''
	top = top_pOper()
	
	if top == '>' or top == '<' or top == '>=' or top == '<=' or top == '!=' or top == '==':
		rightOperand = pop_pilaO()
		rOP_type = pop_pType()
		leftOperand = pop_pilaO()
		lOP_type = pop_pType()
		operator = pop_pOper()
		result_type = semantic_check(lOP_type, rOP_type, operator)
		if result_type != 'error':
			global cont
			cont = cont + 1
			add_quad(operator,leftOperand,rightOperand,cont)
			add_pilaO(cont)
			add_pType(result_type)
			#for q in quad: print q
			#print(pType)
		else:
			print('Error de tipo en una comparacion')
			sys.exit()

def p_exp(p):
	'exp : term anotherExp'

	top = top_pOper()
	if top == '+' or top == '-':
		rightOperand = pop_pilaO()
		rOP_type = pop_pType()
		leftOperand = pop_pilaO()
		lOP_type = pop_pType()
		operator = pop_pOper()
		result_type = semantic_check(lOP_type, rOP_type, operator)
		if result_type != 'error':
			global cont
			cont = cont + 1
			add_quad(operator,leftOperand,rightOperand,cont)
			add_pilaO(cont)
			add_pType(result_type)
			#for q in quad: print q
			#print(pType)
		else:
			print('Error de tipo en una suma o resta')
			sys.exit()





def p_anotherExp(p):
	'''anotherExp : OP_MAS exp 
				  | OP_MENOS exp 
				  | empty'''
	if len(p) > 2:
		add_pOper(p[1])		


def p_term(p):
	'term : fact anotherTerm'

	top = top_pOper()
	if top == '*' or top == '/' or top == '%':
		rightOperand = pop_pilaO()
		rOP_type = pop_pType()
		leftOperand = pop_pilaO()
		lOP_type = pop_pType()
		operator = pop_pOper()
		result_type = semantic_check(lOP_type, rOP_type, operator)
		if result_type != 'error':
			global cont
			cont = cont + 1
			add_quad(operator,leftOperand,rightOperand,cont)
			add_pilaO(cont)
			add_pType(result_type)
			#for q in quad: print q
			#print(pType)
		else:
			print('Error de tipo en una multiplicacion, division o modulo')
			sys.exit()

def p_anotherTerm(p):
	'''anotherTerm : OP_MULT term 
				   | OP_DIV term
				   | OP_RESID term
				   | empty'''
	if len(p) > 2:
		add_pOper(p[1])
	

def p_fact(p):
	'''fact : TO_PARABRE megaExp TO_PARCIERRA 
			| ID arrayIndex 
			| val'''
	


def p_empty(p):
    'empty :'


def p_error(p):
    global aprobado
    aprobado = False
    print("Error de sintaxis en '%s'" % p.value)
    sys.exit()





parser = yacc.yacc()





archivo = sys.argv[1]
f = open(archivo, 'r')
s = f.read()
parser.parse(s)


if aprobado == True:
    print("Archivo aprobado")
    sys.exit()
else: 
    print("Archivo no aprobado")
    sys.exit()