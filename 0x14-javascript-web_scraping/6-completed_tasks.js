#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) return console.error(error);
  const data = JSON.parse(body);
  const result = {};
  for (const item of data) {
    if (result[item.userId]) result[item.userId]++;
    else if (item.userId) result[item.userId] = 1;
  }
  console.log(result);
});
