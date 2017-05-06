import tbContacts
import re
# ====================================================
# Indicators  
# ====================================================
logBook = tbContacts.loadcsv('sample.csv');

def avgWord(textList):
	a = [];
	for txt in textList:
		words = txt.split(' ');
		s = [len(re.findall(r'[a-z]|[A-Z]',word)) for word in words];
		a.append(sum(s)/len(s));
	return a;
logBook.register_non_one_zero_indicator(avgWord,"avgWord");

def avgLength(textList):
	return [len(txt) for txt in textList];
logBook.register_non_one_zero_indicator(avgLength,"avgLength");

def avgSpecial(textList):
	a = [];
	for txt in textList:
		words = txt.split(' ');
		s = [len(word)-len(re.findall(r'[a-z]|[A-Z]|[0-9]',word)) for word in words];
		a.append(sum(s)/len(s));
	return a;
logBook.register_non_one_zero_indicator(avgSpecial,"avgSpecial");

from NeuralNetwork import *

# Set Data
number 	= "+14167074099";
data 	= logBook.get_non_one_zero_methods(number)+logBook.getBut_non_one_zero_methods(number);

# Build Network
NN = NeuralNetwork(data, n=4, dW1=0.1, dW2=0.1);

# Print Network Sum Square Error
print(NN.error())

# Compute Error Rate
err = 0;
for entry in NN.get():
	err += 1*(not (entry[0][0]==NN.predict(entry[1])))
	# print( err );

print(err/len(data))
