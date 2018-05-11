import dr
import util
from numpy import *
from sklearn import tree
from time import time
import datasets

digitsData = datasets.TennisData;
N,D = digitsData.X.shape
def svmPredictWithPCA(digits, D):
	(trainData, Z, evals) = dr.pca(digits.X, 7)
	(testData, Z2, evals2) = dr.pca(digits.Xte, 7)
	print(digits.Xte.shape)
	print(testData.shape)
	X_train = trainData
	Y_train = digits.Y	
	Xte = testData
	Yte = digits.Yte
	clf = tree.DecisionTreeClassifier()
	stTrainTime = time();
	clf.fit(X_train,Y_train)
	endTrainTime = time();
	print(Xte.shape)
	Y_test_res = clf.predict(Xte)
	endTestTime = time();
	testAcc = mean((Y_test_res > 0) == (Yte > 0))
	print()
	print("the Dimension is : " + str(D))
	print("Training time : " + str((endTrainTime - stTrainTime)))
	print("Testing time : " + str((endTestTime - endTrainTime)))
	print("accuracy :" + str(testAcc))

for i in range(1):
	svmPredictWithPCA(digitsData, D - i)
