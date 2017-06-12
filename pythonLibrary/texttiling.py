#! /usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.tokenize.texttiling import TextTilingTokenizer
from nltk.corpus import brown
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
from scipy import spatial
import textmining
import numpy as np
from rake_nltk import Rake_nltk


def read_datafile(datafile):
    fname = datafile
    dataset = []
    text = ''
    with open(fname) as f:
        content = f.readlines()
    f.close()
    for i in range(len(content)):
        lineArray = content[i].split(";")
        lineArray[-1] = lineArray[-1].strip('\n')
        dataset.append([])
        dataset[i].append(lineArray[0])
        dataset[i].append(lineArray[1])
        dataset[i].append(' '.join(lineArray[2:]))
        text = text + '\n'+ ' '.join(lineArray[2:]) + '\n'
    # dataset: [speaker; time; content]
    return dataset,text

def texttiling(text):
    ##all paras
    #tt = TextTilingTokenizer(w=20, k=  10, similarity_method=0, stopwords=None, smoothing_method=[0], smoothing_width=2, smoothing_rounds=1, cutoff_policy=1, demo_mode=False)
    ## param w: Pseudosentence size; param k: Size (in sentences) of the block used in the block comparison method
    tt = TextTilingTokenizer(w=80, k=7)
    segmented_text = tt.tokenize(text)
    print "there are " + str(len(segmented_text)) + " topics"
    #segmented_text is [[text..],[text..],,,]
    return segmented_text

    # #visually show segments
    # from nltk.corpus import brown
    # from matplotlib import pylab
    # tt = TextTilingTokenizer(w=70,demo_mode=True)
    # if text is None: text = brown.raw()[:10000]
    # s, ss, d, b = tt.tokenize(text)
    # pylab.xlabel("Sentence Gap index")
    # pylab.ylabel("Gap Scores")
    # pylab.plot(range(len(s)), s, label="Gap Scores")
    # pylab.plot(range(len(ss)), ss, label="Smoothed Gap scores")
    # pylab.plot(range(len(d)), d, label="Depth scores")
    # pylab.stem(range(len(b)), b)
    # pylab.legend()
    # pylab.show()

def sentences_grouped_by_topic(segmented_text, dataset):
    splitArray = []
    for i in range(len(segmented_text)):
        for j in range(len(dataset)):
            if dataset[j][2] in segmented_text[i]:
                k = j
                #ensure dealing with duplicate dataset[j][2]
                segmented_text[i] = segmented_text[i].replace("dataset[j][2]", "##REPLACED##")
        splitArray.append(k)

    contentArray = np.arange(len(dataset))
    contentGroupArray = []
    for k in range(len(splitArray)):
        if k == 0:
            contentGroupArray.append(contentArray[:splitArray[k]+1])
        elif k == len(splitArray)-1 and len(splitArray) != 2:
            contentGroupArray.append(contentArray[splitArray[k]+1:])
        elif k == len(splitArray)-1 and len(splitArray) == 2:
            contentGroupArray.append(contentArray[splitArray[k]+1:])
            contentGroupArray.append(contentArray[splitArray[k-1]+1:splitArray[k]+1])
        else:
            contentGroupArray.append(contentArray[splitArray[k-1]+1:splitArray[k]+1])
            contentGroupArray.append(contentArray[splitArray[k]+1:splitArray[k+1]+1])

    contentGroupArray = [list(t) for t in set(tuple(element) for element in contentGroupArray)]
    #different group sentences
    contentGroupArray.sort()
    groupSentenceIndexArray = filter(None, contentGroupArray)
    print "Sentences are separated into following array"
    print groupSentenceIndexArray
    return groupSentenceIndexArray

def extract_words(method, groupContent):
    if method == 0:
        return extract_keyphrases_for_topic(groupContent)
    elif method == 1:
        return extract_keywords_for_topic(groupContent)
    else:
        return tfidf(groupContent)

def tfidf(groupContent):
    corpus = groupContent
    stop = set(stopwords.words('english'))
    #将文本中的词语转换为词频矩阵  
    vectorizer = CountVectorizer()  
    #计算个词语出现的次数  
    X = vectorizer.fit_transform(corpus)  
    #获取词袋中所有文本关键词  
    word = vectorizer.get_feature_names()  
    #类调用  
    transformer = TfidfTransformer()  
    #将词频矩阵X统计成TF-IDF值  
    tfidf = transformer.fit_transform(X)  
    weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重  

    topicKeywordsList =[]
    for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重  
        topicKeywordsList.append([])
        print "doc",i,"tfidf--------------------------------------"  
        sortedArray = np.argsort(weight[i])
        topWords = []
        topArray = sortedArray[700:]
        for k in range(len(topArray)):
            if word[topArray[k]] not in stop:
                topWords.append([word[topArray[k]],weight[i][topArray[k]]])
                groupKeywordDict = {}
                groupKeywordDict["keyword"] = word[topArray[k]]
                groupKeywordDict["keywordScore"] = weight[i][topArray[k]]
                topicKeywordsList[i].append(groupKeywordDict)
        print topWords
    return topicKeywordsList


