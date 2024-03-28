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
pd.set_option('display.max_rows',100)
print(f"出力行数：{pd.get_option('display.max_rows')}")

#trainデータ詳細
#print(f"\ntrainデータ詳細：{DATA_TRAIN.describe()}")

#sns使用例
#sns.countplot(x='Pclass',hue='Survived',data=DATA_TRAIN)
#plt.show()  # この行を追加




"""
特徴量エンジニアリング
"""
#データ結合
data_all = pd.concat([DATA_TRAIN,DATA_TEST],sort = False)
#print(data_all)

#欠損データ確認
print( data_all.isnull().sum() )

#Sexを数値に置き換え
data_all['Sex'].replace(['male','female'],[0,1],inplace = True) #inplace = Trueで元データを書き換えるか

#Embarkedをデータ補完、数値へ
data_all['Embarked'].fillna('S',inplace = True) #データ欠損をSに置き換え
data_all['Embarked'].replace(['S','C','Q'],[0,1,2],inplace = True)
#print(data_all)

#データ補完
data_all['Fare'].fillna( np.mean(data_all['Fare']) , inplace = True )
data_all['Age'].fillna( np.mean(data_all['Age']) , inplace = True )

#特徴量削除
drop_columns = ['PassengerId','Name','Parch','Ticket']
data_all.drop( drop_columns, axis=1 , inplace=True )


#結合データをtrain testに分ける
FEATURED_DATA_TRAIN = data_all[:len(DATA_TRAIN)]
FEATURED_DATA_TEST = data_all[len(DATA_TRAIN):]


print (FEATURED_DATA_TRAIN ) 

print (FEATURED_DATA_TEST ) 





"""

基本的なグラフの描画
plt.plot(x, y)  # 折れ線グラフ
plt.scatter(x, y)  # 散布図
plt.bar(x, y)  # 棒グラフ
plt.hist(data)  # ヒストグラム

グラフのカスタマイズ
plt.title('Title Here')  # タイトル
plt.xlabel('X Label Here')  # X軸ラベル
plt.ylabel('Y Label Here')  # Y軸ラベル
plt.legend(['Label 1', 'Label 2'])  # 凡例
plt.grid(True)  # グリッド
plt.xlim([xmin, xmax])  # X軸の範囲
plt.ylim([ymin, ymax])  # Y軸の範囲

スタイルとカラー
plt.plot(x, y, linestyle='--', color='r', marker='o')  # プロットスタイル
plt.style.use('ggplot')  # Matplotlibスタイル

サブプロットの作成
fig, ax = plt.subplots(nrows=2, ncols=2)
ax[0, 0].plot(x, y)  # 左上のサブプロット
ax[1, 1].scatter(x, y)  # 右下のサブプロット

テキストとアノテーションの追加
plt.text(x, y, 'Text Here')  # テキスト
plt.annotate('Annotation Text', xy=(x, y), xytext=(xtext, ytext),
             arrowprops=dict(facecolor='black'))  # アノテーション

保存と表示
plt.savefig('filename.png')  # グラフの保存
plt.show()  # グラフの表示


"""