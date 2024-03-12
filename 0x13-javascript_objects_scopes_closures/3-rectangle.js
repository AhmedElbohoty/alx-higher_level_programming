#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!this.isValidSize(w)) return;
    if (!this.isValidSize(h)) return;

    this.width = w;
    this.height = h;
  }

  isValidSize (numb) {
    if (isNaN(numb)) return false;

    return numb > 0;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const row = 'X'.repeat(this.width);
      console.log(row);
    }
  }
}

module.exports = Rectangle;
