from .DB import *

class LogBook(CDB):
	def __init__(this, config, tablename):
		super(LogBook, this).__init__(config);
		this.tablename = tablename;

	def numbers(this):
		return list(set(this.get_dataO("number",this.tablename)));

	def get(this, number):
		return this.get_dataO("body",this.tablename, "number="+number);

	def getAllbut(this, number):
		return this.get_dataO("body",this.tablename, "not number="+number);

	def getAll(this):
		return this.get_dataO("body",this.tablename);

