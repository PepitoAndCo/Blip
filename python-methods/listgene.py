import tbContacts
import re
import numpy as np
# ====================================================
# Indicators  
# ====================================================
logBook = tbContacts.loadcsv('sample.csv');

msgs = logBook.getAll()


def getUniq(msgs):
	arr = [];
	for msg in msgs:
		arr += msg.split(' ');
	arr = set(arr);
	arr.remove('')
	return arr; 

dic = {};
for word in getUniq(logBook.get("14167074099")):
	search = ' '.join(logBook.get("14167074099"));
	dic[word] = len(re.findall(word,search));

print(dic)
