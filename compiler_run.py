import sys

import antlr4 
from antlr4.tree.Trees import Trees
from antlr4_js_parser.ECMAScriptLexer import ECMAScriptLexer
from antlr4_js_parser.ECMAScriptParser import ECMAScriptParser
from antlr4_js_parser.ECMAScriptListener import ECMAScriptListener
 
def main(argv):
    input_stream = antlr4.FileStream(argv[1])
    lexer = ECMAScriptLexer(input_stream)
    token = lexer.nextToken()
    token2 = lexer.nextToken()
    stream = antlr4.CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream)
    tree = parser.program()
    print(Trees.toStringTree(tree, None, parser))
   # print(tree.toStringTree())
 
if __name__ == '__main__':
    #main()
    main(sys.argv)