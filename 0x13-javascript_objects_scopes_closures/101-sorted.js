#!/usr/bin/node
/*
Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
*/
const data_dict = require('./101-data').dict;
const newDict = {};

for (const key in data_dict) {
  if (typeof (newDict[data_dict[key]]) === 'undefined') {
    newDict[data_dict[key]] = [];
  }
  newDict[data_dict[key]].push(key);
}
console.log(newDict);
