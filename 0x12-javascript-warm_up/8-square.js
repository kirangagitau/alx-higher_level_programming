#!/usr/bin/node

const sqSize = process.argv[2];
const mySq = parseInt(sqSize);
const x = 'X';

if (isNaN(mySq)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < mySq; i++) {
    console.log(x.repeat(mySq));
  }
}
