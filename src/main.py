import numpy as np 
import pandas as pd 
#import pandas_profiling #pdの拡張機能
import matplotlib
matplotlib.use('TkAgg') # GUIバックエンドを使用するためのもの
import matplotlib.pyplot as plt
import seaborn as sns #pltの拡張機能



# データセット読み込み
DATA_TRAIN = pd.read_csv('../dataset/train.csv')
DATA_TEST = pd.read_csv('../dataset/test.csv')
DATA_GENDER_SUBMISSION = pd.read_csv('../dataset/gender_submission.csv')

#出力行数設定
pd.set_option('display.max_rows',900)
print(f"出力行数：{pd.get_option('display.max_rows')}")

#trainデータ詳細
print(f"\ntrainデータ詳細：{DATA_TRAIN.describe()}")

#sns使用例
sns.countplot(x='Pclass',hue='Survived',data=DATA_TRAIN)
plt.show()  # この行を追加