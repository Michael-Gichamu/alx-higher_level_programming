#!/usr/bin/node
const args = (process.argv);
function add (a, b) {
  console.log(parseInt(args[2]) + parseInt(args[3]));
}
add();
