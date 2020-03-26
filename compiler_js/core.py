import sys

import antlr4 
from antlr4.tree.Trees import Trees
from compiler_js.antlr4_ecmas.ECMAScriptLexer import ECMAScriptLexer
from compiler_js.antlr4_ecmas.ECMAScriptParser import ECMAScriptParser
from compiler_js.antlr4_ecmas.ECMAScriptListener import ECMAScriptListener

def compile_file(path):
    input_stream = antlr4.FileStream(path)
    compile_js_stream(input_stream)

def compile_js_stream(input_stream):
    lexer = ECMAScriptLexer(input_stream)
    token = lexer.nextToken()
    token2 = lexer.nextToken()
    stream = antlr4.CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream)
    tree = parser.program()
    print(Trees.toStringTree(tree, None, parser))
   # print(tree.toStringTree())