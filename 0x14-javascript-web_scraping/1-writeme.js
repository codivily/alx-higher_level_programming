#!/usr/bin/node

const fs = require('fs');
const [filepath, content] = process.argv.slice(2);

fs.writeFile(filepath, content, { flag: 'w+' }, _ => { });
