#!/usr/bin/node
const args = process.argv;

function factorial (numb) {
  if (numb === 1 || numb === 0) {
    return (1);
  }

  return (numb * factorial(numb - 1));
}

const number = Number(args[2]);

if (number) {
  const fact = factorial(number);
  console.log(fact);
} else {
  console.log('1');
}
