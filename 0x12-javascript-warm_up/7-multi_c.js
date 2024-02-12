#!/usr/bin/node
let n = process.argv[2];

for (;n > 0; n--) console.log('C is fun');

if (isNaN(n)) console.log('Missing number of occurrences');
