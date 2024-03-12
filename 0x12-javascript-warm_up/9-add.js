#!/usr/bin/node
const args = process.argv;

function add (a, b) {
  return a + b;
}

const n1 = Number(args[2]);
const n2 = Number(args[3]);

console.log(add(n1, n2));
