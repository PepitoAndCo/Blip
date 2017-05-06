import re

def avgWord(textList):
	a = [];
	for txt in textList:
		words = txt.split(' ');
		s = [len(re.findall(r'[a-z]|[A-Z]',word)) for word in words];
		a.append(sum(s)/len(s));
	return a;

def avgLength(textList):
	return [len(txt) for txt in textList];

def avgSpecial(textList):
	a = [];
	for txt in textList:
		words = txt.split(' ');
		s = [len(word)-len(re.findall(r'[a-z]|[A-Z]|[0-9]',word)) for word in words];
		a.append(sum(s)/len(s));
	return a;