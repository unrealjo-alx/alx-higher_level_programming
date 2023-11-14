#!/usr/bin/node
const args = process.argv;
if (args.length < 3 || isNaN(args[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(args[2]);
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
