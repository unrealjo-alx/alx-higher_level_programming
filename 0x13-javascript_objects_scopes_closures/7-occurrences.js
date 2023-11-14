#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const occurences = list.filter((e) => e === searchElement);
  return occurences.length;
};
