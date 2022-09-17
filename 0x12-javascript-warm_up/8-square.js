#!/usr/bin/node
const args = process.argv.slice(2);
const size = parseInt(args[0]);
if (isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  let output = '';
  for (let y = 0; y < size; y++) {
    for (let x = 0; x < size; x++) {
      output += 'X';
    }

    if (y < size - 1) {
      output += '\n';
    }
  }
  console.log(output);
}
