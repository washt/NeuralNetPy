import sys
import unittest
sys.path.append("..")
from NeuralNet import *

class NeuronTest(unittest.TestCase):
	
	def testWeights(self):
		_weights = 10
		Neuron = neuron(_weights)
		self.assertEqual(len(Neuron.weights),_weights+1)
		self.assertEqual(Neuron.numinputs,_weights+1)
		self.assertNotEqual(Neuron.weights,None)

class neuronLayerTest(unittest.TestCase):
	
	def testconstructor(self):
		nrons = 10
		inpts = 3
		nlayer = neuronLayer(nrons,inpts)
		self.assertEqual(nlayer.numNeurons,nrons)
		self.assertEqual(len(nlayer.nhiddenlayer),nrons)
		self.assertNotEqual(nlayer.nhiddenlayer,None)

	def testhiddenlayer(self):
		nrons = 10
		inpts = 3
		nlayer = neuronLayer(nrons,inpts)
		for i in xrange(nrons):
			self.assertTrue(nlayer.gethiddenlayer(i))
	def testnumneurons(self):
		nrons = 10
		inpts = 3
		nlayer = neuronLayer(nrons,inpts)
		self.assertTrue(nlayer.getnumNeurons(),nrons)

class nnetTest(unittest.TestCase):
	
	def testconstructor(self):
		nettest = nnet()
		self.assertEqual(nettest.numinputs,0)
		self.assertEqual(nettest.numoutputs,0)
		self.assertEqual(nettest.hiddenlayers,0)
		self.assertEqual(nettest.neuronsperhidden,0)
		#if not hidden layers, then nnet creates one output layer
		self.assertEqual(len(nettest.neuronlayerlist),1)
		self.assertEqual(nettest.bias,0)

	def testgetweights(self):
		
		nettest = nnet()
		self.assertEqual(len(nettest.getWeights()),0)
	

if __name__ == '__main__':
	unittest.main()