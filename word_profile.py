## Course Project PCL1 HS21
## Part1Step2
# Author(s): Eric Szabó Félix, Viviane Walker
# date: 30th December 2021


import csv
import math


def word_pattern(document_in, word):
    """"We are creating a pattern using a given the following parameters: Two dependencies with their relation in between,
    a document to read out the sentences and a file to put out the matches . No anchor words were used, since according
    to the task we are only required to search for dependencies. This is the skeleton, in which the parameters will be
    filled in."""

    with open(document_in) as data:
        dataset = csv.reader(data, delimiter="\t", quotechar='"')
        match_set = {}
        match_set_word = {}
        for row in dataset:
            if word in row:
                for term in row:
                    if term not in match_set_word:
                        match_set_word[term] = 0
                    match_set_word[term] += 1
            for term in row:
                if term not in match_set:
                    match_set[term] = 0
                match_set[term] += 1
        freq_list_raw_freq = list(sorted(match_set.items(), key=lambda item: item[1], reverse=True))
        freq_list_matched = list(sorted(match_set_word.items(), key= lambda item: item[1], reverse=True))
        # print(freq_list_raw_freq)
        # print(freq_list_matched)
        if len(freq_list_matched) != 0:
            for x in range(len(freq_list_raw_freq)):
                #print(freq_list_raw_freq[x][0])
                if freq_list_raw_freq[x][0]==freq_list_matched[1][0]:
                    raw_freq = freq_list_raw_freq[x][1]
                if freq_list_raw_freq[x][0]==word:
                    word_freq = freq_list_raw_freq[x][1]
            print('\n' + 'The word', '\'' + freq_list_matched[0][0] + '\'', 'occurs this often:', freq_list_matched[0][1])
            print('The raw frequency of', '\'' + freq_list_matched[1][0] + '\'', 'using', document_in, 'is:', freq_list_matched[1][1])
            print('The logDice of', '\'' + freq_list_matched[1][0] + '\'', 'is:', 14 + math.log2(2 * freq_list_matched[1][1] /(word_freq + raw_freq)))
        else:
            print("Invalid, due to one or more of the values being 0.")




# Here are the function calls which give the parameters Dep1, Relation, Dep2, and the two files (in and out):

word_pattern("Baum_profile_sb_News_2007_data.tsv", "Baum")
word_pattern("Baum_profile_object_News_2007_data.tsv", "Baum")
word_pattern("Baum_profile_sb_News_2016_data.tsv", "Baum")
word_pattern("Baum_profile_object_News_2016_data.tsv", "Baum")
word_pattern("Baum_profile_sb_Wikipedia_2007_data.tsv", "Baum")
word_pattern("Baum_profile_object_Wikipedia_2007_data.tsv", "Baum")
word_pattern("Baum_profile_sb_Wikipedia_2016_data.tsv", "Baum")
word_pattern("Baum_profile_object_Wikipedia_2016_data.tsv", "Baum")

word_pattern("schoen_profile_nk_News_2002_data.tsv", "schön")
word_pattern("schoen_profile_pd_News_2002_data.tsv", "schön")
word_pattern("schoen_profile_nk_News_2019_data.tsv", "schön")
word_pattern("schoen_profile_pd_News_2019_data.tsv", "schön")
word_pattern("schoen_profile_nk_Web_2002_data.tsv", "schön")
word_pattern("schoen_profile_pd_Web_2002_data.tsv", "schön")
word_pattern("schoen_profile_nk_Web-public_2019_data.tsv", "schön")
word_pattern("schoen_profile_pd_Web-public_2019_data.tsv", "schön")

word_pattern("ist_profile_ROOT_Web-EU_2015_data.tsv", "ist")
word_pattern("ist_profile_oc_Web-EU_2015_data.tsv", "ist")
word_pattern("ist_profile_ROOT_Web-EU_2017_data.tsv", "ist")
word_pattern("ist_profile_oc_Web-EU_2017_data.tsv", "ist")
word_pattern("ist_profile_ROOT_Wikipedia_2010_data.tsv", "ist")
word_pattern("ist_profile_oc_Wikipedia_2010_data.tsv", "ist")
word_pattern("ist_profile_ROOT_Wikipedia_2014_data.tsv", "ist")
word_pattern("ist_profile_oc_Wikipedia_2014_data.tsv", "ist")