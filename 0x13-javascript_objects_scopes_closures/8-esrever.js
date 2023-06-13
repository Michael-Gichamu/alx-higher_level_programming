#!/usr/bin/node
exports.esrever = function (list) {
  const temp = [...list];
  let tempLength = temp.length;
  for (let i = 0; i < list.length; i++) {
    temp[i] = list[tempLength - 1];
    tempLength--;
  }
  return temp;
};
