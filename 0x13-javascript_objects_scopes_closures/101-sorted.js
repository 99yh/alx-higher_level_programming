#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

for (const prop in dict) {
  newDict[dict[prop]] ||= [];
  newDict[dict[prop]].push(prop);
}
console.log(newDict);
exports = newDict;
