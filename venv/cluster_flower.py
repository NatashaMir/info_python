import sklearn
from sklearn import cluster
import pandas as pd

data = sklearn.datasets.load_iris()
print(data.head())
X = pd.DataFrame(data.data, columns = list(data.feature_names))
print(X[:5])
model = cluster.KMeans(n_cluster=3, random_state=25)
results = model.fit(X)
X["cluster"] = results.predict(X)
X["target"] = data.target
X["c"] = "lookatmeIamimportant"
print(X[:5])
classification_result = X[["claster", "target", "c"]].groupby(["cluster", "target"]).agg("count")
print(classification_result)
