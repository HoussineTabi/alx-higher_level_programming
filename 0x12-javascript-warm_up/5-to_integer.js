#!/usr/bin/node
/*
 * script that prints My number: <first argumets convert in integer>
 * if the argument the argument can be converted to an integer
 */

if (isNaN(parseInt(process.argv[2]))) {
	console.log('Not a number');
} else {
	console.log('My number: ' + parseInt(process.argv[2]));
}
