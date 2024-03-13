#!/usr/bin/node

const arg2 = process.argv[2];
const parseNum = parseInt(arg2);

if (isNaN(parseNum)) {
  console.log('Not a number');
} else {
  console.log(`My number is: ${parseNum}`);
}
