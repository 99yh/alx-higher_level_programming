#!/usr/bin/node
try {
  const fs = require('node:fs');
  fs.writeFileSync(process.argv[2], process.argv[3]);
} catch (err) { console.error(err); }
