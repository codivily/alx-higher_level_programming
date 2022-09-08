#!/usr/bin/node
const process = require('node:process');
const args = process.argv.slice(2);

console.log(args[0] ? args.join(' ') : 'No argument');
