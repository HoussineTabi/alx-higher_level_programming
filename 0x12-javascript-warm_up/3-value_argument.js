#!/usr/bin/node
/*
 * A scripts that prints the first argument passed to
 */

if (process.argv[2] == undefined) {
	console.log('No argument');
}
else {
	console.log(process.argv[2]);
}
