#!/usr/bin/node

const fs = require('node:fs');
const path = process.argv[2];

if (!path) process.exit(1);

fs.readFile(path, (err, data) => {
  if (err) console.error(err);
  else console.log('' + data);
});
