#!/usr/bin/node
const args = process.argv;
if (typeof args[2] === 'undefined' || args.length === 3) {
  console.log(0);
} else {
  let temp;
  for (let i = 0; i < (args.length - 1); i++) {
    for (let i = 0; i < (args.length - 1); i++) {
      temp = args[i];
      if (temp > args[i + 1]) {
        args[i] = args[i + 1];
        args[i + 1] = temp;
    }
  }
  }
  console.log(args[(args.length - 2)]);
}
