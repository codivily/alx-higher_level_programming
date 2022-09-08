#!/usr/bin/node
const process = require('node:process');
const arg = process.argv[2];

if (arg) console.log(arg);
else console.log('No argument');
