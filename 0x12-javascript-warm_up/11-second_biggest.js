#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log('0');
} else {
  args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
