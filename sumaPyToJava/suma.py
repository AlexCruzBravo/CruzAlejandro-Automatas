from antlr4 import *
from pyToJavaLexer import pyToJavaLexer
from pyToJavaParser import pyToJavaParser
from listenerSuma import ListenerSuma

def main():
    in_file = input("\nIngrese el nombre del archivo: ")
    
    with open(in_file, 'r') as file:
        contenido = file.read()
        input_stream = InputStream(contenido)
        
        lexer = pyToJavaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = pyToJavaParser(stream)
        tree = parser.program()

        listener = ListenerSuma()
        walker =  ParseTreeWalker()
        walker.walk(listener, tree)
        

if __name__ == "__main__":
    main()


