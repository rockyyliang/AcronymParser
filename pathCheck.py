import os
import sys

def verifyPath(fname):
    '''make sure file exists'''
    if not os.path.isfile(fname):
        print("Can't find " + fname)
        return False
    else:
        return True

def validPaths(paths):
    '''input is a list of paths
    outputs list of paths that are valid (usable)
    '''
    return [p for p in paths if verifyPath(p)]

if __name__=='__main__':
    paths = []
    for p in sys.argv[1:]:
        paths.append(p)
    
    print(validPaths(paths))
