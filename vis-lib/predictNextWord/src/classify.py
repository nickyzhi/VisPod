#!/usr/bin/python

import cPickle, argparse

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_object', default=None,
        help='give file path to load trained object')
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
        action="store_true")
    parser.add_argument("-w", "--word", required=True, 
        help="give word to classify")
    args = parser.parse_args()
    
    try:
        f = file(args.file_object, 'rb')
        classifier = cPickle.load(f)
        f.close()
        res = classifier.classify(args.word)
        print '\"'+args.word+'\"', 'is most probably followed by(sorted by probability high to low): '
        for i in range(len(res)):
            print res[i]+"  "
        
        
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except:
        print "Unexpected error"

if __name__ == "__main__":
    main()
