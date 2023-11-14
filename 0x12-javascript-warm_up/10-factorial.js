#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2] ?? 1);
function fact (n) {
  if (n === 1) return 1;
  return n * fact(n - 1);
}
console.log(fact(num));
