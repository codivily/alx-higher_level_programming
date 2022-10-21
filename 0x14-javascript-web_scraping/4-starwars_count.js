#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/', (_, response, body) => {
  const data = JSON.parse(body);
  let count = 0;

  data.results.forEach(item => {
    if (item.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count += 1;
    }
  });
  console.log(count);
});
