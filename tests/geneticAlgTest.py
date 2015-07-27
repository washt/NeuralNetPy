import sys
import unittest
sys.path.append("..")
from geneticAlg import *

class genomeTest(unittest.TestCase):

	def testFitness(self):
		
		gen = genome()

		self.assertEqual(gen.fitness,0.0)

	def testgetWeights(self):
		
		gen = genome()

		self.assertEqual(len(gen.weights),0)

class genAlgTest(unittest.TestCase):

	def testpopSize(self):

		ga = geneticAlg(1,0,0,0)

		self.assertEqual(ga.populationsize,1)
	
	def testlenChromosome(self):
		ga = geneticAlg(0,0,0,1)

		self.assertEqual(ga.chromosomesize,1)
		self.assertEqual(ga.numweights,1)

	def testtotalFit(self):
		ga = geneticAlg(1,1,1,1)

		self.assertEqual(ga.totalfitness,0)

	def testbestFit(self):
		ga = geneticAlg(1,1,1,1)
		
		self.assertEqual(ga.bestfitness,0)	

	# def testaveFit(self):
	# 	self.fail("Not implemented")

	# def testworstFit(self):
	# 	self.fail("Not implemented")

	# def testbestGenome(self):
	# 	self.fail("Not implemented")

	# def testmutationRate(self):
	# 	self.fail("Not implemented")

	# def testcrossRate(self):
	# 	self.fail("Not implemented")

	# def testgeneration(self):
	# 	self.fail("Not implemented")

	# def testcrossover(self,ma,fa,bab1,bab2):
	# 	self.fail("Not implemented")

	# def testmutate(self,chromosome):
	# 	self.fail("Not implemented")

	# def testgetRandomchromo(self):
	# 	self.fail("Not implemented")

	# def testgetBestrandom(self,best,numclones,pop):
	# 	self.fail("Not implemented")

	# def testaverage(self):
	# 	self.fail("Not implemented")

	# def testreset(self):
	# 	self.fail("Not implemented")

	# def testgen(self,popsize,mut,cross,numweights):
	# 	self.fail("Not implemented")

	# def testEpoch(self):
	# 	self.fail("Not implemented")

	# def testgetChromosomes(self):
	# 	self.fail("Not implemented")

	# def testgetAveragefitness(self):
	# 	self.fail("Not implemented")

	# def testgetBestFitness(self):
	# 	self.fail("Not implemented")

if __name__ == '__main__':
	unittest.main()