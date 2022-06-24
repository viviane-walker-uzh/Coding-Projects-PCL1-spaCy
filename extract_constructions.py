## Course Project PCL1 HS21
## Part1Step2
# Author(s): Eric Szabó Félix, Viviane Walker
# date: 30th December 2021

import spacy
from spacy.matcher import DependencyMatcher
from spacy.tokens import Doc

# run the two following lines for installig parser and lemmatizer in german!
# pip3 install spacy
# python3 -m spacy download de_core_news_sm


nlp = spacy.load("de_core_news_sm")
matcher = DependencyMatcher(nlp.vocab)

def word_pattern(dep_1, relation, dep_2, document_in, document_out):
    """We are creating a pattern using a given the following parameters: Two dependencies with their relation in between,
    a document to read out the sentences and a file to put out the matches . No anchor words were used, since according
    to the task we are only required to search for dependencies. This is the skeleton, in which the parameters will be
    filled in."""
    pattern = [
        # target dependency will be filled up here
        {
            "RIGHT_ID": "word",
            "RIGHT_ATTRS": {"DEP": dep_1}
        },
        # partner dependency to be filled here
        {
            "LEFT_ID": "word",
            "REL_OP": relation,
            "RIGHT_ID": "verb",
            "RIGHT_ATTRS": {"DEP": dep_2}
        }
    ]
    matcher.add("word", [pattern])

    # here is where the script takes the sample sentences from
    doc = Doc(nlp.vocab).from_disk(document_in)
    matches = matcher(doc)
    with open(document_out, "w") as file_out:
        for x in matches:
            y = x[1]
            # the following line is optional, but helps seeing what dependencies it matches
            #print(doc[y[0]].head.dep_, doc[y[1]].head.dep_)
            # use this to see more context of the matched words
            # if y[0] <= y[1]:
            #    print(doc[y[0]-3:y[1]+3])
            # else:
            #    print(doc[y[1]-3:y[0]+3])
            file_out.write(doc[y[0]].text + '\t' + doc[y[1]].text + '\n')

# Here the function takes the parameters. Dep1, Relation, Dep2, and the two files (in and out).

word_pattern("sb", "<", "ROOT", "Baum_News_2007_corpus.spacy", "Baum_profile_sb_News_2007_data.tsv")
word_pattern({"IN": ["oa", "og", "da"]}, "<", "ROOT", "Baum_News_2007_corpus.spacy",
             "Baum_profile_object_News_2007_data.tsv")
word_pattern("sb", "<", "ROOT", "Baum_News_2016_corpus.spacy", "Baum_profile_sb_News_2016_data.tsv")
word_pattern({"IN": ["oa", "og", "da"]}, "<", "ROOT", "Baum_News_2016_corpus.spacy",
             "Baum_profile_object_News_2016_data.tsv")
word_pattern("sb", "<", "ROOT", "Baum_Wikipedia_2007_corpus.spacy", "Baum_profile_sb_Wikipedia_2007_data.tsv")
word_pattern({"IN": ["oa", "og", "da"]}, "<", "ROOT", "Baum_Wikipedia_2007_corpus.spacy",
             "Baum_profile_object_Wikipedia_2007_data.tsv")
word_pattern("sb", "<", "ROOT", "Baum_Wikipedia_2016_corpus.spacy", "Baum_profile_sb_Wikipedia_2016_data.tsv")
word_pattern({"IN": ["oa", "og", "da"]}, "<", "ROOT", "Baum_Wikipedia_2016_corpus.spacy",
             "Baum_profile_object_Wikipedia_2016_data.tsv")
word_pattern("nk", "<", "nk", "schoen_News_2002_corpus.spacy", "schoen_profile_nk_News_2002_data.tsv")
word_pattern("pd", "<", "ROOT", "schoen_News_2002_corpus.spacy", "schoen_profile_pd_News_2002_data.tsv")
word_pattern("nk", "<", "nk", "schoen_News_2019_corpus.spacy", "schoen_profile_nk_News_2019_data.tsv")
word_pattern("pd", "<", "ROOT", "schoen_News_2019_corpus.spacy", "schoen_profile_pd_News_2019_data.tsv")
word_pattern("nk", "<", "nk", "schoen_Web_2002_corpus.spacy", "schoen_profile_nk_Web_2002_data.tsv")
word_pattern("pd", "<", "ROOT", "schoen_Web_2002_corpus.spacy", "schoen_profile_pd_Web_2002_data.tsv")
word_pattern("nk", "<", "nk", "schoen_Web-public_2019_corpus.spacy", "schoen_profile_nk_Web-public_2019_data.tsv")
word_pattern("pd", "<", "ROOT", "schoen_Web-public_2019_corpus.spacy", "schoen_profile_pd_Web-public_2019_data.tsv")
word_pattern("ROOT", ">", "pd", "ist_Web-EU_2015_corpus.spacy", "ist_profile_ROOT_Web-EU_2015_data.tsv")
word_pattern("oc", ">", "pd", "ist_Web-EU_2015_corpus.spacy", "ist_profile_oc_Web-EU_2015_data.tsv")
word_pattern("ROOT", ">", "pd", "ist_Web-EU_2017_corpus.spacy", "ist_profile_ROOT_Web-EU_2017_data.tsv")
word_pattern("oc", ">", "pd", "ist_Web-EU_2017_corpus.spacy", "ist_profile_oc_Web-EU_2017_data.tsv")
word_pattern("ROOT", ">", "pd", "ist_Wikipedia_2010_corpus.spacy", "ist_profile_ROOT_Wikipedia_2010_data.tsv")
word_pattern("oc", ">", "pd", "ist_Wikipedia_2010_corpus.spacy", "ist_profile_oc_Wikipedia_2010_data.tsv")
word_pattern("ROOT", ">", "pd", "ist_Wikipedia_2014_corpus.spacy", "ist_profile_ROOT_Wikipedia_2014_data.tsv")
word_pattern("oc", ">", "pd", "ist_Wikipedia_2014_corpus.spacy", "ist_profile_oc_Wikipedia_2014_data.tsv")