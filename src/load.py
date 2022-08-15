import sys
import os
def loadtext():
    name = sys.argv[1]
    r = os.path.isfile(name)
    if r:
        f = open(name)
        src = f.read()
        f.close()
        return src
    else:
        print("file load error")
        sys.exit(0)
