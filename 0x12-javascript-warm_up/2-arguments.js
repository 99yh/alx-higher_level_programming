#!/usr/bin/node
const total = process.argv.length;

if (total < 3) console.log('No argument');
else if (total > 3) console.log('Arguments found');
else console.log('Argument found');
