from config import *
import db
import NeuralNetwork as NN

UDB = {
	"generic": db.UDB(config,"generic")
}

_id = "6476680478";
tablename = UDB["generic"].get_table(_id);

C = db.makeCorpus(config,tablename);
names = NN.names(C);
retdata = [];
for number in C.numbers():
	weights = NN.get_weights(C.get_non_one_zero_methods(number) + C.getBut_non_one_zero_methods(number));
	for wK in names:
		for w in weights[wK]:
			for wI in range(0,len(w)):
				retdata.append(','.join([number,wK,names[wK][wI]+str(wI),str(w[wI])]));
return ',\n'.join(retdata);

# numbers = this.numbers();
# print(this.getAll())
# print(this.get(numbers[1]))
# print(this.getAllBut(numbers[1]))

