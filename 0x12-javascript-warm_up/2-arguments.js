#!/usr/bin/node

const process = require('process');

let args = process.argv;

if ( args === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}