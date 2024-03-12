#!/usr/bin/node
exports.esrever = function (list) {
  const array = [];
  for (let i = list.length - 1; i >= 0; i--) {
    const elem = list[i];
    array.push(elem);
  }

  return array;
};
