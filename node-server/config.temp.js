module.exports = {
	"PORT"	: "",
	"DB"	: [
		{
			"host"		: "",
			"user"		: "",
			"password"	: "",
			"database"	: ""
		},
		{
			"host" 		: "http://",
			"port"		: ""
		}
	],
	"DB-CONN": {
		"CDB"		 : 0,
		"google_UDB" : 0,
		"apple_UDB"  : 0,
		"generic_UDB": 0,
		"python"	 : 1
	},
	"DB-TEMP": {
		"log_template"		: "(number VARCHAR(20),date DATETIME,body TEXT);",
		"google_contact_db"	: "(google_id VARCHAR(50),table_name VARCHAR(50));",
		"apple_contact_db"	: "(apple_id VARCHAR(50),table_name VARCHAR(50));",
		"generic_contact_db": "(generic_id VARCHAR(50),table_name VARCHAR(50));"
	}
}