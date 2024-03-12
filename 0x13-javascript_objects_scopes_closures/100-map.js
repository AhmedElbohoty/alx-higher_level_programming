#!/usr/bin/node

// script that imports an array and computes a new array.
// A new list must be created with each value equal to the value of the initial
// list, multipled by the index in the list.
const list = require('./100-data').list;
console.log(list);
const newList = list.map((num, index) => num * index);
console.log(newList);
