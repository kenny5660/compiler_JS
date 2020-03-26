import sys
import compiler_js.core
def main():
    if len(sys.argv) < 2:
        print("Error: no input files")
        return -1

    print("Hello")
    print(sys.argv)
    compiler_js.core.compile_file(sys.argv[1])
 
if __name__ == '__main__':
    #main()
    main()
