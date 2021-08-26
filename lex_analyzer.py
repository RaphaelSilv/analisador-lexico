from ply import lex

data = """
"teste de string literal"
def func1(int A, int B)
{
  int SM[2];
  SM[0] = A + B;
  SM[1] = B * C;
  return;
}

def principal()
{
  int C;
  int D;
  int R;
  C = 4;
  D = 5;
  R = func1(C, D);
  return;
}
"""

resultado_lexema = []

# List of tokens that are literals and have only one character
literals = "+-*/{}[](),;=%"

def t_plus(t):
    r'\+' #scape because + has a meaning in regular expressions
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
t_ignore = ' \t\r\n'

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
    r'"([^\\\"]|\\.)*"' #Accept a string between quotes and supports scape characters
    t.value = t.value
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok.type) #     print the token found

