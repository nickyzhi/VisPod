#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy import spatial
import textmining
import numpy as np
import lda
import lda.datasets
from rake import Rake


def read_datafile(datafile):
    fname = datafile
    dataset = []

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
    # dataset: [speaker; time; content]
    return dataset

def extract_content(dataset, minimum_length):
    content_dataset_index = []
    content = []
    for i in range(len(dataset)):
        if len(dataset[i][2].split(" ")) > minimum_length:
            content.append(dataset[i][2])
            content_dataset_index.append([i])
        else:
            if i == 0:
                content.append(dataset[i][2])
                content_dataset_index.append([i])
            else:
                content[-1] = content[-1] + " "+ dataset[i][2]
                content_dataset_index[-1].append(i)

    # for i in range(len(content)):
    #     print "content          " + content[i]
    #     content_dataset_index.append([])
    #     for j in range(len(dataset)):
    #         print "dataset          " +dataset[j][2]
    #         content_dataset_index[i] = []
    #         if dataset[j][2] in content[i]:
    #             print "yes"
    #             content_dataset_index[i].append(j)print content_dataset_index, len(content_dataset_index)
    # f = open('grouptext.txt', 'w')
    # for i in range(len(content)):
    #     f.write(content[i]+'\n')
    # f.close()
    return content,content_dataset_index

def remove_stopwords(content, stopwordsPath):
    with open(stopwordsPath) as f:
        stopwords = f.readlines()
    f.close()
    stopwords = [x.strip() for x in stopwords]

    content_words = content.split(" ")
    content = ''
    for i in range(len(content_words)):
        stripWord = content_words[i].replace(",","").replace(".","")
        if stripWord not in stopwords:
            content = content + stripWord + " "

    # sentence without stopwords
    return content

def lda_extract_topics(content, topic_num, stopwordsPath):

    tdm = textmining.TermDocumentMatrix()

    if isinstance(content, list):
        for i in range(len(content)):
            content[i] = remove_stopwords(content[i],stopwordsPath)
            tdm.add_doc(content[i])
          
    elif isinstance(content, basestring):
        content = remove_stopwords(content,stopwordsPath)
        tdm.add_doc(content)
    else:
        print "dataset fail to load"

    # create a temp variable with doc-term info
    temp = list(tdm.rows(cutoff=1))
    # get the vocab from first row
    vocab = tuple(temp[0])
    # get document-term matrix from remaining rows
    X = np.array(temp[1:])

    n_topics=topic_num
    model = lda.LDA(n_topics=n_topics, n_iter=3000, random_state=1)
    model.fit(X)  # model.fit_transform(X) is also available
    topic_word = model.topic_word_  # model.components_ also works
    n_top_words = 10
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
        print('Topic {}: {}'.format(i, ' '.join(topic_words)))

    doc_topic = model.doc_topic_

    
    topic_index_array = np.arange(n_topics)

    doc_num = len(content)

    # docTopicArray is topic distribution for each doc
    docTopicArray = []
    top_topics_num = 10
    for n in range(doc_num):
        #topic_most = np.array(topic_index_array)[np.argsort(doc_topic[n])][:-(top_topics_num+1):-1]
        docTopicArray.append(doc_topic[n])
        #print("doc: {} topic: {}...".format(n,' '.join(str(x) for x in topic_most)))

    return docTopicArray

def group_docs(content, docTopicArray,similarityThreshold):
    # cluster same topic sentence
    simiArray = []
    for i in range(len(docTopicArray)-1):
        result = 1 - spatial.distance.cosine(docTopicArray[i], docTopicArray[i+1])
        simiArray.append(result)
        print "doc "+ str(i) + "   and   doc " + str(i+1) + "   " + str(result)

    splitArray = []
    for j in range(len(simiArray)):
        if simiArray[j] < similarityThreshold:
            splitArray.append(j)

    contentArray = np.arange(len(content))
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
    return contentGroupArray

def content_groupedByTopic(content,contentGroupArray):
    groupContent = []
    for i in range(len(contentGroupArray)):
        for j in range(len(contentGroupArray[i])):
            groupList = []
            groupList.append(content[contentGroupArray[i][j]])
        group = ' '.join(groupList)
        groupContent.append(group)
    return groupContent

