#!/usr/bin/python

import sys, random, string


#
def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    splitcorpus = corpus.split()
    
    ## initialize empty dictionary
    chains = {}
    
    ## loop through list of strings, assign each bigram to a key
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

    startkeys = []
    openquotekeys = []

    ## beginning: make subsets of keys for capitals and open quotes
    for key in chains.keys():
        if key[0][0] in string.uppercase:
            startkeys.append(key)
        if key[0][0] in '"':
            openquotekeys.append(key)
            startkeys.append(key)
        if  key[1][0] in '"':
            openquotekeys.append(key)


    ## beginning: randomly choose first key
    thebigram = random.choice(startkeys)


    ##  middle: initialize generated sentence and length counter
    generated = []

    thelength = 0

    ## middle: add the first two words to the sentence
    generated.append(thebigram[0])
    generated.append(thebigram[1])
    thelength += len(thebigram[0] + thebigram[1]) +1



    ## middle: set up conditions for loop ending
    ending = False
    inquote = False

    ## check if quote is already open
    if thebigram in openquotekeys and thebigram[0][-1] not in '"' and thebigram[1][-1] not in '"':
        inquote = True

    ## ending: don't loop until has added first bigram and set up ending conditions
    while not ending:

        # TRY to get values that don't end with quote where not in quote and vice versa
        if not inquote:
            allvalues = chains.get(thebigram)
            nextvalues = []
            for value in allvalues:
                if value[-1] != '"':
                    nextvalues.append(value)
            if len(nextvalues) == 0:
                nextvalues = allvalues
        else:
            allvalues = chains.get(thebigram)
            nextvalues = []
            for value in allvalues:
                if value[0] != '"':
                    nextvalues.append(value)
            if len(nextvalues) == 0:
                nextvalues = allvalues

### end_gracefully
        if thelength >= 110:
            allvalues = chains.get(thebigram)
            nextvalues = []
            for value in allvalues:
                if ('.' in value or '!' in value or '?' in value):
                    nextvalues.append(value)
            if len(nextvalues) == 0:
                nextvalues = allvalues



        # get a random value from bigram's values
        nextword = random.choice(nextvalues)
        generated.append(nextword)
        thelength += len(nextword) + 1
        thebigram = (thebigram[1], nextword)


        # set up inquote checking
        if nextword[0] in '"':
            inquote = True
        
        if inquote == True and nextword[-1] in '"':
            inquote = False

        newtotal = thelength + len(nextword) + 1

        # close only if conditions are met: no open quotes, ending punctuation in last word        
        if inquote == False and newtotal <= 140:
            if ('.' in nextword or '!' in nextword or '?' in nextword):
                ending = True
        elif newtotal > 140:
            del generated[-1]
            ending = True
        

    return ' '.join(generated) 

def main():
    args = sys.argv

    input_text = ""

    ## take any number of input files
    for eachfile in args[1:]:
        f = open(eachfile)
        input_text += ' ' + f.read()
        f.close()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()