#!/usr/bin/node
const arg1 = process.argv[2];
if (isNaN(arg1)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg1);
}
