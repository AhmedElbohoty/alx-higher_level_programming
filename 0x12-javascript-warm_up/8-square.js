#!/usr/bin/node
const args = process.argv;

const width = parseInt(args[2], 10);

const row = [];

if (!isNaN(width)) {
  for (let i = 0; i < width; i++) {
    row.push('X');
  }
  for (let i = 0; i < width; i++) {
    console.log(row.join(''));
  }
} else {
  console.log('Missing size');
}
