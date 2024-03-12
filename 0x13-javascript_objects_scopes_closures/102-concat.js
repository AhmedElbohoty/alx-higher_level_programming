#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

const file1 = readFile(args[2]);
const file2 = readFile(args[3]);

function readFile (path) {
  return fs.readFileSync(path, 'utf-8');
}

function writeToFile (data) {
  fs.appendFile(args[4], data + '\n', (err) => err);
}

writeToFile(file1);
writeToFile(file2);
