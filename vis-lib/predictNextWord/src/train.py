#!/usr/bin/python

import argparse, cPickle, os, time, math, sys, signal,re
from classifier import Classifier
from parser import *

from collections import defaultdict, Counter   #defaultdict needs python > 2.5  
from itertools import izip, islice

startTime = None
classifier = None

def _exit(message):
    print message
    exit(1)

def print_time_elapsed():
    
    global starTime
    seconds = time.time()-startTime
    minutes = math.floor(seconds / 60)
    secs = seconds % 60
    print 'time elapsed: ' +str(minutes) + 'min ' +str(secs) +'s'
    return seconds

def save_classifier(filename):
    
    global classifier
    try: 
        with open (filename, 'wb') as f:
            cPickle.dump(classifier, f, protocol=cPickle.HIGHEST_PROTOCOL)
    except:
        print "error:", sys.exc_info()[0]
        _exit("Could not save classifier in " +filename)

def load_classifier(filename):
    
    try:
        with open (filename, 'rb') as f:
            classifier = cPickle.load(f) 
        f.close()
        return classifier
    except:
        print "error:", sys.exc_info()[0]
        _exit('Could load classifier from ' + filename)

def signal_handler(signal, frame):
    ''' Ctrl-C handler. Save the classifier before exiting'''    
    filename = 'trained_stopped.pickle'
    print 'Saving classifier in ' , filename
    save_classifier(filename)
    print_time_elapsed()
    exit(0)

def split_sentences(text):
    ''' Break a text into sentences and return a list.'''

    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(text)
    sentenceList = [s.strip() for s in sentenceList]
    return sentenceList

def remove_stemming(sentenceList):
    '''Cleans each sentence from punctuation '''
    
    cleanSentences = []
    for s in sentenceList:
        assert type(s).__name__ == 'str'
        tmp = re.sub('[\[!#$%&()*+,-.:;<=>?@^_{|}~\'\"\]]', '', s)
        clean = tmp.replace("\r\n"," ")
        clean = clean.replace("\\", "")
        clean = clean.lower()
        cleanSentences.append(clean)
    return cleanSentences

def make_bigrams(s):
    '''Builds bigrams as defaultdicts where key is the a tuple containing two strings
       (each word), and the value is its frequency. E.g ('I', 'am'): 2. For example
       a complete bigram: defaultdict(<type 'int'>, 
       {('aqs', 'hello'): 1, ('what', 'hello'): 1, ('hello', 'man'): 2, ('man', 'what'): 1})
       Each bigram must be fed to Classifier.update_joint_apriori(bigram)
    '''
    words = s.split(' ')
    
    d = defaultdict(int, Counter(izip(words, islice(words, 1, None))))
    #counter example, Counter({'blue': 3, 'red': 2, 'green': 1})
    #islice, such as elements from seq[start:stop:step] islice('ABCDEFG', 2, None) --> C D E F G
    #izip,p, q, ... (p[0], q[0]), (p[1], q[1]), ... izip('ABCD', 'xy') --> Ax By
    
    return d
    
def merge_and_sum_bigrams(bigrams1, bigrams2):
    
    for k,v in bigrams2.items():
        #bigram is defaultdict so even if k not a key it will be added
        bigrams1[k] += bigrams2[k]     

    
def read_files_calculate_probs(rootdir, classifier):
    
    for root, subFolders, files in os.walk(rootdir):
        print 'Reading files and building the bigram table/info from ', root, ' ... '

        for f in files:
            if f[-4:] == ".txt":
                with open(os.path.join(root, f), 'r') as fin:
                    text = fin.read()
                    
                    sentences = split_sentences(text)
                    


                    sentencesWithoutStemming = remove_stemming (sentences)
                    allBigrams = defaultdict(int)   #Bigram along with their frequencies
                    for s in sentencesWithoutStemming:
                        newBigrams = make_bigrams(s)
                        merge_and_sum_bigrams(allBigrams, newBigrams)
                     
                    classifier.update_joint_apriori(allBigrams)  #THE ACTUAL TRAINING
        classifier.print_probs()    #so far (after each directory)

'''
def read_files(filename, classifier):
    
    with open(filename , 'r') as fin:
        text = fin.read()
        sentences = split_sentences(text)
        sentencesWithoutStemming = remove_stemming (sentences)
        allBigrams = defaultdict(int)
        for s in sentencesWithoutStemming:
            newBigrams = make_bigrams(s)
            merge_and_sum_bigrams(allBigrams, newBigrams)
        
        classifier.update_joint_apriori(allBigrams)
'''

def example_classify(word):
    '''Demonstration'''
    res = classifier.classify(word) #random example
    print '\"'+word+'\"', 'is most probably is followed by: "' +res[0]+ '" with probability: ', res[1]
    
def main():
    
    global startTime, classifier
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--rootdir", type=str, default="../www.gutenberg.lib.md.us", 
        help="The root directory to collect txt files for training")
    parser.add_argument('-fo', '--file_object_out', 
        help='give file path to store trained object', type=str, default="trained.pickle")
    parser.add_argument('-fi', '--file_object_in', 
        help='give file path to store trained object', type=str, default=None)
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
        action="store_true")
    args = parser.parse_args()

    if args.file_object_in != None:
        classifier = load_classifier(args.file_object_in)
    else:
        classifier = Classifier(args.verbose)

    #register the signal handler
    signal.signal(signal.SIGINT, signal_handler)  
    #start the clock
    startTime = time.time()
    #parse all the files and update classifier's dictionaries (prior && joint) frequences
    read_files_calculate_probs(args.rootdir, classifier)
    ###read_file('3.txt', classifier) ### testing
    if args.verbose:
        classifier.print_probs()
    #Train method does num_words(in all texts) * num_bigrams(num_joints) => FORGET IT
    ### classifier.pre_train() ###
    #classify will train the classifier for the specific word which is ok
    example_classify('and')
    
    save_classifier(args.file_object_out)
    print_time_elapsed()
    
if __name__ == "__main__":
    main()
