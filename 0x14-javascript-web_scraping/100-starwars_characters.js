#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) {		      
    console.log(err);
  }

  body = JSON.parse(body).results;
  for (const result of body) {
    for (const character of result.characters) {
      console.log(character);
    }
  }
});
