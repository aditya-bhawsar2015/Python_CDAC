
dict1 = {1 : 'abc', 2: 'def', 3: 'ghi'}
dict2 = {3: 'jkl', 4: 'mno', 5: 'pqr'}

print({**dict1 , **dict2})


def merge_dictionaries(dict1, dict2):
    print({**dict1,**dict2})

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merge_dictionaries(dict1,dict2)