# -*- coding: utf-8 -*-
import antlr4
import sys
import locale
from operator import itemgetter
from tree_format import format_tree

def get_val(node):
    if isinstance(node,antlr4.TerminalNode):
        return "TerminalNode(  "+node.getSymbol().text+'  )'
    return type(node).__name__ + "(  "+node.start.text+"  )"

def get_children(node):
    if isinstance(node,antlr4.TerminalNode):
        return []
    n = node.getChildCount()
    children = []
    for i in range(n):
        child = node.getChild(i)
        if not isinstance(child,antlr4.TerminalNode):
            children.append(child)
    return children

def print_tree_to_file(root, path):
    orig_stdout = sys.stdout
    f = open(path, 'w', encoding="utf-8")
    sys.stdout = f
    print_tree(root)
    f.close()
    sys.stdout = orig_stdout

def tree_to_str(root):
    return format_tree(root,format_node=get_val, get_children=get_children)

def print_tree(root):
        print(tree_to_str(root))
