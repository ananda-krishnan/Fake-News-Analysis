#Data Ananlysis Project for detecting Fake and Real News

import numpy as np

import pandas as pd

import itertools

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import PassiveAggressiveClassifier

from sklearn.metrics import accuracy_score, confusion_matrix

df=pd.read_csv('D:\\DataAnalysis Projects\\news.csv')

df.shape


df.head

