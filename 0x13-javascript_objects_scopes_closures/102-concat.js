#!/usr/bin/node
const fs = require('fs');
const buffers = [];

fs.readFile(process.argv[2], (err, data) => {
  if (err) return;
  buffers.push(data);
  fs.readFile(process.argv[3], (err, data) => {
    if (err) return;
    buffers.push(data);
    fs.writeFile(process.argv[4], buffers.join(''), () => {});
  });
});
