import unittest
from NeuralNet import neuron

class NeuronTest(unittest.TestCase):
	
	def testWeights(self):
		self.assertFalse(NeuralNet.weights,None)