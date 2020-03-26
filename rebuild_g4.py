import subprocess
import os.path
import os
path_install= "compiler_js/antlr4_ecmas"
path_jar = "antlr.jar"
path_g4="ECMAScript.g4"
if(not os.path.isfile(path_jar)):
    subprocess.call(["curl","-o",path_jar, "https://www.antlr.org/download/antlr-4.8-complete.jar   "])
os.system("java -jar {0} -Dlanguage=Python3 -o {1} {2}".format(path_jar,path_install,path_g4))
print(os.name)
if os.name == "nt":
    os.system("del {0}\*.tokens".format(path_install.replace("/","\\")))
    os.system("del {0}\*.interp".format(path_install.replace("/","\\")))
    
else:
    os.system("rm {0}/*.tokens".format(path_install))
    os.system("rm {0}/*.interp".format(path_install))

