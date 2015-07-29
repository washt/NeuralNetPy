import random as ran
import copy
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
		
		ran.seed(2)
			

		self.populationsize = populationsize
		self.mutationrate 	= mutationrate
		self.crossoverrate 	= crossoverrate
		self.numweights 	= numweights 
		self.genome 		= genome()
		self.chromosomesize = numweights

		self.population 	= []
		self.totalfitness 	= 0.1
		self.generation 	= 0.0
		self.bestgenome 	= 0
		self.bestfitness 	= 0.0
		self.worstfitness 	= 99999999.9
		self.averagefitness = 0.0

		for  x in range(populationsize):

			self.population.append(self.genome)
	
			for y in range(self.chromosomesize):
				# should this be a normal distribution 
				# or maybe a bounded by smaller range?
				self.population[x].pushweights(ran.uniform(-1.0,1.0))


	def pushNet(self,net):
		
		self.population.append(net)
		
	def crossover(self,mother,father):
		
		offspring1 = copy.copy(mother)
		offspring2 = copy.copy(father)

		return offspring1,offspring2

	def mutate(self,chromosome):
		mutatedchromo = []
		for i in chromosome:
			r = ran.uniform(-1.0,1.0)
			if r < self.mutationrate:
				i += (r * self.totalfitness)
				mutatedchromo.append(i)
		return mutatedchromo

	def getrandomchromo(self):

		ranslice = ran.uniform(0.0,1.0)
		localfitness = 0
		thechosenone = self.genome

		for genome in self.population:

			localfitness += genome.fitness

			if localfitness >= ranslice:

				thechosenone = genome
		return thechosenone