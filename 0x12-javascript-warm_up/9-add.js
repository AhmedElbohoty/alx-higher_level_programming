#!/usr/bin/node
const args = process.argv;

function add (a, b) {
  return a + b;
}

const integer1 = parseInt(args[2], 10);
const integer2 = parseInt(args[3], 10);

console.log(add(integer1, integer2));
