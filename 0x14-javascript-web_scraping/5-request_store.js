#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const [url, filepath] = process.argv.slice(2);

request(url, (_, response, body) => {
  fs.writeFile(filepath, body, _ => {});
});
