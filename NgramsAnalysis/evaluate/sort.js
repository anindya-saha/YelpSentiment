/**
 * nodejs program for ranking N-grams in reviews.
 *  
 *  execution instructions:
 *  	node sort.js
 */

var fs = require('fs');

var readline = require('readline');
var stream = require('stream');

var fileLoc = './NegativeNgramsFiltered';
var outputFileLoc = './NegativeNgramsSorted';

var istream = fs.createReadStream(fileLoc);
var ostream = new stream;

var wstream = fs.createWriteStream(outputFileLoc);
var ngrams = {};


var rl = readline.createInterface(istream, ostream);

rl.on('line', function(line) {
  if (line.indexOf(' ') != -1) {
      var index = line.lastIndexOf(':');
      var token = line.substring(0, index);
      var freq = parseInt(line.substring(index+1));
      ngrams[token] = freq;
  }
});

rl.on('close', function() {
	
  var tokens_arr = [];
  
  for (var k in ngrams) {
	  if (ngrams.hasOwnProperty(k)) {
		  var obj = {
			key: k,
			freq: ngrams[k]
		  };
		  tokens_arr.push(obj);
	  }
  }
  
  tokens_arr.sort(function(a, b) {return b.freq - a.freq});
  
  for (var i = 0; i < tokens_arr.length; i++) {
      wstream.write(tokens_arr[i].key+ ":" + tokens_arr[i].freq)
      wstream.write('\n');
  }
  
  wstream.end();

  console.log('done');
});
