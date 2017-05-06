from .NeuralNetwork import *

__n   	 = 4;
__dW1 	 = 0.01;
__dW2 	 = 0.01;
__replim = 100;
__elim 	 = 0.1;
def get_weights(data):
	NN = NeuralNetwork(data, n=__n, dW1=__dW1, dW2=__dW2, 
		replim=__replim, elim = __elim);
	return NN.get_weights();

def names(logbook):
	return {
		"W1": logbook.get_non_one_zero_names(),
		"W2": ["hidden" for k in range(0,__n)]	
	}