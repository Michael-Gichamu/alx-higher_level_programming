#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const jsonResponse = JSON.parse(body);
    const userDict = {};

    for (const user of jsonResponse) {
      if (user.completed === true) {
        if (user.userId in userDict) {
          userDict[user.userId]++;
        } else {
          userDict[user.userId] = 1;
        }
      }
    }
    console.log(userDict);
  } else {
    console.log('code: ', response.statusCode);
  }
});
