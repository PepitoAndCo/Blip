import tbContacts
import re
logBook = tbContacts.loadcsv('sample.csv');

print('all',logBook.getAll())
print('get 16473839095',logBook.get("6473839095"))
print('get all but 16473839095',logBook.getAllbut("16473839095"))
print('numbers',logBook.numbers())

textList = logBook.get("16473839095");
print(textList)
textlengths = [0]*(len(textList));
for x in range(0,len(textList)):

	for txt in textList:
		txt = textList[x];
	words = txt.split(' ');
	s = 0;
	for word in words:
		print(' special characters ',(re.findall(r':|;|(|),',word)))
		print('word =',word);
		print(' > ',(re.findall(r'[a-z]|[A-Z]',word)))
		print(' > ',len(re.findall(r'[a-z]|[A-Z]',word)))
		print(' > ',len(re.findall(r'[a-z]|[A-Z]',word))>0);
		print(' > ',1*(len(re.findall(r'[a-z]|[A-Z]',word))>0));
		s=s+int(1*(len(re.findall(r'[a-z]|[A-Z]',word))>0));
		print('s =',s);
		textlengths[x] = s;
	print('final s = ',s)


print('textlength for this number =',(textlengths))
avgtxtlen = sum(textlengths)/len(textList);
print('average text length for this number =',avgtxtlen)

