#!/usr/bin/node

const request = require('request');
const url = process.argv.slice(2)[0];

if (url == null) process.exit(-1);

request(url, (_, response, body) => {
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
