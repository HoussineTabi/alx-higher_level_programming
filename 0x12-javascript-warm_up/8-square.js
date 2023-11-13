#!/usr/bin/node
/*
Script that prints x times the string "C is fun"
*/

if (process.argv[2] === null || isNaN(parseInt(process.argv[2]))) {
	console.log('Missing number of occurences')
}
else {
	let i, j;
	let nb = parseInt(process.argv[2]);
	for (i = 0; i < nb; i++)
		{
			let square = '';
			for (j = 0; j < nb; j++)
			{
				square +=  'X';
			}
			console.log(square);
		}
}
