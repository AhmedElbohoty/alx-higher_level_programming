#!/usr/bin/node
const list = require('./100-data.js').list;
const multList = list.map((e, ind) => e * ind);
console.log(list);
console.log(multList);
