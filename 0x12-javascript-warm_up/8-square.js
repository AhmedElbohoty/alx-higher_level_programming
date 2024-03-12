#!/usr/bin/node
const args = process.argv;
const size = Number(args[2]);

if (size) {
  for (let i = 0; i < size; i++) {
    const row = 'X'.repeat(size);
    console.log(row);
  }
} else {
  console.log('Missing size');
}
