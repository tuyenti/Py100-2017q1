#!/usr/bin/env python
# Tuyen Nguyen
# HW4
##############################################
def dictionary_add(curent_dict, key,value):
    curent_dict[key] = value

def remove_entry(diction,key,entry):
    diction[key].remove(entry)

def replacewith(curent_dict, character):
    for i in curent_dict:
        for j in range(len(curent_dict[i])):
            assert isinstance(character, object)
            curent_dict[i][j] = character

def setbuild(divisible, maximum):
    i = 0
    myset = set()
    while (True):
        value = i * divisible
        if (value <= maximum):
            myset.add(i*divisible)
            i +=1
        else:
            break
    return myset

def setexercise():
    s2 = setbuild(2, 20)
    s3 = setbuild(3, 20)
    s4 = setbuild(4, 20)
    print(s2)
    print(s3)
    print(s4)
    print(str(s3.issubset(s2)))
    print(str(s4.issubset(s2)))
    pythonset = set('Python')
    pythonset.add('i')
    fs = frozenset('marathon')
    print(pythonset.union(fs))
    print(pythonset.intersection(fs))

def test_diction():
    new_dict = dict()
    dictionary_add(new_dict,'Chris Seattle Chocolate',['name','city','cake'])
    print(new_dict)
    remove_entry(new_dict,'Chris Seattle Chocolate','cake')
    print(new_dict)
    dictionary_add(new_dict,'Mango',['fruit'])
    print(new_dict.keys())
    print(new_dict.values())
    keyindiction = 'cake' in new_dict
    print('\'cake\' is they key: ' + str(keyindiction))
    keyindiction = 'Mango' in new_dict
    print('\'Mango\' is they key: ' + str(keyindiction))
    replacewith(new_dict, 't')
    print(new_dict)

if __name__ == "__main__":
    test_diction()
    setexercise()