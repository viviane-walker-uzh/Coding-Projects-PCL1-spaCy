## Course Project PCL1 HS21
## Part1Step1
# Author(s): Eric SzabÃ³ FÃ©lix, Viviane Walker
# date: 30th December 2021


import sys
import spacy

## run the two following lines for installig parser and lemmatizer in german! 
# pip3 install spacy
# python3 -m spacy download de_core_news_sm

def parser():
    """ this function parses an input file through the 
    spacy pipeline and saves its parsed as a spacy file"""

    nlp = spacy.load('de_core_news_sm')
    output_f = sys.argv[2]
    with open(sys.argv[1], "r") as input_f:
        input_f = input_f.read()
        doc = nlp(input_f)
        doc.to_disk(output_f)

parser()

# Copy the following terminal command and run them in the terminal one by one in order to parse the single txt files:

# python3 parse_corpus.py Baum_News_2007_corpus.txt Baum_News_2007_corpus.spacy
# python3 parse_corpus.py Baum_News_2016_corpus.txt Baum_News_2016_corpus.spacy
# python3 parse_corpus.py Baum_Wikipedia_2007_corpus.txt Baum_Wikipedia_2007_corpus.spacy
# python3 parse_corpus.py Baum_Wikipedia_2016_corpus.txt Baum_Wikipedia_2016_corpus.spacy

# python3 parse_corpus.py schoen_News_2002_corpus.txt schoen_News_2002_corpus.spacy
# python3 parse_corpus.py schoen_News_2019_corpus.txt schoen_News_2019_corpus.spacy
# python3 parse_corpus.py schoen_Web_2002_corpus.txt schoen_Web_2002_corpus.spacy
# python3 parse_corpus.py schoen_Web-public_2019_corpus.txt schoen_Web-public_2019_corpus.spacy

# python3 parse_corpus.py ist_Wikipedia_2010_corpus.txt ist_Wikipedia_2010_corpus.spacy
# python3 parse_corpus.py ist_Wikipedia_2014_corpus.txt ist_Wikipedia_2014_corpus.spacy
# python3 parse_corpus.py ist_Web-EU_2015_corpus.txt ist_Web-EU_2015_corpus.spacy
# python3 parse_corpus.py ist_Web-EU_2017_corpus.txt ist_Web-EU_2017_corpus.spacy
