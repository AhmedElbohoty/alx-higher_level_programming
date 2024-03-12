#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

function readFile (path) {
  return fs.readFileSync(path, 'utf-8');
}

function writeToFile (file) {
  fs.appendFile(file3, file + '\n', (err) => err);
}

const file1 = readFile(args[2]);
const file2 = readFile(args[3]);
const file3 = readFile(args[4]);

writeToFile(file1);
writeToFile(file2);
