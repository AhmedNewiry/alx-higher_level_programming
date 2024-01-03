#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  body = JSON.parse(body).results;
  let count = 0;
  for (const result of body) {
    for (const character of result.characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
