
def cleanWord(word):
    '''returns word without leading or trailing symbols'''
    i = 0
    j = len(word)-1
    while (not word[i].isalpha()) or (not word[j].isalpha()):
        if not word[i].isalpha():
            i += 1
        if not word[j].isalpha():
            j -= 1
    return word[i:j+1]

def countAcronyms(fname, counter):
    '''takes in tex file path and counter, returns updated counter'''
    #assume valid file path+name
    with open(fname, 'rb') as tex:
        for line in tex:
            for word in line.split():
                if len(word)>1 and word.isupper():
                    #decode and remove leading/trailing non alphabet chars
                    acronym = word.decode('utf-8')
                    acronym = cleanWord(acronym)
                    #after cleaning, acronym might have len()==1 again
                    if len(acronym)>1:
                        #print(acronym)
                        if acronym in counter:
                            counter[acronym] += 1
                        else:
                            counter[acronym] = 1
    return counter



if __name__=='__main__':
    counter = {}
    counter = countAcronyms('chapter-VD.tex', {})
    for k, c in counter.items():
        print(str(k),c)
