#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!this.width && !this.height) {
      return;
    }
    let output = '';
    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        output += 'X';
      }

      if (y < this.height - 1) {
        output += '\n';
      }
    }
    console.log(output);
  }
}
module.exports = Rectangle;
