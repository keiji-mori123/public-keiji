import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv('Iris.csv')

#特徴量（横列のIDになる文字たちをXに入れておく。）
X = df[['SepalLengthCm','SepalWidthCm',#エックスが大文字なのは、特徴量だから。
        'PetalLengthCm','PetalWidthCm']]#正確にCSVのカラムの文字を入れ込む。
#正解列を抜き取る。
y = df['Species']

#「データ分割」　　データを学習用80％と評価用20％に分ける。
#X_train(特徴量) y_train（正解データ）は、学習用
#X_test（特徴量） y_test（正解データ）は、評価用
X_train, X_test, y_train, y_test = train_test_split( 
    X, y, test_size=0.2, random_state=77
)#評価サイズは20％で、順番は変えずシャッフル「77」は任意の数

#決定木（ここでアルゴリズムを自由に決めて良い。）によって、平均と多数決といった精度の高い分析を行う。これがフォレスト
clf = RandomForestClassifier(random_state=77)#オブジェクトを作成し、予測の再現性を保つために、適当な77という数字を入れる。
clf.fit(X_train, y_train)#「学習」　fitメソッドで学習させる。

#「予測」　predictメソッドで、評価用の特徴量で、アヤメの予想結果一覧を得る。
pred = clf.predict(X_test)
#※※ここで、正解データと予想データを比べて制度を確認。※※

#「評価」　ここで正解率（accuracy）を評価用正解データと比べて求める。
accuracy = accuracy_score(y_test, pred)
print(accuracy)