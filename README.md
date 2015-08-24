# Python implementation of various machine learning techniques with a feed forward neural network 

[![Build Status](https://travis-ci.org/washt/NeuralNetPy.svg)](https://travis-ci.org/washt/NeuralNetPy)
[![Coverage Status](https://coveralls.io/repos/washt/NeuralNetPy/badge.svg?branch=master&service=github)](https://coveralls.io/github/washt/NeuralNetPy?branch=master)

##Features
* `nnet` class provides basic structure and accessor methods for a generic feed-forward Neural Network. (__completed__)
* `geneticAlg` class implements a genetic algorithim for the `nnet` class, based on [ai-junkie's C++ implementation.](http://www.ai-junkie.com/ann/evolved/nnt1.html) (__partially__ __implemented__)
* `neat` class is an implementation of the GE decribed in the [NEAT Paper](http://mitpress.mit.edu/journals), again using the `nnet` class. (__partially__ __implemented__)

##Dependencies

   __Implementation__
   * numpy (for matrix math)
   * sklearn (for test datasets)
   * matplotlib (not really nessessary, mainly to visualize test datasets nicely)
   __Testing__
   * nose
   * coveralls

##TODO
* convert from unittest to nose
* set up coveralls 
* add/implement backpropagation class
* add/implement restricted boltzman machine class