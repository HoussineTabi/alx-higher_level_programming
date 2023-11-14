#!/usr/bin/node
/*
Script that prints x times the string "C is fun"
*/

if (process.argv[2] === null || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurences')
}
else {
  let i;
  for (i = 0; i < parseInt(process.argv[2]); i++) {
		console.log('C is fun');
  }
}
