# -*- coding: utf-8 -*-
import unittest   # The test framework
import compiler_js.core
import compiler_js.ast_printer as ast_printer
class Test_TestAst(unittest.TestCase):
    def test_ast_quickSort_js(self):
        tree = compiler_js.core.parse_file('test\\test_js_files\\quickSort.js')
        ast_printer.print_tree_to_file(tree,'out.txt')    

if __name__ == '__main__':
    unittest.main()