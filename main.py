import lex_analyzer as analyzer


data = """
int 3 + int 4 * int 10
  + -20 *2
"""


lexer = analyzer.load_input_data(data)
analyzer.print_input_data(lexer)
