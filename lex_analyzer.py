from ply import lex

data = """
def func1(int A, int B)
def func1(int A, int B)
"""

resultado_lexema = []
tabela_de_simbolos = {}
erros_lexema = []

# List of tokens that are literals and have only one character
literals = "+-*/{}[](),;=%"


def t_plus(t):
    r'\+'  # scape because + has a meaning in regular expressions
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


def t_lbracket(t):
    r'\['
    t.type = '['
    return t


def t_rbracket(t):
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


# Token for ignored characters (spaces, tabs, etc.)
t_ignore = ' \t\r'

# Tokens that are reserved keywords
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

# Tokens
tokens = [
    "IDENT",
    "RELOP",  # ( <= | < | == | != | > |>=  )
    "INT_CONSTANT",
    "FLOAT_CONSTANT",
    "STRING_CONSTANT"
] + list(reserved.values())


def t_IDENT(t):
    r'[a-zA-Z_] [a-zA-Z_0-9]*'
    t.type = reserved.get(t. value, 'IDENT')
    return t


def t_RELOP(t):
    r'(<=|<|==|!=|>=|>)'
    return t


def t_FLOAT_CONSTANT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT_CONSTANT(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_STRING_CONSTANT(t):
    # Accept a string between quotes and supports scape characters
    r'"([^\\\"]|\\.)*"'
    t.value = t.value
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    global erros_lexema
    estado = "** Erro lexico na Linha {:4} Coluna {:4} Valor {:16}".format(
        str(t.lineno), str(t.lexpos), str(t.value))
    erros_lexema.append(estado)
    t.lexer.skip(1)


lexer = lex.lex()

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    resultado_lexema.append(tok.type)
    if tok.type == 'IDENT':
        if tok.value not in tabela_de_simbolos:
            tabela_de_simbolos[tok.value] = [tok.lineno]
        else:
            tabela_de_simbolos[tok.value].append(tok.lineno)

if erros_lexema:
    for elem in erros_lexema:
        print(elem)
else:
    print(resultado_lexema)
    print("Tabela de Simbolos")
    for key, value in tabela_de_simbolos.items():
        print("Ident: " + key + " linhas: ", value)
