#!/usr/bin/node
const args = process.argv;

switch (args.length) {
  case 2:
    console.log('No argument');
    break;

  case 3:
    console.log('Argument found');
    break;

  default:
    console.log('Arguments found');
    break;
}
