#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (!this.width && !this.height) {
      return;
    }

    c = (c || 'X');
    let output = '';
    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        output += c;
      }

      if (y < this.height - 1) {
        output += '\n';
      }
    }
    console.log(output);
  }
}

module.exports = Square;
