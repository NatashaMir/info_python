import pandas as pd 
from sklearn import preprocessing
from sklearn.decomposition import PCA
import pylab as plt 

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'	
data = pd.read_csv(url, sep = ';')
X = data[[u'fixed acidity',	u'volatile acidity',	u'citric acid',	u'residual sugar',	u'chlorides',	u'free sulfur dioxide',	u'total sulfur dioxide',	u'density',	u'pH',	u'sulphates',	u'alcohol']]
y = data.quality
X = preprocessing.StandardScaler().fit(X).transform(X)

model = PCA()
results = model.fit(X)
Z = results.transform(X)
plt.plot(results.explained_variance_)
plt.show()

pd.DataFrame(results.components_, columns=list([u'fixed acidity',	u'volatile acidity',	u'citric acid',	u'residual sugar',	u'chlorides',	u'free sulfur dioxide',	u'total sulfur dioxide',	u'density',	u'pH',	u'sulphates',	u'alcohol']))
