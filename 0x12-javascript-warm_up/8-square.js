#!/usr/bin/node
/* a script that prints a square */
const square = Math.floor(Number(process.argv[2]));
if (isNaN(square)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < square; i++) {
    console.log('XX');
  }
}
