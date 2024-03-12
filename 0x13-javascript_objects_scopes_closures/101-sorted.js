#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDictionary = {};
Object.keys(dict).forEach((key) => {
  if (dict[key] in newDictionary) {
    newDictionary[dict[key]].push(key);

    return;
  }
  newDictionary[dict[key]] = [key];
});

console.log(newDictionary);
