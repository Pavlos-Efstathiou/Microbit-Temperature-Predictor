import pandas as pd
import numpy as np
import sklearn
from sklearn import datasets, svm, metrics

file_name = str(input("What's the name of the file that contains the temperature data of your micro:bit?\n"))
separator = str(input("What's the separator of your file?\n"))
predict = str(input("Name of the y column?\n"))

data = pd.read_csv(file_name, sep=separator)

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

clf = svm.SVC(kernel="rbf", C=100)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

acc = metrics.accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc}/1.0\nPredictions: {y_pred}\n")
print(f"Average Temperature: {np.mean(y_pred)}")

predictions_df = pd.DataFrame(data=y_pred.flatten())
predictions_df.plot(title="Temperature", kind="kde", fontsize=10)