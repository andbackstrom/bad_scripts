#!/usr/bin/env python3
import sys, json, re
from random import randint

def fix(key, list, rgx):
    if key not in list:
        return key
    
    for word in list[key]:
        vars = re.findall(rgx, word)
        if len(vars) > 0:
            return " ".join([fix(i, list, rgx) for i in vars])
        else:
            return list[key][randint(0, len(list[key]) - 1)]

def beautify(words, list):
    res = []
    regex_word = re.compile(r'{(\w+)}')
    regex_sym = re.compile(r'{(\W+)}')
    for split in words.split():
        word = [i.lower() for i in re.split(r'\W+', split) if i is not '']
        for i in range(len(word)):
            word[i] = fix(word[i], list, regex_word)
        word = "".join(word)
        
        roll = randint(0, 10)
        if roll > 7:
            word = word.capitalize()
        
        sym = [i for i in re.split(r'\w+', split, flags=re.I) if i is not '']
        for i in range(len(sym)):
            sym[i] = fix(sym[i], list, regex_sym)
        sym = "".join(sym)
        
        roll = randint(0, 5)
        if roll > 4:
            sym = " " + sym
        
        res.append(word + sym)
        
    return " ".join(res)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: {} <args...>".format(sys.argv[0]))
        exit(1337)
        
    with open("wordlist.json", 'r', encoding="ISO-8859-1") as f:
        list = json.load(f)
    
    for sentence in sys.argv[1:]:
        print(beautify(sentence, list))