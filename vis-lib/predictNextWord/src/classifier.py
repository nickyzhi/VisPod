import re
from collections import defaultdict   #needs python > 2.5
import operator
#from mongodict import MongoDict
#from pymongo import Connection

class Classifier:

    def __init__(self, verbose=False):
        ''' Apriori and joint are calculated each time a file is read.
            posterior is only calculated when a certain word is being evaluated
            Thus posterior['hello'] is the most probable word following 'hello'
            along with the corresponding probability '''
            
        self.apriori  = defaultdict(int)
        self.joint = defaultdict(int)
        #self.apriori = MongoDict(host='localhost', port=27017, database='next_word',
        #                    collection='apriori')
        #self.joint = MongoDict(host='localhost', port=27017, database='next_word',
        #                    collection='joint')
        self.posterior = {}
        self.verbose = verbose
        
        #self.connection = Connection()
        
        
    def update_joint_apriori(self, dict_bigrams):
        '''Every time an new file is read, the bigrams (defaultdicts) are created
           and the apriori && joint probs are updated '''
           
        for k, v in dict_bigrams.items():
            if type(k).__name__ != 'tuple' or len(k) != 2 or type(v).__name__!='int':   
                #sth is wrong
                if self.verbose:
                    print 'wrong bigram type, skipping:\t', k,v
                continue
            self.joint[k] += v
            self.apriori[k[0]] += v
        
        return self.joint  #redundant: just for unit testing
        
    def calculate_posterior(self, word):
        ''' For each word update the posterior (next word prediction).
            We want to maximize joint_prob(word,next) / prior(word)'''
        originalBigram = {}
        sortBigram = []
       
        postProb = []

        #max = -1
        for k, v in self.joint.items():
            
            prev, next = k[0], k[1]
            assert type(prev).__name__ == 'str'
            assert type(next).__name__ == 'str'
            if prev == word:
                
                originalBigram[k]=v
        #print originalBigram
        for x, y in originalBigram.items():
            postProb = round(float(y)/float(self.apriori[word]), 2)#round 2 digit number after dot
            #assert postProb <= 1.0
            originalBigram[x] = postProb
            #print postProb
        #print originalBigram

        sortBigram = sorted(originalBigram.items(), key=lambda x: x[1], reverse = True)
        #print len(sortBigram),sortBigram[0][0][1],sortBigram[1][0][1]
            
        self.posterior[word]=[sortBigram[0][0][1]]
        if len(sortBigram)>5:
            self.posterior[word] = [sortBigram[0][0][1],sortBigram[1][0][1],sortBigram[2][0][1],sortBigram[3][0][1],sortBigram[4][0][1]]
        else:

            for i in range(1,len(sortBigram), 1):
                #print sortBigram[i][0][1]
                self.posterior[word].append(sortBigram[i][0][1])

        
        #self.posterior[word] = (sortBigram[0][0][1],sortBigram[0][1])
            
                        
  

    
    def pre_train(self):
        ''' To calculate all of the posteriors before the classifier (classify.py is runned).
            Computationally FORBIDABLE '''
        
        for k, v in self.apriori.items():
            self.calculate_posterior(k)
    
    def classify(self, word):
        '''clean the word and find the most probable follower (calculate_posterior)'''
        
        word = re.sub('[,!#$%&()*+,-.:;<=>?@^_{|}~]', '', word)
        word = word.lower()
        #searches for the most probable outcome based on joint and prior probs
        self.calculate_posterior(word)
        return self.posterior[word]
    
    def save(self, dbName):
        db = self.connection[dbName]
        db.apriori.insert(self.apriori)
        db.joint.insert(self.joint)
    
    def load(self, dbName):
        db = self.connection[dbName]
        self.apriori = db.apriori.find()  #its only one
        self.joint = db.joint.find()
    
    def print_probs(self):
        
        print 'apriori length (number of words): ', len(self.apriori)
        print 'joint length (number of bigrams): ', len(self.joint)
        
