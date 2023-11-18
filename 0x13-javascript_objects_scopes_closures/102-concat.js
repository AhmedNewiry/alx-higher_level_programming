#!/usr/bin/node
const fs = require('fs');
const firstf = fs.readFileSync(process.argv[2]).toString();
const secondf = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], (firstf + secondf));
