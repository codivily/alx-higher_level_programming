#!/usr/bin/node
const args = process.argv.slice(2);
let n = parseInt(args[0]);
let r = 1;

if (isNaN(n) || n === 0) {
  console.log(1);
} else {
  while (n > 0) {
    r *= n;
    n -= 1;
  }
  console.log(r);
}
