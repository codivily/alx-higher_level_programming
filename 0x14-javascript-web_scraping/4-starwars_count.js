#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/', (_, response, body) => {
  const data = JSON.parse(body).results;

  const count = data.reduce((count, item) => {
    for (const url of item.characters) {
      if (url.indexOf('18') !== -1) {
        return count + 1;
      }
    }
    return count;
  }, 0);

  console.log(count);
});
