import sys
import compiler_js.core
def main():
    if len(sys.argv) < 2:
        print("Error: no input files")
        return -1
    compiler_js.core.parse_file(sys.argv[1])
 
if __name__ == '__main__':
    #main()
    main()
