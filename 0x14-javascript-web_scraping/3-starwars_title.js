#!/usr/bin/node

const request = require('request');
const movieid = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieid;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const jsonResponse = JSON.parse(body);
    console.log(jsonResponse.title);
  } else {
    console.log('code: ', response.statusCode);
  }
});
