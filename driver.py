import random

class neuron(object):

    def __init__(self,inputs):
        
        self.numinputs = inputs + 1
        self.weights = []

        for i in range(self.numinputs):
            self.weights.append(random.randint(1,inputs +1))

    def println(self):
        print self.weights, self.numinputs
        
class neuronLayer(object):
    
    def __init__(self,numns,neuralinputs):
        self.numNeurons = numns
        self.neuronlist = []
        for i in range(numns):
            self.neuronlist.append(neuron(neuralinputs))
    def getnlist(self,i):
        return self.neuronlist[i].weights

class nnet(object):

    def __init__(self):
        self.numinputs        = 0
        self.numoutputs       = 0
        self.hiddenlayers     = 0
        self.neuronsperhidden = 0
        self.neuronlayer      = []
    
    def buildNet(self):
        pass
    def getWeights(self):
        pass
    def getNumWeights(self):
        pass
    def pushWeights(self):
        pass
    def update(self):
        pass
    def sigmoid(self):
        pass

if __name__ == "__main__":
    
    for i in range(10):
        l = neuronLayer(i,i)
        for x in range(i):
            print l.getnlist(x)
