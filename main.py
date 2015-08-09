from NeuralNet import *
from sklearn import datasets,cross_validation
import matplotlib.pyplot as pl

fig = pl.figure(figsize=(10, 1), dpi=100)

def run():

	digits = datasets.load_digits()
	#shape data into a vector
	data = digits.images.reshape((digits.images.shape[0], -1))
	#split data in to training and test sets
	xtrain,xtest,targettrain,targettest = cross_validation.train_test_split(
										digits.data,data,test_size=0.4)
	#split test into validation and final 
	xvalidation, xtest, targetvalidation, targettest = cross_validation.train_test_split(
														xtest, targettest, test_size=0.5)
	#initialize neural net
	network = nnet(64,10,3,4,.1)
		
	for image in xtrain:
		out = network.update(image)
	print out
	
	return None








if __name__ == '__main__':
	# digits = datasets.load_digits()
	# for i in range(10):
	# 	ax = fig.add_subplot(1,10,i+1)
	# 	ax.matshow(digits.images[i], cmap='binary') 
	# 	ax.axis('off')
	# pl.show()

	run()