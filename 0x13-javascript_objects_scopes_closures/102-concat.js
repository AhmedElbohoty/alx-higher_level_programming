#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

function readFile (path) {
  return fs.readFileSync(args[2], 'utf8');
}

const file1 = readFile(args[2]);
const file2 = readFile(args[3]);

fs.writeFileSync(args[4], file1 + file2);
