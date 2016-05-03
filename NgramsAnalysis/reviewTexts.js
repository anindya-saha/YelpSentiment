/**
 * nodejs program for filtering texts of reviews.
 *  
 *  execution instructions:
 *  	node reviewTexts.js
 */

var fs = require('fs');

var readline = require('readline');
var stream = require('stream');

var fileLoc = './aux_files/grepResults.txt';
var outputFileLoc = './aux_files/grepResults_reviews.txt';

var istream = fs.createReadStream(fileLoc);
var ostream = new stream;

var wstream = fs.createWriteStream(outputFileLoc);
var reviews = [];
var reviews_strs = [];

var remove_duplicates = true;

function is_str_duplicate(str)
{
	if (reviews_strs.indexOf(str) == -1)
	{
		reviews_strs.push(str);
		return false;
	}
	else
		return true;
}

var rl = readline.createInterface(istream, ostream);

rl.on('line', function(line) {
  reviews.push(line);
});

rl.on('close', function() {
  for (var i = 0; i < reviews.length; i++) {
	  var str = reviews[i].replace(/[^\x00-\x7F]/g, "");
	  str = str.replace(/[\r\n]/g, "");
	  str = str.substring(str.lastIndexOf("||")+3);
	  
	  if (remove_duplicates)
	  {
		  var str_duplicate = is_str_duplicate(str);
		  
		  if (!str_duplicate) {
			  wstream.write(str);
			  wstream.write('\n');
		  }
	  }
	  else
	  {
		  wstream.write(str);
		  wstream.write('\n');
	  }
  }
  wstream.end();

  console.log('done');
});
