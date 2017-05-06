from .LogBook import *

class Corpus(LogBook):
	def __init__(this, config, tablename):
		super(LogBook, this).__init__(config);
		this.tablename = tablename;
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