def extract_keyphrases_for_topic(groupContent, weightThreshold=5, sentenceLengthThreshold=6):
    rake = Rake_nltk()
    topicKeywordsList =[]
    for i in range(len(groupContent)):
        topicKeywordsList.append([])
        keywords = rake.run(groupContent[i])
        for j in range(len(keywords)):
            if keywords[j][1] > weightThreshold and len(keywords[j][0].split(" "))<sentenceLengthThreshold:
                groupKeywordDict = {}
                groupKeywordDict["keyword"] = keywords[j][0]
                groupKeywordDict["keywordScore"] = keywords[j][1]
                topicKeywordsList[i].append(groupKeywordDict)
    return topicKeywordsList

def extract_keywords_for_topic(groupContent, weightThreshold=8):
    rake = Rake_nltk()
    topicKeywordsList =[]
    for i in range(len(groupContent)):
        topicKeywordsList.append([])
        keywords = rake.run(groupContent[i])
        for j in range(len(keywords)):
            if keywords[j][1] > weightThreshold:
                keywordsList = keywords[j][0].split(" ")
                for k in range(len(keywordsList)):
                    groupKeywordDict = {}
                    groupKeywordDict["keyword"] = keywordsList[k]
                    groupKeywordDict["keywordScore"] = keywords[j][1]
                    topicKeywordsList[i].append(groupKeywordDict)
    #print topicKeywordsList
    return topicKeywordsList

def return_json_data(dataset,groupSentenceIndexArray,topicKeywordsList):
    data = []
    for i in range(len(groupSentenceIndexArray)):
        data.append({})
        data[i]["startTime"] = dataset[groupSentenceIndexArray[i][0]][1]
        #duration
        if i < len(groupSentenceIndexArray)-1:
            data[i]["topicDuration"] = time_format(dataset[groupSentenceIndexArray[i+1][0]][1]) - time_format(dataset[groupSentenceIndexArray[i][0]][1])
        else:
            data[i]["topicDuration"] = time_format(dataset[groupSentenceIndexArray[i][-1]][1]) - time_format(dataset[groupSentenceIndexArray[i][0]][1])
        data[i]["sentences"] = []
        index = 0
        for j in range(len(groupSentenceIndexArray[i])):
                data[i]["sentences"].append({})
                data[i]["sentences"][index]["sentenceTime"] = dataset[groupSentenceIndexArray[i][j]][1]
                data[i]["sentences"][index]["sentenceContent"] = dataset[groupSentenceIndexArray[i][j]][2]
                data[i]["sentences"][index]["sentenceSpeaker"] = dataset[groupSentenceIndexArray[i][j]][0]
                index += 1
        data[i]["keywords"] = topicKeywordsList[i]
        data[i]["topicName"] = topicKeywordsList[i][-2]["keyword"] + " "+ topicKeywordsList[i][-1]["keyword"] 
    return data

def time_format(str):
    strlist = str.split(":")
    time = int(strlist[0])*3600 + int(strlist[1])*60 +int(strlist[2])
    return time

class textTiling(object):
    def __init__(self, dataset_file_path):
        self.file_name = dataset_file_path

    def run(self):
        dataset, text = read_datafile(self.file_name)
        segmented_text = texttiling(text)
        #lda_extract_topics(segmented_text,5)
        groupSentenceIndexArray = sentences_grouped_by_topic(segmented_text,dataset)
        keywordsList = extract_words(2,segmented_text)
        data = return_json_data(dataset,groupSentenceIndexArray,keywordsList)
        return data

if __name__ == "__main__":
    dataset, text = read_datafile("../static/dataset.txt")
    segmented_text = texttiling(text)
    #lda_extract_topics(segmented_text,5)
    groupSentenceIndexArray = sentences_grouped_by_topic(segmented_text,dataset)
    keywordsList = extract_words(0,segmented_text)#0 is phrase, 2 is word
    #data = return_json_data(dataset,groupSentenceIndexArray,keywordsList)
    print keywordsList













    