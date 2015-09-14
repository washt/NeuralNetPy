from NeuralNet import *
import random as ran

class neat(object):
	"""implementation of the Neural Evolution for Augmented Topologies (NEAT)
		algoritm. [SOURCE]"""

	def __init__(self):
		
		self.generation 	   = []
		self.genotype 		   = []
		self.phenotype 		   = []
		self.global_inno_count = 0
		self.population        = []
		self.populationsize    = 100

		for i in range(self.populationsize):
			#create an initial population with zero hidden nodes
			# with 2 inputs and 1 ouput, and a random bias
			self.population.append(nnet(2,1,0,0,ran.uniform(-1.0,1.0)))

	def generation():

		raise NotImplementedError

	def crossover():

		raise NotImplementedError