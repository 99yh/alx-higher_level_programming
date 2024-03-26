#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) return console.error(error);
  const all = JSON.parse(body);
  const needed = all.results?.filter((film) => {
    const ID = 18;
    return film.characters?.includes('https://swapi-api.alx-tools.com/api/people/' + ID + '/');
  });
  console.log(needed.length);
});
