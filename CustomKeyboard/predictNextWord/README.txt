THIS IS FOR TEXT PREDICTION.

==TRAINING==

$ python src/train.py -d medical/ -fo trained.pickle -v

The second parameter(medical/) is the dataset need to be tranined, the fourth parameter is the name of the model we got.

==USAGE==

$ python src/classify.py -f trained.pickle -w no

trained.pickle is the model we are using, "no" is the word we need to predict. 

For example, run $ python src/classify.py -f trained_medical.pickle -w and
you will got the result as following:
"and" is most probably followed by (sorted by probablity high to low):
foot
the 
parasitic
neuroleptics
large

There'll be five words to be listed at most. 

== METHODOLOGY ==

We applied the maximum likelihood method in order to predict the most probable word (W[n])
following (W[n-1]). Thus we seek to maximize the following quantity:

Prob(W[n] | W[n-1]) =  Prop(W[n] and W[n-1]) / Prob (W[n]) = count(W[n-1]W[n]) / count(W[n])

Thus for each text we build all of the possible bigrams, counting their frequency.
Then we feed them to the classifier which updated its counts about \
a)The frequency of each word (defaultdict: prior)
b)The frequency of each bigram (defaultdict: joint) 

In order to predict the W[n] given W[n-1], it searches all of the bigrams stored in (joint) and
computes the forementioned prob. It returns the max. Details in the code.
