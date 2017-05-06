import tbContacts
import re

logBook = tbContacts.loadcsv('sample.csv');
# This is an example on how to register
# new methods

# Define your function
# the input "textList" is the same as logBook.get(<some-number>)
def F(textList):
	a = [];
	for txt in textList:
		words = txt.split(' ');
		s = [len(re.findall(r'[a-z]|[A-Z]',word)) for word in words];
		a.append(sum(s)/len(s));
	
	return a;
	#MAKE SURE to return your final array!!
	#Also ensure that all final results are positive!!


# Next register the function using the following.
# the first input is the function that you just made,
# the second input is the name of the indicator you just made
logBook.register_non_one_zero_indicator(F,"avgWord");
# As the name suggests your function can 
# return any numbers (not just between 0-1)

# The following are ways to call your method

#run_non_zero_method, runs it on a particular phone number
print(logBook.run_non_one_zero_method("avgWord","+1-647-383-9095"))
# runBut_non_one_zero_method, runs it on everything BUT the number
print(logBook.runBut_non_one_zero_method("avgWord","+1-647-383-9095"))
# runAll_non_one_zero_method, runs it on everythin
print(logBook.runAll_non_one_zero_method("avgWord"))

# These method return values between one and zero,
# because they are ran through a normalizing algorithmn 
# that I wrote.

# To check what data they run on, do the following
print(logBook.get("+1-647-383-9095"))
print(logBook.getAllbut("+1-647-383-9095"))
print(logBook.getAll())























