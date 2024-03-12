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
}

module.exports = Rectangle;
