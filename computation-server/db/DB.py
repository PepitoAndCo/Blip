import pymysql.cursors

class DB(object):
	def __init__(self, DBtype, configDB):
		super(DB, self).__init__()
		self.__host 	= configDB[DBtype]["host"];
		self.__user 	= configDB[DBtype]["user"];
		self.__password = configDB[DBtype]["password"];
		self.__db 		= configDB[DBtype]["database"];
	
	def query(self, qry):
		connection = pymysql.connect(
			host 		=self.__host,
			user 		=self.__user,
			password 	=self.__password,
			db 			=self.__db,
			cursorclass =pymysql.cursors.DictCursor);
		result = "NA";
		try:
			with connection.cursor() as cursor:
				cursor.execute(qry)
				result = cursor.fetchall()
		finally:
			connection.close();
		return result;
		
class UDB(DB):
	def __init__(self, config, TYPE):
		super(UDB, self).__init__(config["DB-CONN"][TYPE+"_UDB"],config["DB"]);
		self.__type = TYPE;

	def get_table(self, _id):
		return self.query("SELECT table_name FROM "+self.__type+"_UDB WHERE "+self.__type+"_id="+ _id +";")[0]["table_name"];

class CDB(DB):
	def __init__(self, config):
		super(CDB, self).__init__(config["DB-CONN"]["CDB"],config["DB"]);
	
	def get_data(self, colname, table_name, cond=""):
		if(not(len(cond)==0)): cond = " WHERE " + cond;
		qry = "SELECT "+colname+" FROM "+table_name+cond+";";
		# print(qry);
		return self.query(qry);

	def get_dataO(self, colname, table_name, cond=""):
		return [q[colname] for q in self.get_data(colname,table_name, cond)];
