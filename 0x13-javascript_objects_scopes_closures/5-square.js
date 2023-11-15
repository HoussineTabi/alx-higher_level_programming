#!/usr/bin/node
// This class describe a square

class Square extends squareBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
