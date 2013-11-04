# -*- coding: cp932 -*-
import pandas as pd
import numpy as np
from pandas.tools.plotting import radviz

'''matplotlibの日本語環境'''
from matplotlib import rcParams
rcParams['font.family'] = 'IPAexGothic'
rcParams['font.sans-serif'] = ['IPAexGothic']
import matplotlib.pyplot as plt

'''データの読み込み。Windows環境はencoding='cp932'必須'''
iris = pd.read_csv('.//iris2.csv',index_col=0,encoding='cp932')

'''最初の5つを表示'''
print iris.head(n=5)

'''概要'''

iris_ab=iris.describe()
print iris_ab

'''相関係数行列'''
iris_co=iris.corr()
print iris_co


'''散布図行列'''
pd.scatter_matrix(iris,color='green',diagonal='kde',figsize=(6,6))

'''radviz'''
plt.figure()
radviz(iris,u"種類")

'''箱ひげ'''
iris.boxplot(by=u"種類")

plt.show()

iris_co.to_csv('iris_corr.csv')
