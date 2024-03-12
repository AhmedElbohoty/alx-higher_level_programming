#!/usr/bin/node
const args = process.argv;
const argsLen = args.length;

if (argsLen < 4) {
  console.log(0);
} else {
  const numbers = args.slice(2);
  const sortedArray = numbers.sort((a, b) => b - a);
  console.log(sortedArray[1]);
}
