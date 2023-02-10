#!/usr/bin/node
const request = require('request');
const api = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`
request(api, function (err, res, body) {
  if (err) {		      
    console.log(err);
  }

  body = JSON.parse(body).characters;
  
  for (const character of body) {
    request(character, function (err, res, body) {
      console.log(body);
    });
  }
});
