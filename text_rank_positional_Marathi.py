from __future__ import print_function
import streamlit as st
import collections
import io
import math
import operator
import sys
import networkx as nx
from preprocess import cleanText
import nltk
nltk.download('punkt_tab')

window = 10
numberofSentences = 6
nodeHash = {}
textRank = {}
sentenceDictionary = collections.defaultdict(dict)
size = 0
sentences = []


def generatepositionaldistribution():
    global nodeHash, sentenceDictionary, sentences, size
    positional_dictionary = collections.defaultdict(dict)
    count = 0
    for i in sentenceDictionary.keys():
        for j in range(0, len(sentenceDictionary[i])):
            count += 1
            position = float(count) / (float(size) + 1.0)
            positional_dictionary[i][j] = 1.0 / \
                (math.pi * math.sqrt(position * (1 - position)))
            word = sentenceDictionary[i][j]
            if word in nodeHash:
                if nodeHash[word] < positional_dictionary[i][j]:
                    nodeHash[word] = positional_dictionary[i][j]
            else:
                nodeHash[word] = positional_dictionary[i][j]


def textrank():
    '''
        Generates a graph based ranking model for the tokens
    :return: Keyphrases that are most relevant for generating the summary.
    '''
    global sentenceDictionary, nodeHash, textRank
    graph = nx.Graph()
    graph.add_nodes_from(nodeHash.keys())
    for i in sentenceDictionary.keys():
        for j in range(0, len(sentenceDictionary[i])):
            current_word = sentenceDictionary[i][j]
            next_words = sentenceDictionary[i][j + 1:j + window]
            for word in next_words:
                graph.add_edge(current_word, word, weight=(
                    nodeHash[current_word] + nodeHash[word]) / 2)
    textRank = nx.pagerank(graph, weight='weight')
    keyphrases = sorted(textRank, key=textRank.get, reverse=True)[:n]
    return keyphrases


def summarize(filePath, keyphrases, numberofSentences):
    '''
        Generates the summary and writes the summary to the file.
    :param filePath: path of file to be used for summarization.
    :param keyphrases: Extracted keyphrases
    :param numberofSentences: Number of sentences needed as a summary
    :output: Writes the summary to the file
    '''
    global textRank, sentenceDictionary, sentences
    sentenceScore = {}
    for i in sentenceDictionary.keys():
        position = float(i + 1) / (float(len(sentences)) + 1.0)
        positionalFeatureWeight = 1.0 / \
            (math.pi * math.sqrt(position * (1.0 - position)))
        sumKeyPhrases = 0.0
        for keyphrase in keyphrases:
            if keyphrase in sentenceDictionary[i]:
                sumKeyPhrases += textRank[keyphrase]
        sentenceScore[i] = sumKeyPhrases * positionalFeatureWeight
    sortedSentenceScores = sorted(sentenceScore.items(
    ), key=operator.itemgetter(1), reverse=True)[:numberofSentences]
    sortedSentenceScores = sorted(
        sortedSentenceScores, key=operator.itemgetter(0), reverse=False)
    print("\nSummary: ")
    summary = []
    arr = []
    # for keyphrase in keyphrases:
    #     print(keyphrase)
    # print(keyphrases)

    for i in range(0, len(sortedSentenceScores)):
        arr.append(sentences[sortedSentenceScores[i][0]])
    s = "".join(arr)
    # print(s)
    return (s)


def process(text_data):
    global window, n, numberofSentences, textRank, sentenceDictionary, size, sentences
    if text_data is not None:
        sentenceDictionary, sentences, size = cleanText(text_data)  # Use the string content
        window = 6
        numberofSentences = 5
        n = int(math.ceil(min(0.1 * size, 7 * math.log(size))))
        generatepositionaldistribution()
        keyphrases = textrank()
        t = summarize(text_data, keyphrases, numberofSentences)
        return t
    else:
        print("Not enough parameters")

