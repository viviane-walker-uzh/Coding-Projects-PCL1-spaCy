## Course Project PCL1 HS21
## Part2Step2
# Author(s): Eric Szabó Félix, Viviane Walker
# date: 30th December 2021

import spacy
from spacy.matcher import DependencyMatcher
from spacy.tokens import Doc
import random

# run the two following lines for installig parser and lemmatizer in german!
# pip3 install spacy
# python3 -m spacy download de_core_news_sm

nlp = spacy.load("de_core_news_sm")
matcher = DependencyMatcher(nlp.vocab)


def context(corpus, target_word, construction_name, number):
    """In this function we use the following parameters: a spacy file, a target word, dependencies and an integer to set
    the number of randomly selected sentences"""
    # Here we check whether the file entered by the user is eligible or not:
    if corpus.endswith('.spacy'):
        # If it is so, we read the file into the function
        doc = Doc(nlp.vocab).from_disk(corpus)
        # We create some if statements, to account for all different constructions. Since some head-dependency
        # structures go in different direction, there is no easy way to deal with this, without adding another
        # parameter. The task only permits 4.
        if construction_name != 'ROOT' or 'oc':
            # The patterns are similar to the ones used in extract_constructions.py. See there for further explanations.
            pattern = [
                # target dependency will be filled up here
                {
                    "RIGHT_ID": "verb",
                    "RIGHT_ATTRS": {"DEP": 'ROOT'}
                },
                # partner dependency to be filled here
                {
                    "LEFT_ID": "verb",
                    "REL_OP": ">",
                    "RIGHT_ID": "word",
                    "RIGHT_ATTRS": {"LEMMA": target_word, "DEP": construction_name}
                }
            ]
            matcher.add("word", [pattern])
            matches = matcher(doc)
        if target_word == 'schön' and construction_name == 'pd':
            pattern = [
                # target dependency will be filled up here
                {
                    "RIGHT_ID": "verb",
                    "RIGHT_ATTRS": {"DEP": 'ROOT'}
                },
                # partner dependency to be filled here
                {
                    "LEFT_ID": "verb",
                    "REL_OP": ">",
                    "RIGHT_ID": "word",
                    "RIGHT_ATTRS": {"LEMMA": target_word, "DEP": construction_name}
                }
            ]
            matcher.add("word", [pattern])
            matches = matcher(doc)

        if target_word == 'schön' and construction_name == 'nk':
            pattern = [
                # target dependency will be filled up here
                {
                    "RIGHT_ID": "verb",
                    "RIGHT_ATTRS": {"DEP": 'nk'}
                },
                # partner dependency to be filled here
                {
                    "LEFT_ID": "verb",
                    "REL_OP": ">",
                    "RIGHT_ID": "word",
                    "RIGHT_ATTRS": {"LEMMA": target_word, "DEP": construction_name}
                }
            ]
            matcher.add("word", [pattern])
            matches = matcher(doc)

        if construction_name == 'ROOT' or 'oc':
            pattern = [
                # target dependency will be filled up here
                {
                    "RIGHT_ID": "verb",
                    "RIGHT_ATTRS": {"LEMMA": target_word, "DEP": construction_name}
                },
                # partner dependency to be filled here
                {
                    "LEFT_ID": "verb",
                    "REL_OP": ">",
                    "RIGHT_ID": "predicate",
                    "RIGHT_ATTRS": {"DEP": 'pd'}
                }
            ]
            matcher.add("word", [pattern])
            matches = matcher(doc)

        # Here we make sure that spacy gives us sentences to work with
        sentences = [i for i in nlp(doc).sents]
        # A dictionary is created to account for all sentences that match the parameters
        matched_sentences = {}
        # A variable y is created to account for all matches found in matches. These are lists with two items in them
        for x in matches:
            y = x[1]
            for sentence in range(len(sentences)):
                # Here we check for the matches in the y list against the sentences. If a match is found,
                # the sentence is added to the dictionary
                if doc[y[0]] and doc[y[1]] in sentences[sentence]:
                    matched_sentences[sentences[sentence]] = 0
        # A random sample is selected, with key setting the amount of sentences to be printed. The if statement makes
        # sure we are not asking for more than the script can give
        if number <= len(matched_sentences):
            selection = random.sample(list(matched_sentences), k=number)
            for item in selection:
                print('\n' + str(item).rstrip().lstrip())
        else:
            print('The number you chose exceeds the amount of matches given current parameters or is negative. '
                  'Please '
                  'choose a lower, positive number.')

    # If file format does not match, user is asked to use another file
    else:
        print('Please make sure to use a \'*.spacy\' file format.')


# When executing the function, the user will now be asked to enter the following parameters:

context(input('Please enter corpus file name:\n'), input('Please choose a German lemma:\n'), input('Please enter a '
                                                                                                   'German dependency'
                                                                                                   ' value:\n'),
        int(input('Please enter the amount of samples to be generated:\n')))

# Uncomment to execute the following examples:

# context('Baum_News_2007_corpus.spacy', 'Baum', 'sb', 5)
# context('ist_Web-EU_2015_corpus.spacy', 'sein', 'ROOT', 5)
# context('schoen_Web-public_2019_corpus.spacy', 'schön', 'nk', 5)
# context('schoen_Web-public_2019_corpus.spacy', 'schön', 'pd', 5)
