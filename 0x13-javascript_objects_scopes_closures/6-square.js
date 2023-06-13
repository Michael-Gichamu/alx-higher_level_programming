#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let string = '';
        for (let j = 0; j < this.width; j++) {
          string += c;
        }
        console.log(string);
      }
    }
  }
};
