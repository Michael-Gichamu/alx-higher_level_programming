#!/usr/bin/node
const parsedInt = parseInt(process.argv[2]);
if (Number.isNaN(parsedInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parsedInt; i++) {
    let string;
    for (let i = 0; i < parsedInt; i++) {
      if (i === 0) {
        string = 'X';
      } else {
        string += 'X';
      }
    }
    console.log(string);
  }
}
