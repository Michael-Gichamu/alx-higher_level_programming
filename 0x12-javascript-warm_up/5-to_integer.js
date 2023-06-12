#!/usr/bin/node
const parsedInt = parseInt(process.argv[2]);
if (Number.isNaN(parsedInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsedInt}`);
}
