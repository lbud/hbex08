#!/usr/bin/env python

import sys
import random



#
def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    corpus = corpus.lower()
    splitcorpus = corpus.split()
    #maybe strip it? if we need to? 

    # initialize empty dictionary
    chains = {}
    
    #loop through list of strings, assign each bigram to a key
    for i in range(len(splitcorpus) - 2):
        bigram = (splitcorpus[i], splitcorpus[i+1])
        if not chains.get(bigram):
            chains[bigram] = [splitcorpus[i+2]]
        else:
            chains[bigram].append(splitcorpus[i+2])

    return chains

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # takes output (dictionary) of make_chains
    # print a random bigram (key)

    thekeys = chains.keys()
    thebigram = random.choice(thekeys)

    generated = []

    generated.append(thebigram[0])
    generated.append(thebigram[1])

    # write a loop
        # using random.choice() output the predicted string
        # reassign bigram to the new bigram
    for i in range(30):
        nextword = random.choice(chains.get(thebigram))
        generated.append(nextword)
        thebigram = (thebigram[1], nextword)

    return ' '.join(generated)

def main():
    args = sys.argv
    script, filename = args

    f = open(filename)
    input_text = f.read()
    f.close()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

#just let this one run. we'll explain it later.
if __name__ == "__main__":
    main()
