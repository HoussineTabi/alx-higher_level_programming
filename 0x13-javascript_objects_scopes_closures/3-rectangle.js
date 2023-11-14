#!/usr/bin/node
// This class describe a rectangle

class Rectangle {
	constructor(w, h) {
		if (isNaN(w) || isNaN(h) || w <= 0 || h <= 0)
		{
		} else {
			this.width = w;
			this.height = h;
		}
	}
	print() {
		let row = '';
		let i;
		for (i = 0; i < this.width; i++)
			row += 'X';
		for (i = 0; i < this.height; i++)
			console.log(row);
	}
}
module.exports = Rectangle;