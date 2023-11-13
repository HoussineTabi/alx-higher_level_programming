#!/usr/bin/node
/*
Write a script that prints a square

The first argument is the size of the square
If the first argument can’t be converted to an integer, print “Missing size”
You must use console.log(...) to print all output
you are not allowed to use var
you must use a loop (while, for, etc.)
*/

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let it = 0; it < process.argv[2]; it++) {
    let line = '';
    for (let ji = 0; ji < process.argv[2]; ji++) {
      line += 'X';
    }
    console.log(line);
  }
}
