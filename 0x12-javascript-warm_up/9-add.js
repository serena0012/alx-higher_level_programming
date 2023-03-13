#!/usr/bin/node
/* A script that prints the addition of two ingeters */
function add (a, b) {
  return a + b;
}
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
