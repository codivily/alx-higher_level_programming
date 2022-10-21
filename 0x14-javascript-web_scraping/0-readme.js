#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv.slice(2)[0];

fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
