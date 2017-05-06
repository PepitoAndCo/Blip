from .Corpus import Corpus, UDB
from .non_one_zero_indicator import add_nozi

def makeCorpus(config, tablename):
	c = Corpus(config, tablename);
	add_nozi(c);
	return c;


