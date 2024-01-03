#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const completed = {};
  const tasks = JSON.parse(body);
  for (const task of tasks) {
    if (!completed[task.userId]) {
      completed[task.userId] = 0;
    }
    if (task.completed === true) {
      completed[task.userId] += 1;
    }
  }
  console.log(completed);
});
