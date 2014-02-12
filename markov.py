#!/usr/bin/env python

import sys, random, string


#
def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
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

    upperkeys = []

    for key in chains.keys():
        if key[0][0] in string.uppercase:
            upperkeys.append(key)

    thebigram = random.choice(upperkeys)

    # TODO : only use lowercase letters (except I) inside generated text

    generated = []

    generated.append(thebigram[0])
    generated.append(thebigram[1])

    endpunc = False

    while not endpunc:
        nextword = random.choice(chains.get(thebigram))
        generated.append(nextword)
        thebigram = (thebigram[1], nextword)
        if len(generated) >= 15 and ('.' in nextword or '!' in nextword):
            endpunc = True

    return ' '.join(generated) 

def main():
    args = sys.argv

    input_text = ""

    for eachfile in args[1:]:
        f = open(eachfile)
        input_text += f.read()
        f.close()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

#just let this one run. we'll explain it later.
if __name__ == "__main__":
    main()
