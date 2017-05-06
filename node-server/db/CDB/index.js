var bodyFormat = require('./bodyFormat.js');

module.exports = function(config) {
	var _id;
	var self = this;
	this.addMessage = function(tblname, body, cb) {
		if(bodyFormat(body) !== ""){
			conn().query('SELECT COUNT(*) FROM ' + tblname).then(function() {
				conn().query('INSERT INTO ' + tblname + ' VALUES' + bodyFormat(body))
					.then(function(row) {
						__log(__id, "Finished pushing to database");
						cb(200, "Successfully Updated");
					},function(errI) {
						__log(__id, "Encoutered errors: " + errI);
						cb(500,"Server Encountered errors");
					})
			},function(err0) {
			switch(err0.code){
				default:
					defErr(err0,cb);
					break;
				case 'ER_NO_SUCH_TABLE':
					conn().query('CREATE TABLE '+tblname+' '+config["DB-TEMP"]["log_template"]).then(function(rows) {
							__log(__id,'Successfully created new table ' + tblname);
							self.addMessage(tblname, body, cb);					
						},function(errT) {
							defErr(errT,cb)
						});
						break;
			}
		})
		}	else 	{
			cb(400,"Empty or Bad Body")
		}
	}

	function conn()	{
		__id = (Math.random().toString(25).substr(2,5));
		__log(__id, "Opening connection to CDB");
		var db = require('mysql-promise')("CDB");
			db.configure(config["DB"][config["DB-CONN"]["CDB"]]);
		return db;
	}

	function defErr(err,cb) {
		__log(__id, "Unknown error happened: " + err);
		cb(500,"Unknown error happened");
	}
}

function __log(id, str) {
	console.log(" MySQL:CDB<"+id+">: " + str);
}