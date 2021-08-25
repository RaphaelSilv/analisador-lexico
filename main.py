import ply.lex
import ply.yacc

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="specify file path", metavar="FILE")
parser.add_option("-s", "--source",
                  help="specify source code")

(options, args) = parser.parse_args()
