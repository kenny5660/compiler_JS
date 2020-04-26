# compiler_JS
javaScript code compiler as Academic project

INSTALLATION
------------
Requires

      java runtime
      curl

Run install commands:

      python setup.py install

for only rebuild gramma g4 file run

      python rebuild_g4.py

USAGE
------------
      usage: compiler_js [-h] [--print_ast] [-o O] inpath
      Compile js file.
      positional arguments:
        inpath       Input path to js file.

      optional arguments:
        -h, --help   show this help message and exit
        --print_ast  Print to stdout ast tree, if set -o argument then print ot file
        -o O         output file name

To print ast tree:

      compiler_js .\test\test_js_files\quickSort.js --print_ast

Print to file with operator '>' have problems with unicode in windows, but you can use '-o' argument for print to file.

      compiler_js .\test\test_js_files\quickSort.js --print_ast -o ast.txt


TESTS
------------
To run all tests:

      python -m unittest discover -s test
