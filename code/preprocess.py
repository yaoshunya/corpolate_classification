import pandas as pd
import pdb
import numpy as np
import tensorflow as tf
import MeCab
from gensim.models import word2vec

if __name__ ==  '__main__':

    df = pd.read_csv("../data/corporation_sample.csv")

    mt = MeCab.Tagger('')
    mt.parse('') 
  	 
    model = word2vec.Word2Vec.load("../data/wiki.model")

    title = df['title']
    description = df['description']
    y = df['class']
    pdb.set_trace()
