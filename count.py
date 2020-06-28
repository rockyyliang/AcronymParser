import sys

from aparser import countAcronyms
from pathCheck import validPaths

def main(paths):
    counter = {}
    for p in paths:
        counter = countAcronyms(p, counter)

    #sort by occurance
    occurances = sorted(counter.items(), key=lambda x:x[1], reverse=True)
    print('Acronyms and their occurances:')
    for k, v in occurances:
        print(str(k) + ' ' + str(v))


if __name__=='__main__':
    paths = validPaths(sys.argv[1:])
    print('\nCounting acronyms from {} files:'.format(len(paths)))
    for p in paths:
        print(p)
    print('\n')
    main(paths)
