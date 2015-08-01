import sys
import unittest
sys.path.append("..")
from NeuralNet import *

class NeuronTest(unittest.TestCase):
	
	def testWeights(self):
		_weights = 10
		Neuron = neuron(_weights)
		self.assertEqual(len(Neuron.weights),_weights+1)

if __name__ == '__main__':
	unittest.main()