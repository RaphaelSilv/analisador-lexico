from ply import lex

resultado_lexema = []

literals = "+-*/{}[](),;=%"

def t_plus(t):
    r'\+'
    t.type = '+'     
    return t

def t_minus(t):
    r'-'
    t.type = '-'
    return t

def t_times(t):
    r'\*'
    t.type = '*'     
    return t

def t_divide(t):
    r'\/'
    t.type = '/'
    return t

def t_lparen(t):
    r'\('
    t.type = '('     
    return t

def t_rparen(t):
    r'\)'
    t.type = ')'
    return t

def t_lcol(t):
    r'\['
    t.type = '['     
    return t

def t_rcol(t):
    r'\]'
    t.type = ']'
    return t

def t_lbrace(t):
    r'\{'
    t.type = '{'     
    return t

def t_rbrace(t):
    r'\}'
    t.type = '}'
    return t

def t_comma(t):
    r','
    t.type = ','
    return t
    
def t_semicolon(t):
    r';'
    t.type = ';'
    return t
    
def t_at(t):
    r'='
    t.type = '='
    return t
    
def t_mod(t):
    r'%'
    t.type = '%'
    return t

t_ignore = " \t"

reserved = {
    'return': 'RETURN',
    'def': 'DEF',
    'break': 'BREAK',
    'if': 'IF',
    'else': 'ELSE',
    'print': 'PRINT',
    'for': 'FOR',
    'new': 'NEW',
    'read': 'READ',
    'null': 'NULL',
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
}

tokens = [
    "IDENT",
    "RELOP",  # ( <= | < | == | != | > |>=  )
    "INT_CONSTANT",
    "FLOAT_CONSTANT",
    "STRING_CONSTANT"
] + list(reserved.values())


# t_RELOP = r''

def t_IDENT(t):
    r'[a-zA-Z_] [a-zA-Z_0-9]*'
    t.type = reserved.get(t. value, 'IDENT')
    return t


def t_INT_CONSTANT(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_FLOAT_CONSTANT(t):
    r"\d+"
    t.value = float(t.value)
    return t


def t_STRING_CONSTANT(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


# Give the lexer some input
def load_input_data(data):
    return lexer.input(data)


def print_input_data(data):

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok.type, tok.value)
