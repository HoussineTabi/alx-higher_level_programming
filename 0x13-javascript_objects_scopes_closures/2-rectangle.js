#!/usr/bin/node
// This class describe a rectangle

class Rectangle {
  constructor(w, h) {
	  if (isNaN(w) || isNaN(h) || w <= 0 || h <= 0) {
	  } else {
		  his.width = w;
		  this.height = h;
	  }
  }
}
module.exports = Rectangle;
