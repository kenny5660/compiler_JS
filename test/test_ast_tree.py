# -*- coding: utf-8 -*-
import unittest   # The test framework
import compiler_js.core
import compiler_js.ast_printer as ast_printer
import os
class Test_TestAst(unittest.TestCase):
    maxDiff = None
    def test_ast_quickSort_js(self):
        tree = compiler_js.core.parse_file('test\\test_js_files\\quickSort.js')
        ast_str = ast_printer.tree_to_str(tree).strip('\n')
        ast_file = open('test\\test_js_files\\quickSort.js'+'.ast',encoding="utf-8")
        ast_str_ref = ast_file.read().strip('\n')
        ast_file.close()
        self.assertEqual(ast_str,ast_str_ref)

    def assert_ast_all_files_in_dir(self,dir_name):
        for root, dirs, files in os.walk(dir_name):
            for file in files:
                if file[-3:] == '.js':
                    with self.subTest(dir=root,file=file):
                        
                        tree = compiler_js.core.parse_file(root +'\\'+ file)
                        ast_str = ast_printer.tree_to_str(tree).strip('\n')
                        ast_file  = open(root +'\\'+ file+'.ast',encoding="utf-8")
                        ast_str_ref = ast_file.read().strip('\n')
                        ast_file.close()
                        self.assertEqual(ast_str,ast_str_ref)


    def test_declaration(self):
        dir_name = 'test/test_js_files/declaration'
        self.assert_ast_all_files_in_dir(dir_name)
    def test_expressions(self):
        dir_name = 'test/test_js_files/expression'
        self.assert_ast_all_files_in_dir(dir_name)
    def test_statements(self):
        dir_name = 'test/test_js_files/statement'
        self.assert_ast_all_files_in_dir(dir_name)


if __name__ == '__main__':
    unittest.main()