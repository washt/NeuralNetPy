import random
from math import exp

class neuron(object):

    def __init__(self,inputs):
        
        self.numinputs = inputs + 1
        self.weights = []

        for i in range(self.numinputs):
            self.weights.append(random.uniform(-1.0,1.0))

    #for debugging, keeping for now
    def println(self):
        print self.weights, self.numinputs
        

class neuronLayer(object):
    
    def __init__(self,numns,neuralinputs):
        self.numNeurons = numns
        self.nhiddenlayer = []
        if neuralinputs > 0:
            for i in range(numns):
                self.nhiddenlayer.append(neuron(neuralinputs))   
        
    def gethiddenlayer(self,i):
        return self.nhiddenlayer[i].weights

    def getnumNeurons(self):
        return self.numNeurons

class nnet(object):
    
    def __init__(self):
        self.numinputs        = 0
        self.numoutputs       = 0
        self.hiddenlayers     = 0
        self.neuronsperhidden = 0
        self.neuronlayerlist      = []
        self.bias = 0
        
        self.buildNet()
    
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
            self.neuronlayerlist.append(neuronLayer(self.numoutputs,self.numinputs))

    def getWeights(self):
        locweights = []
        #layer
        for  x in range(self.hiddenlayers + 1):
            # neuron
            for y in range(self.neuronlayerlist[x].numNeurons):
                #weight
                for z in range(neuronlayerlist[x].nhiddenlayer[y].numinputs):
                    locweights.append(neuronLayer[x].nhiddenlayer[y].weights[z])

        return locweights
  
    def getNumWeights(self):
        weights = 0

        for x in range(self.hiddenlayers):
            for y in range(self.neuronlayerlist[x].numNeurons):
                for z in range(self.neuronlayerlist[x].nhiddenlayer[y].numinputs):
                    weights += 1

        return weights

    def pushWeights(self,neweights):
        ccweight = 0

        for x in range(self.hiddenlayers):
            for y in range(self.neuronlayerlist[x].numNeurons):
                for z in range(self.neuronlayerlist[x].nhiddenlayer[y].numinputs):
                    ccweight += 1
                    self.neuronlayerlist[x].nhiddenlayer[y].weights[z] = neweights[ccweight]

    def update(self,inputs):
        
        outputs  = []
        ccweight = 0

        if (len(inputs) != self.numinputs):
            return outputs

        for x in range(self.hiddenlayers + 1):
        
            if x > 0:
                inputs = outputs
            #clear list 
            outputs[:]  = []
            ccweight    = 0
            for  y in range(self.neuronlayerlist[x].numNeurons):
                
                Netin = 0.0
                Numinputs = self.neuronlayerlist[x].nhiddenlayer[y].numinputs

                for z in range(Numinputs - 1):
                    #sum weights*inputss
                    inputs += 1
                    Netin += self.neuronlayerlist[x].nhiddenlayer[y].weights[z] * inputs
                #add bias    
                Netin+= self.neuronlayerlist[x].nhiddenlayer[y].weights[self.numinputs - 1] *self.bias

                outputs.append(sigmoid(Netin,0))
                ccweight = 0

        return outputs

    def sigmoid(self, netin, resp):
        #@params input,activation response 
        return (1/ (1 + exp( ((-1)*netin)) / resp))