import sys
import re
import math
from collections import defaultdict
 
mypath="\\Hamshahri\\"
    
PUNCTUATION = re.compile(r'["\',;!?()\\/&%$^.:-<>\[\]،.:؛]+')

def analyze(filename):
    "Build a markov chain of words and neighbours"
    fd = open(filename, "r",encoding="utf-8")
    
    markov = {}
 
    for line in fd.readlines():
        line = line.strip().lower()
        line = re.sub(PUNCTUATION, " ", line)

        words = line.split()
        tot = len(words)
        x = 0
        while x < tot - 1:
            if  not (words[x].isdigit() or words[x + 1].isdigit()) and \
                len(words[x]) > 1 and \
                len(words[x + 1]) > 1:

                markov.setdefault(words[x], []).append(words[x + 1])
            x += 1
 
    fd.close()
 
    return depurate(markov)
 
def count_items(wordlist):
    d = {}
    for word in wordlist:
        d[word] = d.setdefault(word, 0) + 1
    return d
 
def depurate(markov_rawchain):
    """
    Remove items from the markov chain that are below
    the threshold (and compute this threshold as well)
    """
    final = {}   
    for word, items in markov_rawchain.items():
        threshold=-1
        for w, c in count_items(items).items():
            if c > threshold:
                final.setdefault(word, []).append(w)
                threshold=c
    return final
 
def print_chain(chain):
    for word, words in chain.items():
        with open(mypath+"Model.txt",'a',encoding="utf-8") as f:
            f.write("%s: %s" % (word, words[-1]))
            f.write("\n")
        
if __name__ == '__main__': 
    print("Start...")
    final = analyze(mypath+"Total.txt")
 
    print_chain(final)
    print("\n Done!")