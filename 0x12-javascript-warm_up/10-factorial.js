#!/usr/bin/node
const args = process.argv;

function factorial (numb) {
  if (numb === 1) {
    return (1);
  }

  return (numb * factorial(numb - 1));
}

if (!isNaN(args[2])) {
  const num = factorial(parseInt(args[2], 10));
  console.log(num);
} else {
  console.log('1');
}
