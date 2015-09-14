import random
from ad import adnumber,gh
from numpy import exp

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
    
    def __init__(self,numinputs=0,numoutputs=0,
                    hiddenlayers=0,neuronsperhidden=0,bias=0.5):

        self.numinputs        = numinputs
        self.numoutputs       = numoutputs
        self.hiddenlayers     = hiddenlayers
        self.neuronsperhidden = neuronsperhidden
        self.neuronlayerlist  = []
        self.bias             = bias
        self.errorlist        = []
        self.error            = 0.0
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
                for z in range(self.neuronlayerlist[x].nhiddenlayer[y].numinputs):
                    locweights.append(neuronLayer[x].nhiddenlayer[y].weights[z].weights)

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
    
    def getError(self):
        return self.errorlist
                
    def addLayer(self):
        '''
        Add a layer to the network, pushed to 
        either the front or back of the network.
        You can __not__ push to middle of the network.
        '''
        raise NotImplementedError

    def addConnection(self):
        ''' 
        Add a connection to the network by
        connecting a neuron's output to the input
        another neuron
        '''
        raise NotImplementedError

    def mutelayer(self):
        '''
        Remove a layer from the functionality
        of the network. Still keep reomoved layer with network
        to maintain genome persistancy
        '''
        raise NotImplementedError

    def calc_error(self,calculated,expected):
        '''
        This should be the difference between the output
        of the network and the target data corrisponding 
        to the input of the network, using the squared 
        error function. The total_error list is updated
        with every call.
        '''
        self.error = ((expected - calculated)/2)**2
        self.errorlist.append(self.error)

        return self.error

    def backpropagation(self):
        '''
        Step backwards through the network, and
        caculate the gradient function for every weight
        Apply chain rule to find a given nodes influence on the 
        output __wrt__ the value returned fromt eh total_error method.
        '''
        toterror   = total_error()
        opts = zip([adnumber(node) for node in self.getWeights()],
                   [adnumber(node) for node in self.getError()])

        optweights = [node[0].gradient(node[1]) for node in opts]
            
        return optweights

    def total_error(self):
        return sum(self.getError())
    
    def sigmoid(self, netin, resp):
        #@params input,activation response 
        return (1/ (1 + exp( ((-1)*netin)) / resp))

    def update(self,inputs):
        
        outputs  = []
        ccweight = 0

        if (len(inputs) != self.numinputs):
            return outputs

        for x in range(self.hiddenlayers + 1):
            if x > 0:
                inputs[x] = outputs[x]
            # clear list 
            outputs[:]  = []
            ccweight    = 0
            for  y in range(self.neuronlayerlist[x].numNeurons):
                Netin = 0.0
                Numinputs = self.neuronlayerlist[x].nhiddenlayer[y].numinputs
                for z in range(Numinputs - 1):
                    #sum weights*inputss
                    inputs[x] += 1
                    Netin += self.neuronlayerlist[x].nhiddenlayer[y].weights[z] * inputs[x]
                #add bias    
                Netin += self.neuronlayerlist[x].nhiddenlayer[y].weights[-1] *self.bias
                sig = (1/(1 + exp(-Netin/1)))
                outputs.append(sig)
                ccweight = 0
        return outputs
