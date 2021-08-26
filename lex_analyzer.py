from ply import lex

resultado_lexema = []

tokens = (
    "INT",
    "FLOAT",
    "STRING",
    "IDENT",
    "LPAREN",
    "RPAREN",
    "LCOL",
    "RCOL",
    "LBRACK",
    "RBRACK",
    "COMMA",
    "SEMICOLON",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "RELOP",  # ( <= | < | == | != | > |>=  )
    "AT",
    "MOD",
    "RETURN",
    "DEF",
    "BREAK",
    "IF",
    "ELSE",
    "PRINT",
    "FOR",
    "NEW",
    "READ",
    "NULL",
    "INT_CONSTANT",
    "FLOAT_CONSTANT",
    "STRING_CONSTANT",
    "WS",  # (\t, \n)
)

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LCOL = r"\["
t_RCOL = r"\]"
t_LBRACK = r"{"
t_RBRACK = r"}"
t_COMMA = r","
t_SEMICOLON = r";"
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"\/"
t_AT = r"="
t_MOD = r"%"

t_INT = r"int"
t_FLOAT = r"float"
t_STRING = r"string"
t_PRINT = r"print"
t_RETURN = r"return"
t_ELSE = r"else"
t_READ = r"read"
t_NULL = r"null"
t_NEW = r"new"
t_FOR = r"for"
t_BREAK = r"break"
t_IF = r"if"
t_DEF = r"def"

t_ignore = " \t"

# t_RELOP = r''
# t_IDENT = r''


def t_INT_CONSTANT(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_FLOAT_CONSTANT(t):
    r"\d+"
    t.value = int(t.value)
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
