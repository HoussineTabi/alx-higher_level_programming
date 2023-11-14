#!/usr/bin/node
/*
Write a function that converts a number from base 10 to another base passed as argument:
You are not allowed to import any file
*/
exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};
