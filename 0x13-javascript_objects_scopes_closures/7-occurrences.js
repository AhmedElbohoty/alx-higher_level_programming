#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const count = list.filter(elem => elem === searchElement).length;
  return count;
};
