#!/usr/bin/node
const args = parseInt(process.argv[2]);
function factorial (par) {
  if (isNaN(par) || par === 1) {
    return 1;
  } else {
    return par * factorial(par - 1);
  }
}
console.log(factorial(args));
