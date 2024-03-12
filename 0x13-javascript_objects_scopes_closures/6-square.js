#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      const row = c.repeat(this.width);
      console.log(row);
    }
  }
}

module.exports = Square;
