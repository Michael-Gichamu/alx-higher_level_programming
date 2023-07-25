#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const jsonResponse = JSON.parse(body);
    const characters = jsonResponse.characters;
    
    for (const character in characters) {
      request(characters[character], function (error, response, body) {
        if (error) {
          console.error(error);
        } else if (response.statusCode === 200) {
          const charjson = JSON.parse(body);
          console.log(charjson.name);
        } else {
          console.log('code: ', response.statusCode);
        }
      });
    }
  } else {
    console.log('code: ', response.statusCode);
  }
});
