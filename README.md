# Coding-Projects-PCL1-spaCy

# Project 2021 : Computing Syntactic Word Profiles using

# SpaCy

## Remarks on submission

- Always name your submissions as follows:
olatusername_pcl1_exnumber.txt/pdf/py/zip
- Learning partnerships in pairs are desirable. In this case, p lease name your sub-
mission username1_username2_pcl1_exnumber.txt/pdf/py/zip
- Please state first and last names on the submission form - in the case of learn-
ing p artnerships, the names of both students.
- Add a Doc-string to every function you write and add comments to your
code. They don’t just help the tutors to understand what you’re thinking, but can
also help you to find and fix p ossible bugs.
- Please number the tasks on the submission sheet/Python p rograms the same as
on the task sheet.
- Hand in: Part 0 Step 1 by December 9th at 18:00, the remaining p arts by De-
cember 31st at 18:00. Make sure to hand in on time!
- This exercise will take more time to solve than the previous ones, p lease start
early. We really recommend doing this exercise in teams.
- Grading: In total you can earn 3 p oints, distributed in the following way: Part
0 will be the p reprocessing of the data and you will not earn sp ecific p oints for
this p art, although it is necessary to solve the following p arts. Part 1 will earn
you 1 point and for part 2 and 3 you will receive 1.5 p oints total. The remaining
0.5 p oints will be given for the quality of your comments and doc strings as well
as the functions and data structures you choose considered for all p arts.
**- Important** : We don’t want you to suffer! If there are any questions, please
p ost a question in the forum / write an email / ask us in the tutorial!

## Introduction

The final goal of this p roject will be to calculate word p rofiles based on syntactic
collocations. A good examp le for word p rofiles in German is the DWDS

