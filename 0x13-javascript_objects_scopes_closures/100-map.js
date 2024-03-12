#!/usr/bin/node
const list = require('./100-data').list;
const multList = list.map((e, ind) => e * ind);
console.log(list);
console.log(multList);
