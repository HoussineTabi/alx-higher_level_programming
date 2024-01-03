#!/usr/bin/node
/*
Write a script to read and print the content of a file.


The first argument is the file path
The content of the file must be read with utf-8
If an error occurred during the reading, print error object
*/
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, file) {
  if (err) {
    return console.log(err);
  } else {
    console.log(file);
  }
});
