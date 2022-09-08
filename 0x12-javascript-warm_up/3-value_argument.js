#!/usr/bin/node
const process = require('node:process');
const args = process.argv.slice(2);

if (args[0]) {
  console.log(...args);
} else {
  console.log('No argument');
}
