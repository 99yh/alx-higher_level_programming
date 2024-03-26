#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const ID = 18;
const lookfor = 'https://swapi-api.alx-tools.com/api/people/' + ID + '/';

request(url, function (error, response, body) {
  if (error) return console.error(error);
  const all = JSON.parse(body);
  const needed = all.results?.filter((film) => film.characters?.includes(lookfor));
  console.log(needed.length);
});
