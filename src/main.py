import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# データセット読み込み
DATA_TRAIN = pd.read_csv('../dataset/train.csv')
DATA_TEST = pd.read_csv('../dataset/test.csv')
DATA_GENDER_SUBMISSION = pd.read_csv('../dataset/gender_submission.csv')

#出力行数設定
pd.set_option('display.max_rows',900)
print(pd.get_option('display.max_rows'))

print (DATA_TRAIN)