#!/usr/bin/node

const request = require('request');
const url = process.argv.slice(2)[0];

if (url == null) process.exit(-1);

request(url, (_, response, body) => {
  if (response.statusCode !== 200) return;
  const todos = JSON.parse(body);
  const users = todos.reduce((users, todo) => {
    if (todo.completed) {
      if (users[todo.userId] == null) users[todo.userId] = 1;
      else users[todo.userId] += 1;
    }
    return users;
  }, {});
  console.log(users);
});
