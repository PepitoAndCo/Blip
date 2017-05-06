from .ContactLog import *
from .non_one_zero_indicator import *

def add_nozi(logBook):
	logBook.register_non_one_zero_indicator(avgWord,"avgWord");
	logBook.register_non_one_zero_indicator(avgLength,"avgLength");
	logBook.register_non_one_zero_indicator(avgSpecial,"avgSpecial");
	
def loadcsv(filename):
	lb = LogBook();
	with open(filename, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|');
		for row in spamreader:
			if(len(row)>2):
				e = [row[0],row[1],','.join(row[2:])];
				lb.add(e);

	add_nozi(lb);
	return lb;

def loadjson(json):
	lb = LogBook();
	epoch = datetime.datetime.utcfromtimestamp(0);
	for en in json:
		e = [en["number"],int((en["date"]- epoch).total_seconds() * 1000),en["body"]];
		lb.add(e);

	add_nozi(lb);
	return lb;


