from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import re
import pandas as pd
import nltk

# nltk.download('punkt')
# nltk.download('stopwords')


def remove_stopwords(sentence):
    """ Removes stop words in the passed sentence """

    stop_words = set(stopwords.words('english'))
    new_sentence = " ".join([i for i in sentence if i not in stop_words])
    return new_sentence


def tokenize(data):
    """ Performs sentence tokenization """

    content = ""
    for paragraph_content in data:
        content += paragraph_content.text

    sentences = nltk.sent_tokenize(content)
    return sentences


def preprocess(sentences):
    """
    Preprocesses the sentences passed in as a parameter &
    returns cleaned sentences
    """

    # Removing special characters,punctuation, whitespaces and converting to lowercase
    clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")
    clean_sentences = [re.sub(r'\[[0-9]*\]', ' ', s) for s in clean_sentences]
    clean_sentences = [re.sub(r'\s+', ' ', s) for s in clean_sentences]
    clean_sentences = [s.lstrip() for s in clean_sentences]
    clean_sentences = [s.rstrip() for s in clean_sentences]
    clean_sentences = [s.lower() for s in clean_sentences]

    # Removing stopwords
    clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]

    return clean_sentences


def clean_summary(x):
    """ Returns a cleaned summary """

    # summ = pd.Series(x).str.replace("[^a-zA-Z]", " ")
    summ = [re.sub(r'\[[0-9]*\]', ' ', s) for s in x]
    summ = [re.sub(r'\s+', ' ', s) for s in summ]

    summary = ""
    for i in range(len(summ)):
        summary += summ[i]

    return summary
