import sys

import antlr4 
from antlr4.tree.Trees import Trees
from compiler_js.antlr4_ecmas.ECMAScriptLexer import ECMAScriptLexer
from compiler_js.antlr4_ecmas.ECMAScriptParser import ECMAScriptParser
from compiler_js.antlr4_ecmas.ECMAScriptListener import ECMAScriptListener

def parse_file(path):
    input_stream = antlr4.FileStream(path)
    return parse_js_stream(input_stream)

def parse_js_stream(input_stream):
    lexer = ECMAScriptLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream)
    tree = parser.program()
    return tree