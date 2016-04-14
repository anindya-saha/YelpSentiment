/**
 * nodejs program for ranking N-grams in reviews.
 *  
 *  execution instructions:
 *  	node rankReviewsNGrams.js
 */

var fs = require('fs');

var readline = require('readline');
var stream = require('stream');

var fileLoc = './aux_files/grepResults_reviews.txt';
var outputFileLoc = './nv_files/rankReviewsNGramsFull';

var istream = fs.createReadStream(fileLoc);
var ostream = new stream;

var wstream = fs.createWriteStream(outputFileLoc);
var unigrams = {};
var bigrams = {};
var trigrams = {};
var tetragrams = {};
var pentagrams = {};

function keepToken(token)
{
	if (token == '' || token == ' ')
		return false;
	
	return true;
}

function processToken(token)
{
	token = token.toLowerCase();
	token = token.replace(/[,\.-]*$/,"");//"|!-?'
	return token;
}

var rl = readline.createInterface(istream, ostream);

rl.on('line', function(line) {
  var tokens = line.split(' ');
  for (var i = 0; i < tokens.length; i++) 
  {
	  var token = processToken(tokens[i]);
	  
	  if (keepToken(token)) 
	  {  
		  if (unigrams[token])
			  unigrams[token]++;
		  else
			  unigrams[token] = 1;
	  }
  }
  
  for (var i = 0; i < tokens.length - 1; i++) 
  {
	  var token0 = processToken(tokens[i]);
	  var token1 = processToken(tokens[i+1]);
	  
	  if (keepToken(token0) && keepToken(token1))
	  {
		  var token = token0 + ' ' + token1;
		  
		  if (bigrams[token])
			  bigrams[token]++;
		  else
			  bigrams[token] = 1;
	  }
  }
  
  for (var i = 0; i < tokens.length - 2; i++) 
  {
	  var token0 = processToken(tokens[i]);
	  var token1 = processToken(tokens[i+1]);
	  var token2 = processToken(tokens[i+2]);
	  
	  if (keepToken(token0) && keepToken(token1)
			  				&& keepToken(token2))
	  {
		  var token = token0 + ' ' + token1 + ' ' + token2;
		  
		  if (trigrams[token])
			  trigrams[token]++;
		  else
			  trigrams[token] = 1;
	  }
  }
  
  for (var i = 0; i < tokens.length - 3; i++) 
  {
	  var token0 = processToken(tokens[i]);
	  var token1 = processToken(tokens[i+1]);
	  var token2 = processToken(tokens[i+2]);
	  var token3 = processToken(tokens[i+3]);
	  
	  if (keepToken(token0) && keepToken(token1) &&
		  keepToken(token2) && keepToken(token3)) 
	  {
		  var token = token0 + ' ' + token1
		  				+ ' ' + token2 + ' ' + token3;
		  
		  if (tetragrams[token])
			  tetragrams[token]++;
		  else
			  tetragrams[token] = 1;
	  }
  }
  
  for (var i = 0; i < tokens.length - 4; i++) 
  {
	  var token0 = processToken(tokens[i]);
	  var token1 = processToken(tokens[i+1]);
	  var token2 = processToken(tokens[i+2]);
	  var token3 = processToken(tokens[i+3]);
	  var token4 = processToken(tokens[i+4]);
	  
	  if (keepToken(token0) && keepToken(token1) &&
			  keepToken(token2) && keepToken(token3) && keepToken(token4)) 
	  {
		  var token = token0 + ' ' + token1
	  				+ ' ' + token2 + ' ' + token3 + ' ' + token4;
	  
		  if (pentagrams[token])
			  pentagrams[token]++;
		  else
			  pentagrams[token] = 1;
	  }
  }
});

rl.on('close', function() {
	
  var tokens_arr = [];
  
  for (var k in unigrams) {
	  if (unigrams.hasOwnProperty(k)) {
		  var obj = {
			key: k,
			freq: unigrams[k]
		  };
		  tokens_arr.push(obj);
	  }
  }
  
  tokens_arr.sort(function(a, b) {return b.freq - a.freq});
  
  for (var i = 0; i < tokens_arr.length; i++) {
      wstream.write(tokens_arr[i].key+ ":" + tokens_arr[i].freq)
	  wstream.write('\n');
  }
  
  tokens_arr = [];
  
  for (var k in bigrams) {
	  if (bigrams.hasOwnProperty(k)) {
		  var obj = {
			key: k,
			freq: bigrams[k]
		  };
		  tokens_arr.push(obj);
	  }
  }
  
  tokens_arr.sort(function(a, b) {return b.freq - a.freq});
  
  for (var i = 0; i < tokens_arr.length; i++) {
      wstream.write(tokens_arr[i].key+ ":" + tokens_arr[i].freq)
	  wstream.write('\n');
  }
  
  tokens_arr = [];
  
  for (var k in trigrams) {
	  if (trigrams.hasOwnProperty(k)) {
		  var obj = {
			key: k,
			freq: trigrams[k]
		  };
		  tokens_arr.push(obj);
	  }
  }
  
  tokens_arr.sort(function(a, b) {return b.freq - a.freq});
  
  for (var i = 0; i < tokens_arr.length; i++) {
      wstream.write(tokens_arr[i].key+ ":" + tokens_arr[i].freq)
	  wstream.write('\n');
  }
  
  tokens_arr = [];
  
  for (var k in tetragrams) {
	  if (tetragrams.hasOwnProperty(k)) {
		  var obj = {
			key: k,
			freq: tetragrams[k]
		  };
		  tokens_arr.push(obj);
	  }
  }
  
  tokens_arr.sort(function(a, b) {return b.freq - a.freq});
  
  for (var i = 0; i < tokens_arr.length; i++) {
      wstream.write(tokens_arr[i].key+ ":" + tokens_arr[i].freq)
	  wstream.write('\n');
  }
  
  tokens_arr = [];
  
  for (var k in pentagrams) {
	  if (pentagrams.hasOwnProperty(k)) {
		  var obj = {
			key: k,
			freq: pentagrams[k]
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
