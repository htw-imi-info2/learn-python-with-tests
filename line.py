from inspect import currentframe, getframeinfo
from os import path

def print_loc():
    fi = getframeinfo(currentframe().f_back)
    print("at line ",fi.lineno, " in ", path.basename(fi.filename))

print_loc()
