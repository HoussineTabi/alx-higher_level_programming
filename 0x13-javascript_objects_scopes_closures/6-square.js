#!/usr/bin/node
// This class describe a square
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
	constructor(size) {
		super(size, size);
	}
	charPrint(c) {
		if (c) {
		let i, row;
		c = c + '';
		row = '';
		for (i = 0; i < this.width; i++)
			row += c;
		for (i = 0; i < this.width; i++)
			console.log(row);
		} else {
			this.print();
		}
	}
}
module.exports = Square;