(https://www.dwds.de/wp/) and we will basically try to reimplement it p artially.

Please take a look at this web application and search for different words to get a
feeling of how word p rofiles look like. Note that they use a lemmatized rep resen-
tation of words. We will also comp ute both collocation measures they p rovide:
The raw frequency and the logDice (p lease read this p aper under

https://nlp.fi.muni.cz/raslan/2008/papers/13.pdf), to better understand the motiva-

tion behind it.


## Part 0: Preprocessing

Step 1: Choose a language, target words and construction type

You are free to choose a language for this p roject if Sp aCy has a dep endency
p arser for this language (a list of all these languages can be found under
https://spacy.io/usage/models).
Carefully choose three interesting words from this language that have different
UPOS tags and for each of these three words choose two suitable dependency-
oriented syntactical constructions based on which you will calculate the con-
struction sp ecific collocation. Choose a construction that occurs reasonably often
with your target word as to not run into data sparsity p roblems during the analysis
later.
Deliverable: As the idea is that all of you should choose different target words
and constructions for this p roject, p ost your choice in the resp ective thread on
OLAT by 9 th of December at 18:00.

Step 2: Formulate your hypotheses

Based on these selections formulate a corp us linguistics hypothesis with your ex-
p ectations: Which words will co-occur how most frequently in your chosen con-
struction with your target word most often (these are referred to from now on as
p artner words)? Will these accurately reflect the most important partner words for
your target and construction? What influence will different text sorts such as ei-
ther news or web articles have? What difference could different time p eriods
make?

Deliverable: A descrip tion of your hypothesis for every target word and construc-
tion p air p er time p eriod and text type.

Step 3 : Build specific corpora for each target word

On the web p age of Wortschatz Leip zig (https://wortschatz.uni-leipzig.de/de/down-
load/German#deu_news_2020) you can find corp ora from different languages and
text types (news, web and wikipedia) and time periods. Choose and download one
from either text sort and from different time p eriods that you think will hold the
most occurrences for each of your constructions and target words and are con-
nected to your hypothesis. Inside the downloaded unzipped folder you will find a
sentence-segmented corp us. Use this corp us to search (either using grep or Py-
thon) for sentences that contain your target words, extract and save those, there-
fore creating one mini corp us p er target word, time p eriod and text type. Keep
inflected word forms in mind while you search!


Make sure that each of your mini corp ora has at least 100 sentences as a smaller
amount will cause p roblems for the following statistical collocation analysis. If
you do not have enough occurrences try to use different text types from different
years or extract from more than one corpus.

Deliverable: One sentence segmented mini corp us for each of your target words,
text typ es and time p eriods as a .txt file named [word]_[text typ e]_[time p e-
riod]_corpus.txt.

## Part 1 : Extract dependency constructions using SpaCy

Step 1: Sentence parsing using SpaCy

Deliverable: The p ython scrip t used to p arse the corp ora with Sp aCy named
p arse_corpus.py (accep ting in- and output files as command line arguements) and
the p arsed version of each mini corp us named [word]_[text typ e]_[time p e-
riod]_corpus.spacy.

Step 2: Extracting the relevant constructions

In a sep arate Python script you will then reload the p arsed version of each mini
corp us and extract all the relevant constructions into sperate files. For this, p lease

use the Dep endencyMatcher (https://spacy.io/api/dependencymatcher, tutorial mate-
rial) from Sp aCy. Iterate over each sentence with this matcher and if you match

the construction save the lemmas that contribute to it sep arated by a tabulator in
a .tsv file. Please note that we are only sampling for the construction here, so it is

p ossible that your target word may not be one of the two words contributing to
the construction and still save those examples in the .tsv file as they will be rele-
vant for the analysis later.
The Sp aCy lemmatizer is not always very good. Try to fix missing lemmatizations

of Sp aCy in your code by creating a data structure that can be used efficiently and

can be easily extended if you would need to create word p rofiles for other words.

Hint: In order to figure out the specifics of the matcher class it can be help ful to
manually create a small samp le file where you know the outcome of the matches
(you can also use displacy to familiarize yourself with the tags and structures used
by Sp aCy). Here you can find a tutorial to get started with SpaCy
(https://course.spacy.io/en/chapter1). However, you will not need to deliver this.

First write a Python script that iterates through each of your mini corpora and
passes each sentence through the SpaCy pipeline to parse it. Save the parsed ver-
sion of each corpus separately with SpaCy’s .to_disk() method.


Deliverables: The p ython scrip t used for extracting the relevant constructions
called extract_constructions.py and the resulting files (one for each construction
and target word p air p er time p eriod and text type) named [word]_profile_[con-
struction]_[text type]_[time p eriod]_data.tsv.

## Part 2 : Creating the profile

Step 1: Calculating the measures

Take your [word]_profile_[construction]_[text type]_[time p eriod]_data.tsv files
and go through them line p er line. For each p artner word that you find together
with your word in one line calculate the frequency and logDice of this p air. At the
end p rint out the top p artner words, once sorted by their frequency and once by
their logDice. Do this sep arately for your chosen text types and time p eriods for a
comp arison.

For the logDice use the following formula: 14 +log 2 (

2 ∗𝑓𝑥𝑦
𝑓𝑥+𝑓𝑦), where 𝑓𝑥𝑦^ denotes
the frequency of your target word (x) and the respective p artner word (y) occur-
ring together on one line, 𝑓𝑥 is the frequency of your target word occurring in the
[word]_profile_[construction]_data.tsv file, regardless of the other word on the

line and 𝑓𝑦 is the frequency of the resp ective p artner word in the [word]_pro-
file_[construction]_data.tsv file in the second column, regardless of the word oc-
curring in the first column. Make sure to calculate 𝑓𝑦 p er lemma (each token in

the doc should already have a lemma assigned).

Deliverables: The Python script used to solve this task named word_profile.py.

Step 2 : Keyword concordance

In the p revious step, you found the most frequent constructions of a target word.
In this step , the goal is to p rint out some of these constructions in the context of a
sentence. Similar to what DWDS does with its example sentences. Create a new
Python file. In it, define a function named context. It should accep t the following
inp uts:

- a p arsed corpus
- a target word
- a construction name
- an integer which determines the maximum number of randomly samples
    sentences that function returns


Make it p ossible to sp ecify all these p arameters with command-line arguments.

The function should search for the construction in the p arsed corpus, randomly
select the desired number of sentences and return them.

Deliverables: The p ython script used to solve this task named keyword_concord-
ance.p y.

## Part 3 : Evaluation of your hypothesis

Did you find your hyp otheses for each word and construction from Part 0 con-
firmed in your empirical results? Which one of the two measures do you find more
intuitive: LogDice or the raw frequencies? Did you find anything surprising? Does
our ap proach have flaws or weaknesses? What do you think about SpaCy’s lem-
matizer p erformance for your language?

Deliverables: Your reflection on your findings and the task (one to two sentences
p er question/word) in either English or German.

```
Have fun with creating statistical word p rofiles!
```

