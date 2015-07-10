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

    def getnumNeurons(self):
        return self.numNeurons

class nnet(object):

    def __init__(self):
        self.numinputs        = 0
        self.numoutputs       = 0
        self.hiddenlayers     = 0
        self.neuronsperhidden = 0
        self.neuronlayerlist      = []

        buildNet()
    
    def buildNet(self):
        # build layers of net
        if self.hiddenlayers > 0:
            #create first hidden layer
            self.neuronlayerlist.append(neuronLayer(self.neuronsperhidden,
                                                        self.numinputs))
            for i in range(self.hiddenlayers - 1):
                self.neuronlayerlist.append(neuronLayer(self.neuronsperhidden,
                                                            self.neuronsperhidden))
            #build output layer
            self.neuronlayerlist.append(neuronLayer(self.numoutputs,
                                                            self.neuronsperhidden))
        #build output layer
        else:
            self.neuronlayerlist(neuronLayer(self.numoutputs,numinputs))

    def getWeights(self):
        locweights = []
        #layer
        for  x in range(self.hiddenlayers + 1):
            # neuron
            for y in range(self.neuronlayerlist[x].numNeurons):
                #weight
                for z in range(neuronlayerlist[x].neuronlist[y].numinputs):
                    locweights.append(neuronLayer[x].neuronlist[y].weights[z])

        return locweights
  
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
