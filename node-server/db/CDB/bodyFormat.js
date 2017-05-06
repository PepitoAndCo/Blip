var	moment 	= require('moment');

module.exports = function(body) {
	return body.split('\n').filter(function(m) {
		return (m !== "")&&(m.split(',').length === 3);
	}).map(function(m){ 
		var d = m.split(',');
		return '('+__number(d[0])+',\''+__date(d[1])+'\',\"'+d.slice(2,d.length).join(',')+'\")';
	}).join(',');
}
function __number(num) {
	num = num.replace(/\ |\+|\-|\(|\)/g,'').split('');
	var number = ["1","000","000","0000"];
	switch(num.length){
		case 10:
			number[1] = num.slice(0,3).join('');
			number[2] = num.slice(3,6).join('');
			number[3] = num.slice(6,10).join('');
			break;
		case 11:
			number[0] = num[0];
			number[1] = num.slice(1,4).join('');
			number[2] = num.slice(4,7).join('');
			number[3] = num.slice(7,11).join('');
			break;
		default:
			number = num;
			break;
	}
	return number.join('');
}
function __date(date) {
	return moment(new Date(Number(date))).format("YYYY-MM-DD HH:mm:ss.SSSSSS")
}