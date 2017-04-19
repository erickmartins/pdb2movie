import sys
import argparse
import os
import cleanpdb
import runfirst
import runelnemo
import runfroda

if __name__ == "__main__":#
    try:
        os.mkdir(sys.argv[1][:-4])
    except Exception:
        os.system("rm "+sys.argv[1][:-4]+"/*")
        pass
    clean_file=cleanpdb.cleanPDB(sys.argv)
    hydro_file=runfirst.firstsim(sys.argv,clean_file)
    runelnemo.elnemosim(sys.argv,hydro_file)
    runfroda.frodasim(sys.argv,hydro_file)