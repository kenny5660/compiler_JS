# -*- coding: utf-8 -*-
import sys
import compiler_js.core
import compiler_js.ast_printer as ast_printer
import argparse

def main():
    parser = argparse.ArgumentParser(description='Compile js file.')
    parser.add_argument("inpath", type=str, help='Input path to js file.')
    parser.add_argument("--print_ast", action='store_true',help='Print to stdout ast tree, if set -o argument then print ot file')
    parser.add_argument("-o",type=str, help='output file name')
    args = parser.parse_args()

    tree = compiler_js.core.parse_file(args.inpath)
    if args.print_ast:
        if args.o:
            ast_printer.print_tree_to_file(tree,args.o)
        else:
            ast_printer.print_tree(tree)

if __name__ == '__main__':
    main()
