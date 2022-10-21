#!/usr/bin/node

const request = require('request');
const filmId = process.argv.slice(2)[0];

request('https://swapi-api.hbtn.io/api/films/' + filmId, (_, response, body) => {
  const data = JSON.parse(body);
  console.log(data.title);
});
