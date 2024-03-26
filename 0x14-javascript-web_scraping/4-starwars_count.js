#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const lookfor = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, function (error, response, body) {
  if (error) return console.error(error);
  const all = JSON.parse(body);
  const needed = all.results?.filter((film) => film.characters?.includes(lookfor));
  console.log(needed.length);
});
