#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);

const [src1, src2, dest] = args;

let content = fs.readFileSync(src1, { encoding: 'utf8', flag: 'r' });
content += fs.readFileSync(src2, { encoding: 'utf8', flag: 'r' });
fs.writeFileSync(dest, content, { encoding: 'utf8' });
