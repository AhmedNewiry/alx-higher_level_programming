#!/usr/bin/node
const fs = require('fs');
const firstf = fs.readFileSync(process.argv[2], "utf-8");
const secondf = fs.readFileSync(process.argv[3], "utf-8");
fs.writeFileSync(process.argv[4], (firstf + secondf));
