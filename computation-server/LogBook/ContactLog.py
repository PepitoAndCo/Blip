import csv
import re
import datetime

class Contact(object):
	"""docstring for Contact"""
	def __init__(this, number, logs=False):
		this.message_log = [];
		this.phone = ["+1","000","000","0000"];
		number = re.sub(r'\ |\+|\-|\(|\)','',str(number));
		if(len(number) == 10):
			this.phone[1] = number[0:3];
			this.phone[2] = number[3:6];
			this.phone[3] = number[6:];
		elif(len(number) == 11):
			this.phone[0] = "+" + number[0];
			this.phone[1] = number[1:4];
			this.phone[2] = number[4:7];
			this.phone[3] = number[7:];
		else:
			print(ResourceWarning("Invalid Number"), number);
			this.phone = False;
		
		if logs:
			if len(logs) >0:
				this.log(logs);

	def number(this):
		if this.phone:
			return ''.join(this.phone);
		else:
			return '+10000000000';

	def numComp(this, number):
		number = Contact(number);
		return number.number() == this.number();

	def log(this,logs):
		if isinstance(logs[0],str) or isinstance(logs[0],int):
			this.message_log.append([int(logs[0]),logs[1]]);		
		elif isinstance(logs[0],list):
			for log in logs:
				this.log(log);
		this.message_log = sorted(this.message_log,key=lambda x:float(x[0]));

	def message(this):
		return [m[1] for m in this.message_log];

class LogBook(object):
	__log = [];
	def log(this):
		return this.__log;

	def __add(this, number, msg=False):
		_id = this.__id(number);
		if _id == -1:
			this.__log.append(Contact(number,msg));
		elif msg:
			this.__log[_id].log(msg);

	def add(this, entry):
		if isinstance(entry,str):
			this.__add(entry);
		elif isinstance(entry,list):
			if isinstance(entry[0],list):
				for e in entry:
					this.add(e);
			else:
				if len(entry) == 1:
					this.add(entry[0]);
				elif len(entry) == 3:
					this.__add(entry[0], entry[1:3]);
				else:
					print(ResourceWarning("Invalid Entry to logBook"),entry);

	def numbers(this): return [c.number() for c in this.__log];

	def __id(this, number):
		test = Contact(number);
		try:
			return this.numbers().index(test.number());
		except ValueError:
			return -1;

	def get(this, number):
		_id = this.__id(number);
		if _id > -1:
			return this.__log[_id].message();
		else:
			return [];

	def getAll(this):
		arr =[];
		for c in this.__log:
			arr+= c.message();
		return arr;

	def getAllbut(this,number):
		_id = this.__id(number);
		arr = [];
		if _id > -1:
			for c in this.__log[:_id]+this.__log[_id+1:]:
				arr+=c.message();
			return arr;
		else:
			return this.getAll();

class Corpus(LogBook):
	def __init__(this):
		super(LogBook, this).__init__();
		this.__dic = {};
	def __compute_max(this,name):
		this.__non_one_zero_max[name] = max([max(this.__run_non_one_zero(name,number)) for number in this.numbers()]);
		return this.__non_one_zero_max[name];

	__non_one_zero_methods = {};
	__non_one_zero_max = {};
	
	def register_non_one_zero_indicator(this,fcn,name):
		this.__non_one_zero_max[name] = 0;
		this.__non_one_zero_methods[name] = fcn;
		this.__compute_max(name);

	def __run_non_one_zero(this,name, number):
		return this.__non_one_zero_methods[name](this.get(number));

	def __runBut_non_one_zero(this,name, number):
		return this.__non_one_zero_methods[name](this.getAllbut(number));

	def __runAll_non_one_zero(this,name):
		return this.__non_one_zero_methods[name](this.getAll());

	def run_non_one_zero_method(this,name,number):
		mx = this.__compute_max(name);
		return [score/mx for score in this.__run_non_one_zero(name,number)];
	
	def runBut_non_one_zero_method(this,name,number):
		mx = this.__compute_max(name);
		return [score/mx for score in this.__runBut_non_one_zero(name,number)];

	def runAll_non_one_zero_method(this,name):
		mx = this.__compute_max(name);
		return [score/mx for score in this.__runAll_non_one_zero(name)];

	def get_non_one_zero_names(this): return list(this.__non_one_zero_methods.keys());

	def get_non_one_zero_methods(this, number):
		cats 	= {};
		msgs 	= this.get(number);
		for cat in this.get_non_one_zero_names():
			cats[cat] = this.run_non_one_zero_method(cat,number);
		return [[1,[cats[cat][x] for cat in cats]] for x in range(0,len(msgs))];

	def getBut_non_one_zero_methods(this, number):
		cats 	= {};
		msgs 	= this.getAllbut(number);
		for cat in this.get_non_one_zero_names():
			cats[cat] = this.runBut_non_one_zero_method(cat,number);
		return [[0,[cats[cat][x] for cat in cats]] for x in range(0,len(msgs))];

	def __getUniq(this,msgs):
		arr = [];
		for msg in msgs:
			arr += msg.split(' ');
		arr = set(arr);
		if '' in arr: arr.remove('');
		return arr;

	def __countUniq(this,msgs):
		__dic = {};
		for word in this.__getUniq(msgs):
			search = ' '.join(msgs);
			res    = len(re.findall(re.sub(r'(\)|\(|\[|\]|\$|\&)',r'\\\1',word),search));
			__dic[word] = res;
		return __dic;

	def getDic(this,number):
		msgs = this.get(number);
		if( not (number in this.__dic) ): this.__dic[number] = this.__countUniq(msgs);
		return this.__dic[number];

	def getAllDic(this):
		msgs = this.getAll();
		if( not ("all" in this.__dic) ): this.__dic["all"] = this.__countUniq(msgs);
		return this.__dic["all"];
	# #  getting the ratios of how often this word is sent to this contact, V.S to all contacts

	def getRatios(this,dic,alldic):
		ratios 	= {};
		for word in dic:
			ratios[word] = dic[word]/alldic[word];
		return ratios;

	def getFreq(this, number):
		return this.getRatios(this.getDic(number),this.getAllDic())
