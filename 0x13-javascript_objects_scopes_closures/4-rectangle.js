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

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
