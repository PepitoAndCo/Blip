/*Requirements*/
var express 	= require('express'),
	bodyParser 	= require('body-parser'),
	config		= require('./config.js'),
	DB 			= require('./db')(config),
	python 		= require('./python')(config);

/*App*/ 
var app = express();

/*Encoders*/
app.use( bodyParser.text({type:'text/*'}) );       
app.use( bodyParser.json() );       
app.use(bodyParser.urlencoded({
  extended: true
})); 

//Logger
function __log_POST(id, str) {
	console.log("POST<"+id+">: " + str);
}
function __log_GET(id, str) {
	console.log("GET<"+id+">: " + str);
}

//setup endpoints
app.post('/send_text',function(req,res) {
	var __id = (Math.random().toString(25).substr(2,5))+ '/send_test';
	__log_POST(__id, 'receiving call...');
	
	reqCBDA(__log_POST, __id, req, res, function(tblname) {
		if(req.body.constructor === String)	{
			if(req.body.length && req.body.length > 0)	{
				DB.CDB.addMessage(tblname, req.body, function(CDBs,notice){
					__log_POST(__id,'call succesful')
					res.status(CDBs).send(notice);
				})
			}	else	{
				res.status(400).send("Empty Body")
			}
		}	else	{
			res.status(400).send("Invalid request body")
		}
	})
});

app.get('/weights', function(req,res) {
	var __id = (Math.random().toString(25).substr(2,5))+ '/weights';
	__log_GET(__id, 'receiving call...');

	reqCBDA(__log_GET, __id, req, res, function(tblname) {
		python.weights(tblname, function(status,data) {
			console.log(data.constructor);
			__log_GET(__id, 'call succesful');
			res.status(status).send(data);
		});
	})
	
})

//create listener
var HOST = app.listen(config.PORT || null ,function() {
	require('dns').lookup(require('os').hostname(), function (err, add, fam) {
		var out = (((HOST.address().address==='::')?add:HOST.address().address) + ':' + HOST.address().port + '\n');
		console.log('addr: %s\nfami: %s',add, fam);
		console.log('Listening on %s',out);
		require('fs').writeFileSync('./current.log', out);
	});
});

function reqCBDA(__log, __id, req, res, cb) {
	if(req.query.id) {
		var type = req.query.type || 'generic';
		if(['google','generic'].indexOf(type) > -1)	{
			__log(__id,'Calling UDB');
			DB.UDB.getCDBA(req.query.id,type,function(UDBs,tblOrErr) {
				switch(Math.floor(UDBs/100))	{
					default:
						__log(__id,'Odd status for UDB: ' + tblOrErr);
						res.status(UDBs).send('');
						break;
					case 4:
						__log(__id,'Error occurred while contacting UDB: ' + tblOrErr);
						res.status(UDBs).send(tblOrErr);
						break;
					case 5:
						__log(__id,'Error occurred while contacting UDB: ' + tblOrErr);
						res.status(UDBs).send(tblOrErr);
						break;
					case 2:
						__log(__id,'Calling CDB');
						cb(tblOrErr)
				}
			});
		}	else	{
			__log(__id,'bad user-type');
			res.status(400).send('bad user-type');
		}
	}	else 	{
		__log(__id, 'no user-id');
		res.status(400).send('no user-id');
	}
}