#!/usr/bin/node
let x = process.argv[2];
let y = x;
let row = '';

for (; x > 0; x--) row += 'X';
for (;y > 0; y--) console.log(row);

if (isNaN(x)) console.log('Missing size');
