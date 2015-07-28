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

	def testaveFit(self):
		ga = geneticAlg(1,1,1,1)

		self.assertEqual(ga.averagefitness,0)

	def testworstFit(self):
		ga = geneticAlg(1,1,1,1)
		
		self.assertEqual(ga.worstfitness,99999999)

	def testbestGenome(self):
		ga = geneticAlg(1,1,1,1)
		
		self.assertEqual(ga.bestgenome,0)

	def testmutationRate(self):
		ga = geneticAlg(0,1,0,0)
		
		self.assertEqual(ga.mutationrate,1)

	def testcrossRate(self):
		ga = geneticAlg(0,0,1,0)
		
		self.assertEqual(ga.crossoverrate,1)

	def testgeneration(self):
		ga = geneticAlg(1,1,1,1)
		
		self.assertEqual(ga.generation,0)

	def testcrossover(self):
		ga = geneticAlg(0,0,0,0)
		
		ma = [1,1,1] 
		fa = [1,1,1]

		bab1,bab2 = ga.crossover(ma,fa)
		self.assertEqual(ma,bab1)
		self.assertEqual(fa,bab2)
		

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