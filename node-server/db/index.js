
var UDB = require('./UDB'),
	CDB = require('./CDB');

module.exports = function DB(config) {
	return {
		UDB: new UDB(config),
		CDB: new CDB(config)
	} 
}