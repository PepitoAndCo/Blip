import numpy as np
class NeuralNetwork(object):
	def __init__(self, YX=[], n=4, dW1=0.01, dW2=0.001, replim=1e2, elim=0.001):
		# Private Globals
		self.__data = [];
		self.__m  = 0;
		self.__n  = n;
		self.__W1 = self.__W2 = [];
		self.__dW1= float(dW1);# Coerce to float
		self.__dW2= float(dW2);
		self.__replim = replim;
		self.__elim = elim;

		# Add Data
		np.random.shuffle(YX);# shuffle entry
		for yx in YX:
			self.add(yx);

	def get(self, var="*"):
		if var.upper() == "X":
			return ([x[1] for x in self.__data]);
		elif var.upper() == "Y":
			return ([x[0] for x in self.__data]);
		elif var == "*":
			return self.__data;
		else:
			return [];

	def __add(self,X,Y):
		self.__data.append([ np.array([Y,1-Y]), X]);
		self.__gradOpt_one(X);

	def add(self, entry):
		X = 0 + 1*(np.size( np.array(entry[1]) ) >= np.size( np.array(entry[0]) ));
		Y = 1 - 1*(np.size( np.array(entry[1]) ) >= np.size( np.array(entry[0]) ));
		X = np.array(entry[X]);
		Y = np.array(entry[Y]);

		if not(np.size(Y) == 1): raise ValueError("NeuralNetwork: Invalid number of Ys");
		if not(np.size(X)/np.size(X,0)==1): raise ValueError("NeuralNetwork: Invalid number of Xs, must be a vector");
		if self.__m == 0: 
			self.__m = np.size(X);
			self.__W1 = np.random.rand(self.__n,self.__m);
			self.__W2 = np.random.rand(self.__n,2);
			self.__add(X,Y);
		elif not(self.__m == np.size(X)):
			print(ResourceWarning("Invalid number of Xs, should be",np.size(X),"not",self.__m));
		else:
			self.__add(X,Y);
		np.random.shuffle(self.__data);
		return self.__data;

	def get_weights(self):return {"W1": self.__W1.tolist(),"W2": np.transpose(self.__W2).tolist()};

	def __f(self,x):return np.power(1+np.exp(-x),-1); 

	def __fp(self,x): return self.__f(x)*(1-self.__f(x));

	def __Z1(self,entry):return self.__W1.dot(np.transpose(entry));
	def __a1(self,entry):return self.__f(self.__Z1(entry));
	def __Z2(self,entry):return np.transpose(self.__W2).dot(self.__a1(entry));
	def __a2(self,entry):return self.__f(self.__Z2(entry));

	def error(self,entry="*",yreal=[]):
		if entry == "*":
			entry = self.get("X");
			yreal = self.get("Y");

		e = (np.array([1,1]).dot(self.__a2(entry)-np.transpose(yreal)))**2;
		return np.array([1 for x in range(0,len(e))]).dot(e);

	def __gradOpt(self,entry):
		dW2 = np.transpose([self.__a1(entry)*z for z in self.__fp(self.__Z2(entry))])
		tmp = self.__a2(self.get("x"))-np.transpose(self.get("y"));
		tmp = tmp.dot([1 for x in range(0,np.size(tmp,1))]);
		dW2 = tmp*dW2;

		dW1 = self.__fp(self.__Z1(entry))*((self.__W2).dot(self.__fp(self.__Z2(entry))));
		dW1 = np.array([dW1[i]*entry for i in range(0,len(dW1)) ]);

		self.__W2 -= self.__dW2*dW2;
		self.__W1 -= self.__dW1*dW1;

		return self.error();

	def __gradOpt_one(self,entry):
		if np.size(self.__data,0) > 1 and (len(self.__W1) > 0 and len(self.__W2) > 0):
			err = self.__gradOpt(entry);
			rep = 0;
			while err > self.__elim and rep <= self.__replim:
				err = self.__gradOpt(entry);
				rep += 1;

			if rep > self.__replim:
				print(ResourceWarning("Repetition overload in gradient compute!"))	
			
			return err;


	def predict(self, entry):
		a2 = self.__a2(entry);
		return 0+1*(a2[0] > a2[1]);