#!/usr/bin/node
const args = process.argv;
if (args.length < 3 || isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  const occurrences = parseInt(args[2]);
  for (let i = 0; i < occurrences; i++) {
    console.log('C is fun');
  }
}