def extract_keywords_for_topic(groupContent, stopwordsPath):
    rake = Rake(stopwordsPath)
    keywordsList = []
    rakeList = [] #[[('short-term secretion lot guys concerned lot information movies', 64.0),(..),[..]]
    for i in range(len(groupContent)):
        keywords = rake.run(groupContent[i])
        # print "\n group "+str(i)+": "
        # print keywords
        rakeList.append(keywords)
        keywordsList.append(keywords[0][0].split(" "))
    return keywordsList

def return_json_data(dataset,content,docTopicArray,contentGroupArray,content_dataset_index,keywordsList):
    data = []
    for i in range(len(contentGroupArray)):
        data.append({})
        data[i]["startTime"] = dataset[content_dataset_index[contentGroupArray[i][0]][0]][1]
        #duration
        if len(contentGroupArray) >1 and contentGroupArray[i] != contentGroupArray[-1]:
            data[i]["topicDuration"] = time_format(dataset[content_dataset_index[contentGroupArray[i][-1]][0]][1]) - time_format(dataset[content_dataset_index[contentGroupArray[i][0]][0]][1])
        elif contentGroupArray[i] == contentGroupArray[-1] and len(contentGroupArray) >1:
            data[i]["topicDuration"] = time_format(dataset[content_dataset_index[contentGroupArray[i][-1]][0]][1]) - time_format(dataset[content_dataset_index[contentGroupArray[i][0]][0]][1]) +5 # last sentence time
        else:
            data[i]["topicDuration"] = time_format(dataset[content_dataset_index[contentGroupArray[i][-1]][0]][1])
        data[i]["sentences"] = []
        index = 0
        for j in range(len(contentGroupArray[i])):
            for k in range(len(content_dataset_index[contentGroupArray[i][j]])):
                
                data[i]["sentences"].append({})
                data[i]["sentences"][index]["sentenceTime"] = dataset[content_dataset_index[contentGroupArray[i][j]][k]][1]
                data[i]["sentences"][index]["sentenceContent"] = dataset[content_dataset_index[contentGroupArray[i][j]][k]][2]
                data[i]["sentences"][index]["sentenceSpeaker"] = dataset[content_dataset_index[contentGroupArray[i][j]][k]][0]
                index += 1
        data[i]["keywords"] = []
        for l in range(len(keywordsList[i])):
            data[i]["keywords"].append({})
            data[i]["keywords"][l]["keyword"] = keywordsList[i][l]
        data[i]["topicName"] = keywordsList[i][0]+" "+keywordsList[i][1]
    return data

def time_format(str):
    strlist = str.split(":")
    time = int(strlist[0])*3600 + int(strlist[1])*60 +int(strlist[0])
    return time

class datasetLDA(object):
    def __init__(self, dataset_file_path):
        self.file_name = dataset_file_path

    def run(self):
        #para
        minimum_length = 30 # cluster short sentence to one doc, minimum 30
        topic_num = 7
        similarityThreshold = 0.35
        stopwordsPath = "pythonLibrary/SmartStoplist.txt"

        file_name = self.file_name 
        #dataset format  [[speaker,starttime,transcript],[..]
        dataset = read_datafile(file_name)
        #content: group sentences, list
        content,content_dataset_index = extract_content(dataset, minimum_length)
        #each doc: [] distribution for each topic
        docTopicArray = lda_extract_topics(content, topic_num, stopwordsPath)
        #sentence array is divided into arrays by topics, like [[0,1],[2,3,4,5],[6]]
        contentGroupArray = group_docs(content, docTopicArray, similarityThreshold)
        #content with different topics, [[fddfas],[sfsdf]]
        groupContent = content_groupedByTopic(content,contentGroupArray)
        keywordsList = extract_keywords_for_topic(groupContent,stopwordsPath)
        data = return_json_data(dataset,content,docTopicArray,contentGroupArray,content_dataset_index, keywordsList)
        return data

if __name__ == "__main__":

    datasetLDA = datasetLDA("dataset.txt")
    datasetLDA.run()
    













