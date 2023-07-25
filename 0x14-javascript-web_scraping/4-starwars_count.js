#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const jsonResponse = JSON.parse(body);
    const movies = jsonResponse.results;
    const searchValue = /18/;

    for (const movie in movies) {
      const characters = movies[movie].characters;
      for (const character in characters) {
        if (characters[character].match(searchValue)) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('code: ', response.statusCode);
  }
});
