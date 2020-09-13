from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)
print clf
raw_input("After being fitted, the model can then be used to predict new values:\n")
result = clf.predict([[2., 2.]])
print result

raw_input("get support vectors")
print clf.support_vectors_

raw_input("get indices of support vectors")
print clf.support_
raw_input("get number of support vectors for each class")
print clf.n_support_