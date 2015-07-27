import random as ran
from NeuralNet import * 

class genome(object):
	"""genome for a given instance of an ANN"""
	def __init__(self):
		
		self.fitness = 0.0
		self.weights = []

	def pushweights(self,weight):

		self.weights.append(weight)

	def upatefitness(self,amt):
		
		self.fitness = self.fitness * amt


class geneticAlg(object):
	"""GE that evolves topoology and weights of ANN"""

	def __init__(self, populationsize, mutationrate,
					 crossoverrate, numweights):
		
		random.seed(2)
			

		self.populationsize = populationsize
		self.mutationrate 	= mutationrate
		self.crossoverrate 	= crossoverrate
		self.numweights 	= numweights 
		self.genome 		= genome()
		self.chromosomesize = numweights

		self.population 	= []
		self.totalfitness 	= 0
		self.generation 	= 0
		self.bestgenome 	= 0
		self.bestfitness 	= 0
		self.worstfitness 	= 99999999
		self.averagefitness = 0 

		for  x in range(populationsize):

			self.population.append(self.genome)
	
			for y in range(self.chromosomesize):
				# should this be a normal distribution 
				# or maybe a bounded by smaller range?
				self.population[x].pushweights(random.randint(0,100))


	def pushNet(self,net):
		
		self.population.append(net)
		