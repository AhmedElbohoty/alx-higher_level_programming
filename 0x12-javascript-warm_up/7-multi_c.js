#!/usr/bin/node
const args = process.argv;

const integer = parseInt(args[2], 10);

if (!isNaN(integer)) {
  for (let i = 0; i < args[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
