#!/usr/bin/node
const dict = require('./101-data.js').dict;
const r = {};

for (const key in dict) {
  const value = dict[key];
  if (!r[value]) {
    r[value] = [];
  }
  r[value].push(key);
}

console.log(r);
