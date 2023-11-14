#!/usr/bin/node
/*
script that prints the addition of two integer
*/
function add(a , b) {
   return a + b;
}
if (isNaN(parseInt(process.argv[2]))|| isNaN(parseInt(process.argv[3]))) {
  console.log('NaN');
} else {
  console.log(add(parseInt(process.argv[2]),parseInt(process.argv[3])));
}
