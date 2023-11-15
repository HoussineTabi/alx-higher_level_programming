#!/usr/bin/node
// imports an array and computes a new array

const myList = require('./100-data').list;

const myList2 = myList.map((num, index) => {
  return num * index;
});

console.log(myList);
console.log(myList2);
