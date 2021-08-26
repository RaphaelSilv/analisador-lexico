import lex_analyzer as analyzer


data = """
int bar = 7
foo = 3
return foo
"""


lexer = analyzer.load_input_data(data)
analyzer.print_input_data(lexer)
