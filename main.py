import sys
import os
from antlr4 import *
from python_generated.SPLLexer import SPLLexer
from python_generated.SPLParser import SPLParser
from python_generated.SPLInterpreterVisitor import SPLInterpreterVisitor

def main(argv):
    if len(argv) <= 1:
        print("ERROR: Please enter an input to be parsed.")
        return
    
    # Input wird als Kommandozeilenargument angegeben
    input = InputStream(argv[1])

    # Als Input wird eine Datei angegeben
    if os.path.isfile(argv[1]):
        input = FileStream(argv[1])
    
    lexer = SPLLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SPLParser(stream)
    tree = parser.program()

    walker = ParseTreeWalker()
    visitor = SPLInterpreterVisitor()
    visitor.visit(tree)


if __name__ == "__main__":
    main(sys.argv)