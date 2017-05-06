var request = require("request");

var __id;
module.exports = function(config) {
	var _config = config["DB"][config["DB-CONN"].python];
	var ADDR 	= _config.host + ':' + _config.port + '/';
	return {
		weights : function(tblname, cb) {
			__id = (Math.random().toString(25).substr(2,5))+ '/weights';
			__log(__id, "Making a call to python server");
			request({ 
				method: 'GET',
				url: ADDR + 'weights',
				qs: { tblname: tblname } 
			}, function (error, response, body) {
				if (error) {
					__log(__id, "Call Failed: " + error);
					cb(500,'Unknown computation error');
				}	else	{
					switch(Math.floor(response.statusCode/100)){
						case 2:
							__log(__id, "Call is successful!");
							cb(response.statusCode,body);
							break;
						default:
							__log(__id, "Server errored: status:" + response.statusCode + "\n<---[B][O][D][Y]--->\n"+body+'\n</---[B][O][D][Y]--->');
							cb(500, "Internal computation server error")
							break;
					}
					
				};
			});
		}
	};
}

function __log(id, str) {
	console.log(" python<"+id+">: " + str);
}