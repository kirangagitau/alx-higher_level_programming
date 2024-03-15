#!/usr/bin/node

const argList = process.argv.slice(2);
const num = argList.map(arg => parseInt(arg));

if (num.length < 2) {
  console.log(0);
} else {
  const sortNum = num.sort((a,b) => b - a);
  console.log(sortNum[1]);
}
