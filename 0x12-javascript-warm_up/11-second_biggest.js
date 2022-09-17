#!/usr/bin/node
const args = [...new Set(process.argv.slice(2)
  .map(v => parseInt(v))
  .sort((a, b) => (a - b)))
];

if (args.length <= 1) {
  console.log(0);
} else {
  console.log(args[args.length - 2]);
}
