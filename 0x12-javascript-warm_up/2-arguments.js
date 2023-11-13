#!/usr/bin/node
/*
Write a script that prints a message depending of the number
of arguments passed:

If no arguments are passed to the script, prints "No argument"
If is one prints "Argument found"
otherwise, print "Arguments found"
we must use console.log(...) to print all arguments
You are not allowed to use var
*/
if (process.argv.length === 2) {
	console.log("No argument");
}
else if (process.argv.length === 3) {
	console.log('Argument found');
}
else {
	console.log('Arguments found');
}
