#!/usr/bin/node
module.exports.addMeMaybe = function (x, theFunction) {
  return theFunction(x + 1);
};
