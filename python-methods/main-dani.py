import tbContacts
import re
logBook = tbContacts.loadcsv('sample.csv');

# print('all',logBook.getAll())
# print('get 16473839095',logBook.get("6473839095"))
# print('get all but 16473839095',logBook.getAllbut("16473839095"))
# print('numbers',logBook.numbers())

textList = logBook.get("6472349313");
print(textList)
a = [];
for txt in textList:
txt = textList[0];
words = txt.split(' ');
s = 0;
for word in words:
	print('word =',word);
# 	print(' > ',(re.findall(r'[a-z]|[A-Z]',word)))
# 	print(' > ',len(re.findall(r'[a-z]|[A-Z]',word)))
# 	print(' > ',len(re.findall(r'[a-z]|[A-Z]',word))>0);
# 	print(' > ',1*(len(re.findall(r'[a-z]|[A-Z]',word))>0));
# 	s=s+int(1*(len(re.findall(r'[a-z]|[A-Z]',word))>0));
# 	print('s =',s);

# print('final s = ',s)

# print(a)