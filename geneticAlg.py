from NeuralNet import * 

class genome(object):
	"""genome for a given instance of an ANN"""
	def __init__(self, fitness, weights):
		
		self.fitness = fitness
		self.weights = weights
		

class geneticAlg(object):
	"""GE that evolves topoology and weights of ANN"""

	def __init__(self, population):
		
		population = []

	def pushNet(self,net):
		
		self.population.append(net)
		