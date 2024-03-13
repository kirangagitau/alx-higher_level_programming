#!/usr/bin/node

const firstArgv = process.argv[2];

if (firstArgv) {
  console.log(firstArgv);
} else {
  console.log('No argument');
}
