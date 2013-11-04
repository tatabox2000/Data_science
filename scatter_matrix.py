# -*- coding: cp932 -*-
import pandas as pd
import numpy as np
from pandas.tools.plotting import radviz

'''matplotlib�̓��{���'''
from matplotlib import rcParams
rcParams['font.family'] = 'IPAexGothic'
rcParams['font.sans-serif'] = ['IPAexGothic']
import matplotlib.pyplot as plt

'''�f�[�^�̓ǂݍ��݁BWindows����encoding='cp932'�K�{'''
iris = pd.read_csv('.//iris2.csv',index_col=0,encoding='cp932')

'''�ŏ���5��\��'''
print iris.head(n=5)

'''�T�v'''

iris_ab=iris.describe()
print iris_ab

'''���֌W���s��'''
iris_co=iris.corr()
print iris_co


'''�U�z�}�s��'''
pd.scatter_matrix(iris,color='green',diagonal='kde',figsize=(6,6))

'''radviz'''
plt.figure()
radviz(iris,u"���")

'''���Ђ�'''
iris.boxplot(by=u"���")

plt.show()

iris_co.to_csv('iris_corr.csv')
