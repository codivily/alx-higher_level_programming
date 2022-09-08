#!/usr/bin/node
const process = require('node:process');
const args = process.argv.slice(2);

switch (args.length) {
  case 0: console.log('No argument'); break;
  case 1: console.log('Argument found'); break;
  default: args.forEach(arg => console.log(arg));
}
