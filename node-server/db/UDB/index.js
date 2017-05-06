var mysql 		= require('mysql-promise');

module.exports = function UDB(config) {
	var _id;
	var self = this;
	this.getCDBA = function(userid, type, cb) {
		conn(type).query('SELECT table_name FROM '+type+'_UDB WHERE ' + type + '_id=' + userid)
			.then(function(data) {
				switch(data[0].length)	{
					case 0:
						conn(type).query('INSERT INTO '+type+'_UDB VALUES('+userid+',\"CBD_'+type+'_'+userid+'\")').then(function(d) {
							__log(__id,'Successfully inserted new CBDA for ' + userid);
							self.getCDBA(userid, type, cb);
						},function(errT) {
							defErr(errT,cb);
						});
						break;
					case 1:
						try{
							cb(200,data[0][0].table_name);
						}catch(e){
							defErr(e,cb);
						}
						break;
					default:
						cb(500,'Unknown error happened')
				}
				
			},function(err) {
				switch(err.code){
					case 'ER_NO_SUCH_TABLE':
						conn(type).query('CREATE TABLE '+type+'_UDB ' +config["DB-TEMP"][type+"_contact_db"]).then(function(rows) {
							__log(__id,'Successfully created new table ' + type+'_UDB');
							self.getCDBA(userid, type, cb);					
						},function(errT) {
							defErr(errT,cb)
						});
						break;
					case 'ER_ACCESS_DENIED_ERROR':
						__log(__id, "Error Connecting");
						cb(503,"Could not connect to UDB");
						break;
					default:
						defErr(err,cb);
						break;
				};
			});
	}

	function conn(type)	{
		__id = (Math.random().toString(25).substr(2,5));
		__log(__id, "Opening connection to " + type + "_UDB");
		var db = require('mysql-promise')(type + "_UDB");
			db.configure(config["DB"][config["DB-CONN"][type+"_UDB"]]);
		return db;
	}

	function defErr(err,cb) {
		__log(__id, "Unknown error happened: " + err);
		cb(500,"Unknown error happened");
	}
}

function __log(id, str) {
	console.log(" MySQL:UDB<"+id+">: " + str);
}