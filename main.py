from optparse import OptionParser
import lex_analyzer as analyzer


def load_file(option, opt, value, parser):

    with open(value) as f:
        data = f.read()

        lexer = analyzer.load_input_data(data)
        analyzer.tokenize_input_data()
        analyzer.print_results()


def read_raw_data(option, opt, value, parser):
    lexer = analyzer.load_input_data(value)
    analyzer.tokenize_input_data()
    analyzer.print_results()


parser = OptionParser()

parser.add_option("-f", "--file", help="lcc file location", metavar="FILE", action="callback", callback=load_file, dest="filename", type="string")

parser.add_option("-r", "--raw", dest="raw_load", help="Load raw data", metavar="RAW", action="callback", callback=read_raw_data, type="string")


(options, args) = parser.parse_args()
