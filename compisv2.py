import ply.lex as lex
import ply.yacc as yacc
import sys

aprobado = True

dir_func = {}

actual_scope = 'global'


cars = {'A':{'speed':70,
        'color':2},
        'B':{'speed':60,
        'color':3}}

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
	'TO_DIGIT', 'TO_NUM', 'TO_FLOT', 'ID', 'TO_COMA', 'TO_UWU'

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
	#dir_func = {'func': {'speed':70,'color':2}, 'vars':{'speed':70,'color':2}}
	
def p_val(p):
	'''val : TO_PARABRE exp TO_PARCIERRA 
			| TO_NUM
			| TO_FLOT
			| bool
			| ID'''

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
	#dir_func[actual_scope]['scope'][p[2]] = {'type' : p[1]}
	


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

def p_assignTo(p):
	'''assignTo : ID arrayIndex
				| PR_kameForw
				| PR_kameBack
				| PR_kameRot'''



def p_func(p):
	'func : PR_function decideType ID TO_PARABRE params TO_PARCIERRA TO_LLAABRE decVar bloque TO_LLACIERRA'
	actual_scope = p[3]
	dir_func[p[3]] = { 'type' : p[2], 'scope' : {}}
	print(dir_func.get(p[3]))
	# dirProced['RedRobin'] = {'func': {}, 'vars': {}, 'obj': {}, 'parent': ''}

def p_decideType(p):
	'''decideType : tipo 
				  | PR_void'''
	p[0] = p[1]


def p_params(p):
	'''params : tipo ID moreParams 
			  | empty'''

def p_moreParams(p):
	'''moreParams : TO_COMA tipo ID moreParams 
			  | empty'''

def p_mainBlock(p):
	'mainBlock : PR_main TO_LLAABRE bloque TO_LLACIERRA'
	actual_scope = p[3]
	dir_func[p[3]] = {'type' : 'void', 'scope' : {}}
	#print(dir_func.get('move'))

def p_opLogico(p):
	'''opLogico : PR_interseccion 
				| PR_union'''


def p_loop(p):
	'loop : PR_loop TO_PARABRE exp TO_PARCIERRA TO_LLAABRE bloque TO_LLACIERRA'

def p_opRelacional(p):
		'''opRelacional : OP_DOBLEIGUAL 
						| OP_DIFDE 
						| OP_MENORQUE 
						| OP_MENOROIGUAL 
						| OP_MAYORQUE 
						| OP_MAYOROIGUAL'''


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
	'''funcCall : ID TO_PARABRE paramVals TO_PARCIERRA 
				| PR_draw TO_PARABRE megaExp TO_PARCIERRA 
				| PR_circle TO_PARABRE exp TO_PARCIERRA 
				| PR_square TO_PARABRE exp TO_PARCIERRA 
				| PR_size TO_PARABRE exp TO_PARCIERRA 
				| PR_color TO_PARABRE colorChoice TO_PARCIERRA '''

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
	'''paramVals : val moreParamVals 
				 | empty'''

def p_moreParamVals(p):
	'''moreParamVals : TO_COMA val moreParamVals 
				 	 | empty'''

def p_return(p):
	'return : PR_return megaExp'

def p_comparacion(p):
	'comparacion : PR_if TO_PARABRE megaExp TO_PARCIERRA TO_LLAABRE bloque TO_LLACIERRA maybeElse'

def p_maybeElse(p):
	'''maybeElse : PR_else TO_LLAABRE bloque TO_LLACIERRA 
				 | empty'''

def p_megaExp(p):
	'megaExp : maybeNot superExp anotherMega'

def p_maybeNot(p):
	'''maybeNot : PR_negacion 
				| empty'''

def p_anotherMega(p):
	'''anotherMega : opLogico megaExp 
				   | empty'''
def p_superExp(p):
	'superExp : exp maybeRel'

def p_maybeRel(p):
	'''maybeRel : opRelacional exp 
				| empty'''

def p_exp(p):
	'exp : term anotherExp'

def p_anotherExp(p):
	'''anotherExp : OP_MAS exp 
				  | OP_MENOS exp 
				  | empty'''


def p_term(p):
	'term : fact anotherTerm'

def p_anotherTerm(p):
	'''anotherTerm : OP_MULT term 
				   | OP_DIV term
				   | OP_RESID term
				   | empty'''

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

# for x in dir_func:
#     print (x)
#     for y in dir_func[x]:
#         print (y,':',dir_func[x][y])




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