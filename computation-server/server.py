from flask import *
from config import *
import db
import NeuralNetwork as NN

UDB = {
	"generic": db.UDB(config,"generic")
}

def get_weights(tblname):
	C = db.makeCorpus(config,tblname);
	names = NN.names(C);
	retdata = [];
	for number in C.numbers():
		weights = NN.get_weights(C.get_non_one_zero_methods(number) + C.getBut_non_one_zero_methods(number));
		for wK in names:
			for w in weights[wK]:
				for wI in range(0,len(w)):
					retdata.append(','.join([number,wK,names[wK][wI]+str(wI),str(w[wI])]));
	return '\r'.join(retdata);

app = Flask(__name__)

@app.route('/weights', methods=['GET'])
def weights():
	# tblname = UDB["generic"].get_table(request.args["id"]);
	return make_response(get_weights(request.args["tblname"]), 200);

if __name__ == '__main__':
    app.run(debug=config["debug"], host=config["HOST"], port=config["PORT"])